extends Node3D

signal tap(screen_position: Vector2)

var camera: Camera3D
var target := Vector3.ZERO
var yaw := 0.72
var pitch := -0.22
var distance := 14.0

var _mouse_dragging := false
var _mouse_last := Vector2.ZERO
var _mouse_moved := 0.0

var _touches: Dictionary = {}
var _single_touch_last := Vector2.ZERO
var _single_touch_moved := 0.0
var _last_pinch_distance := 0.0

func _ready() -> void:
    camera = Camera3D.new()
    camera.current = true
    camera.fov = 48.0
    add_child(camera)
    _update_camera()

func _process(_delta: float) -> void:
    _update_camera()

func reset_view() -> void:
    yaw = 0.72
    pitch = -0.22
    distance = 14.0

func _update_camera() -> void:
    if not is_instance_valid(camera):
        return
    var cp := cos(pitch)
    var offset := Vector3(
        sin(yaw) * cp,
        sin(pitch),
        cos(yaw) * cp
    ) * distance
    camera.position = target + offset
    camera.look_at(target, Vector3.UP)

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseButton:
        if event.button_index == MOUSE_BUTTON_LEFT:
            if event.pressed:
                _mouse_dragging = true
                _mouse_last = event.position
                _mouse_moved = 0.0
            else:
                if _mouse_dragging and _mouse_moved < 8.0:
                    tap.emit(event.position)
                _mouse_dragging = false
        elif event.pressed and event.button_index == MOUSE_BUTTON_WHEEL_UP:
            distance = clamp(distance - 0.9, 7.0, 24.0)
        elif event.pressed and event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
            distance = clamp(distance + 0.9, 7.0, 24.0)

    elif event is InputEventMouseMotion and _mouse_dragging:
        var delta: Vector2 = event.position - _mouse_last
        yaw -= delta.x * 0.006
        pitch = clamp(pitch - delta.y * 0.006, -1.15, 1.15)
        _mouse_moved += delta.length()
        _mouse_last = event.position

    elif event is InputEventScreenTouch:
        if event.pressed:
            _touches[event.index] = event.position
            if _touches.size() == 1:
                _single_touch_last = event.position
                _single_touch_moved = 0.0
            elif _touches.size() == 2:
                _last_pinch_distance = _current_pinch_distance()
        else:
            var was_single_touch := _touches.size() == 1
            var moved := _single_touch_moved
            _touches.erase(event.index)
            if was_single_touch and moved < 12.0:
                tap.emit(event.position)
            if _touches.size() < 2:
                _last_pinch_distance = 0.0

    elif event is InputEventScreenDrag:
        _touches[event.index] = event.position
        if _touches.size() == 1:
            var drag_delta: Vector2 = event.position - _single_touch_last
            yaw -= drag_delta.x * 0.008
            pitch = clamp(pitch - drag_delta.y * 0.008, -1.15, 1.15)
            _single_touch_moved += drag_delta.length()
            _single_touch_last = event.position
        elif _touches.size() == 2:
            var pinch_distance := _current_pinch_distance()
            if _last_pinch_distance > 0.0:
                distance = clamp(distance - (pinch_distance - _last_pinch_distance) * 0.018, 7.0, 24.0)
            _last_pinch_distance = pinch_distance

func _current_pinch_distance() -> float:
    var positions := _touches.values()
    if positions.size() < 2:
        return 0.0
    var a: Vector2 = positions[0]
    var b: Vector2 = positions[1]
    return a.distance_to(b)
