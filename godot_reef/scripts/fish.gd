extends Node3D

var velocity := Vector3.ZERO
var hunger := 0.0
var is_dead := false
var max_speed := 2.5
var max_force := 4.0
var phase := 0.0

var _tail: MeshInstance3D
var _body_material: StandardMaterial3D
var _tail_base_rotation := Vector3(PI / 2.0, 0.0, 0.0)

func configure(rng: RandomNumberGenerator, spawn_position: Vector3) -> void:
    position = spawn_position
    var initial_velocity := Vector3(
        rng.randf_range(-1.0, 1.0),
        rng.randf_range(-0.45, 0.45),
        rng.randf_range(-1.0, 1.0)
    )
    if initial_velocity.length() < 0.01:
        initial_velocity = Vector3.FORWARD
    velocity = initial_velocity.normalized() * rng.randf_range(0.8, 1.6)
    phase = rng.randf_range(0.0, TAU)
    _build_visual(rng)
    update_orientation()

func _build_visual(rng: RandomNumberGenerator) -> void:
    var body := MeshInstance3D.new()
    var body_mesh := SphereMesh.new()
    body_mesh.radius = 0.5
    body_mesh.height = 1.0
    body.mesh = body_mesh
    body.scale = Vector3(0.62, 0.45, 1.25)

    _body_material = StandardMaterial3D.new()
    _body_material.albedo_color = Color.from_hsv(rng.randf(), rng.randf_range(0.55, 0.85), rng.randf_range(0.75, 1.0))
    _body_material.roughness = 0.45
    body.material_override = _body_material
    add_child(body)

    _tail = MeshInstance3D.new()
    var tail_mesh := CylinderMesh.new()
    tail_mesh.top_radius = 0.04
    tail_mesh.bottom_radius = 0.34
    tail_mesh.height = 0.58
    _tail.mesh = tail_mesh
    _tail.position = Vector3(0.0, 0.0, 0.82)
    _tail.rotation = _tail_base_rotation
    _tail.scale = Vector3(1.0, 0.7, 1.0)
    _tail.material_override = _body_material
    add_child(_tail)

    var eye_material := StandardMaterial3D.new()
    eye_material.albedo_color = Color(0.01, 0.01, 0.015, 1.0)
    eye_material.roughness = 0.25
    var eye_mesh := SphereMesh.new()
    eye_mesh.radius = 0.065
    eye_mesh.height = 0.13

    for side in [-1.0, 1.0]:
        var eye := MeshInstance3D.new()
        eye.mesh = eye_mesh
        eye.position = Vector3(0.2 * side, 0.12, -0.53)
        eye.material_override = eye_material
        add_child(eye)

func _process(_delta: float) -> void:
    if is_dead or not is_instance_valid(_tail):
        return
    var tail_rotation := _tail_base_rotation
    tail_rotation.y = sin(Time.get_ticks_msec() * 0.008 + phase) * 0.55
    _tail.rotation = tail_rotation

func update_orientation() -> void:
    if is_dead or velocity.length() < 0.01:
        return
    var direction := velocity.normalized()
    var up := Vector3.UP
    if abs(direction.dot(up)) > 0.95:
        up = Vector3.RIGHT
    look_at(global_position + direction, up)

func die() -> void:
    if is_dead:
        return
    is_dead = true
    velocity = Vector3(0.0, -0.45, 0.0)
    rotation.z = PI / 2.0
    if is_instance_valid(_body_material):
        _body_material.albedo_color = Color(0.42, 0.46, 0.49, 1.0)
