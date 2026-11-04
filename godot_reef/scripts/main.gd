extends Node3D

const FishAgent = preload("res://scripts/fish.gd")
const OrbitCameraRig = preload("res://scripts/orbit_camera.gd")

var aquarium_bounds := AABB(Vector3(-6.0, -2.6, -4.0), Vector3(12.0, 5.2, 8.0))
var fishes: Array = []
var foods: Array = []
var bubbles: Array = []
var rng := RandomNumberGenerator.new()

var desired_fish_count := 50
var vision_radius := 2.8
var separation_radius := 0.82
var cohesion_weight := 0.8
var separation_weight := 1.35
var alignment_weight := 1.0
var max_speed := 2.5
var hunger_enabled := true
var hunger_rate := 1.35
var paused := false

var camera_rig
var stats_label: Label
var pause_button: Button

func _ready() -> void:
    rng.randomize()
    _build_environment()
    _build_bubbles()
    camera_rig = OrbitCameraRig.new()
    add_child(camera_rig)
    camera_rig.tap.connect(_on_camera_tap)
    _build_ui()
    _set_fish_count(desired_fish_count)

func _physics_process(delta: float) -> void:
    if not paused:
        _update_food(delta)
        _update_bubbles(delta)
        _update_fish(delta)
    _update_stats()

func _update_fish(delta: float) -> void:
    var min_bound := aquarium_bounds.position
    var floor_y := min_bound.y + 0.24

    for i in range(fishes.size()):
        var fish = fishes[i]
        if not is_instance_valid(fish):
            continue

        fish.max_speed = max_speed

        if fish.is_dead:
            fish.position.y = max(floor_y, fish.position.y - 0.42 * delta)
            continue

        if hunger_enabled:
            fish.hunger = min(100.0, fish.hunger + hunger_rate * delta)
            if fish.hunger >= 100.0:
                fish.die()
                continue
        else:
            fish.hunger = 0.0

        var acceleration := _flocking_force(i) + _boundary_force(fish)

        if hunger_enabled and fish.hunger > 30.0:
            var food_index := _nearest_food_index(fish.position)
            if food_index >= 0:
                var food_node: MeshInstance3D = foods[food_index]["node"]
                acceleration += _steer_towards(fish, food_node.position, fish.max_speed * 1.3) * 2.2
                if fish.position.distance_to(food_node.position) < 0.46:
                    _consume_food(food_index, fish)

        fish.velocity += acceleration * delta
        if fish.velocity.length() > fish.max_speed:
            fish.velocity = fish.velocity.normalized() * fish.max_speed

        fish.position += fish.velocity * delta
        fish.update_orientation()

func _flocking_force(index: int) -> Vector3:
    var fish = fishes[index]
    var separation := Vector3.ZERO
    var avg_velocity := Vector3.ZERO
    var center_of_mass := Vector3.ZERO
    var neighbor_count := 0
    var separation_count := 0

    for j in range(fishes.size()):
        if j == index:
            continue
        var other = fishes[j]
        if not is_instance_valid(other) or other.is_dead:
            continue

        var offset: Vector3 = fish.position - other.position
        var distance := offset.length()
        if distance <= 0.001 or distance > vision_radius:
            continue

        neighbor_count += 1
        avg_velocity += other.velocity
        center_of_mass += other.position

        if distance < separation_radius:
            separation += offset.normalized() / max(distance, 0.08)
            separation_count += 1

    var total_force := Vector3.ZERO

    if separation_count > 0 and separation.length() > 0.001:
        var desired_separation: Vector3 = (separation / float(separation_count)).normalized() * fish.max_speed
        total_force += (desired_separation - fish.velocity).limit_length(fish.max_force) * separation_weight

    if neighbor_count > 0:
        var desired_alignment: Vector3 = avg_velocity / float(neighbor_count)
        if desired_alignment.length() > 0.001:
            desired_alignment = desired_alignment.normalized() * fish.max_speed
            total_force += (desired_alignment - fish.velocity).limit_length(fish.max_force) * alignment_weight

        var center: Vector3 = center_of_mass / float(neighbor_count)
        var to_center: Vector3 = center - fish.position
        if to_center.length() > 0.001:
            var desired_cohesion: Vector3 = to_center.normalized() * fish.max_speed
            total_force += (desired_cohesion - fish.velocity).limit_length(fish.max_force) * cohesion_weight

    return total_force

func _boundary_force(fish) -> Vector3:
    var min_bound := aquarium_bounds.position
    var max_bound := aquarium_bounds.position + aquarium_bounds.size
    var margin := 0.85
    var strength: float = fish.max_force * 1.6
    var force := Vector3.ZERO

    if fish.position.x < min_bound.x + margin:
        force.x += strength
    elif fish.position.x > max_bound.x - margin:
        force.x -= strength

    if fish.position.y < min_bound.y + margin:
        force.y += strength
    elif fish.position.y > max_bound.y - margin:
        force.y -= strength

    if fish.position.z < min_bound.z + margin:
        force.z += strength
    elif fish.position.z > max_bound.z - margin:
        force.z -= strength

    return force

func _steer_towards(fish, target: Vector3, target_speed: float) -> Vector3:
    var desired: Vector3 = target - fish.position
    if desired.length() < 0.001:
        return Vector3.ZERO
    desired = desired.normalized() * target_speed
    return (desired - fish.velocity).limit_length(fish.max_force)

func _nearest_food_index(position: Vector3) -> int:
    var best_index := -1
    var best_distance := INF
    for i in range(foods.size()):
        var node = foods[i]["node"]
        if not is_instance_valid(node):
            continue
        var distance: float = position.distance_squared_to(node.position)
        if distance < best_distance:
            best_distance = distance
            best_index = i
    return best_index

func _consume_food(index: int, fish) -> void:
    if index < 0 or index >= foods.size():
        return
    var node = foods[index]["node"]
    if is_instance_valid(node):
        node.queue_free()
    foods.remove_at(index)
    fish.hunger = max(0.0, fish.hunger - 48.0)

func _update_food(delta: float) -> void:
    var floor_y := aquarium_bounds.position.y + 0.3
    for i in range(foods.size() - 1, -1, -1):
        var item: Dictionary = foods[i]
        var node = item["node"]
        if not is_instance_valid(node):
            foods.remove_at(i)
            continue

        item["age"] = float(item["age"]) + delta
        node.position.y = max(floor_y, node.position.y - 0.62 * delta)
        node.position.x += sin(float(item["age"]) * 2.2 + float(item["phase"])) * 0.04 * delta
        foods[i] = item

        if float(item["age"]) > 22.0:
            node.queue_free()
            foods.remove_at(i)

func _spawn_food(world_position: Vector3, amount := 4) -> void:
    var max_bound := aquarium_bounds.position + aquarium_bounds.size
    for _i in range(amount):
        var pellet := MeshInstance3D.new()
        var mesh := SphereMesh.new()
        mesh.radius = 0.09
        mesh.height = 0.18
        pellet.mesh = mesh

        var material := StandardMaterial3D.new()
        material.albedo_color = Color(0.45, 0.22, 0.07, 1.0)
        material.roughness = 0.9
        pellet.material_override = material

        pellet.position = Vector3(
            clamp(world_position.x + rng.randf_range(-0.35, 0.35), aquarium_bounds.position.x + 0.25, max_bound.x - 0.25),
            max_bound.y - 0.25,
            clamp(world_position.z + rng.randf_range(-0.35, 0.35), aquarium_bounds.position.z + 0.25, max_bound.z - 0.25)
        )
        add_child(pellet)
        foods.append({
            "node": pellet,
            "age": 0.0,
            "phase": rng.randf_range(0.0, TAU)
        })

func _on_camera_tap(screen_position: Vector2) -> void:
    if camera_rig == null or not is_instance_valid(camera_rig.camera):
        return
    var camera: Camera3D = camera_rig.camera
    var ray_origin := camera.project_ray_origin(screen_position)
    var ray_direction := camera.project_ray_normal(screen_position)
    var plane := Plane(Vector3.UP, 0.0)
    var hit = plane.intersects_ray(ray_origin, ray_direction)
    if hit == null:
        return
    _spawn_food(hit, rng.randi_range(3, 5))

func _feed_center() -> void:
    _spawn_food(Vector3.ZERO, 5)

func _set_fish_count(target_count: int) -> void:
    desired_fish_count = clamp(target_count, 10, 100)

    while fishes.size() < desired_fish_count:
        var fish = FishAgent.new()
        add_child(fish)
        fish.configure(rng, _random_spawn_position())
        fish.max_speed = max_speed
        fishes.append(fish)

    while fishes.size() > desired_fish_count:
        var fish = fishes.pop_back()
        if is_instance_valid(fish):
            fish.queue_free()

func _random_spawn_position() -> Vector3:
    var min_bound := aquarium_bounds.position + Vector3(0.9, 0.9, 0.9)
    var max_bound := aquarium_bounds.position + aquarium_bounds.size - Vector3(0.9, 0.9, 0.9)
    return Vector3(
        rng.randf_range(min_bound.x, max_bound.x),
        rng.randf_range(min_bound.y, max_bound.y),
        rng.randf_range(min_bound.z, max_bound.z)
    )

func _reset_simulation() -> void:
    for fish in fishes:
        if is_instance_valid(fish):
            fish.queue_free()
    fishes.clear()

    for item in foods:
        var node = item["node"]
        if is_instance_valid(node):
            node.queue_free()
    foods.clear()

    _set_fish_count(desired_fish_count)
    camera_rig.reset_view()

func _toggle_pause() -> void:
    paused = not paused
    pause_button.text = "Resume" if paused else "Pause"

func _build_environment() -> void:
    var world_environment := WorldEnvironment.new()
    var environment := Environment.new()
    environment.background_mode = Environment.BG_COLOR
    environment.background_color = Color(0.012, 0.07, 0.11, 1.0)
    environment.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
    environment.ambient_light_color = Color(0.28, 0.55, 0.68, 1.0)
    environment.ambient_light_energy = 1.15
    world_environment.environment = environment
    add_child(world_environment)

    var sun := DirectionalLight3D.new()
    sun.rotation_degrees = Vector3(-52.0, -28.0, 0.0)
    sun.light_color = Color(0.72, 0.9, 1.0, 1.0)
    sun.light_energy = 1.15
    sun.shadow_enabled = false
    add_child(sun)

    var fill_light := OmniLight3D.new()
    fill_light.position = Vector3(0.0, 2.6, 0.0)
    fill_light.omni_range = 14.0
    fill_light.light_energy = 1.5
    fill_light.light_color = Color(0.25, 0.72, 0.9, 1.0)
    add_child(fill_light)

    var floor := MeshInstance3D.new()
    var floor_mesh := BoxMesh.new()
    floor_mesh.size = Vector3(12.0, 0.22, 8.0)
    floor.mesh = floor_mesh
    floor.position = Vector3(0.0, aquarium_bounds.position.y + 0.1, 0.0)
    var floor_material := StandardMaterial3D.new()
    floor_material.albedo_color = Color(0.42, 0.34, 0.22, 1.0)
    floor_material.roughness = 1.0
    floor.material_override = floor_material
    add_child(floor)

    var water := MeshInstance3D.new()
    var water_mesh := BoxMesh.new()
    water_mesh.size = aquarium_bounds.size
    water.mesh = water_mesh
    water.position = aquarium_bounds.position + aquarium_bounds.size * 0.5
    var water_material := StandardMaterial3D.new()
    water_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    water_material.albedo_color = Color(0.04, 0.38, 0.52, 0.055)
    water_material.roughness = 0.2
    water.material_override = water_material
    add_child(water)

    for _i in range(9):
        var rock := MeshInstance3D.new()
        var rock_mesh := SphereMesh.new()
        rock_mesh.radius = rng.randf_range(0.35, 0.7)
        rock_mesh.height = rock_mesh.radius * 2.0
        rock.mesh = rock_mesh
        rock.scale = Vector3(rng.randf_range(1.0, 1.7), rng.randf_range(0.45, 0.8), rng.randf_range(0.8, 1.4))
        rock.position = Vector3(
            rng.randf_range(-5.0, 5.0),
            aquarium_bounds.position.y + rng.randf_range(0.28, 0.45),
            rng.randf_range(-3.1, 3.1)
        )
        var rock_material := StandardMaterial3D.new()
        rock_material.albedo_color = Color(0.18, 0.22, 0.2, 1.0).lightened(rng.randf_range(0.0, 0.12))
        rock_material.roughness = 1.0
        rock.material_override = rock_material
        add_child(rock)

    for _i in range(14):
        var plant := MeshInstance3D.new()
        var plant_mesh := CylinderMesh.new()
        plant_mesh.top_radius = 0.04
        plant_mesh.bottom_radius = 0.09
        plant_mesh.height = rng.randf_range(0.8, 1.8)
        plant.mesh = plant_mesh
        plant.position = Vector3(
            rng.randf_range(-5.4, 5.4),
            aquarium_bounds.position.y + plant_mesh.height * 0.5 + 0.2,
            rng.randf_range(-3.5, 3.5)
        )
        plant.rotation_degrees = Vector3(rng.randf_range(-8.0, 8.0), rng.randf_range(0.0, 180.0), rng.randf_range(-8.0, 8.0))
        var plant_material := StandardMaterial3D.new()
        plant_material.albedo_color = Color(0.05, rng.randf_range(0.35, 0.65), 0.22, 1.0)
        plant_material.roughness = 0.8
        plant.material_override = plant_material
        add_child(plant)

func _build_bubbles() -> void:
    var bubble_mesh := SphereMesh.new()
    bubble_mesh.radius = 0.06
    bubble_mesh.height = 0.12
    var bubble_material := StandardMaterial3D.new()
    bubble_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    bubble_material.albedo_color = Color(0.72, 0.92, 1.0, 0.42)
    bubble_material.roughness = 0.05

    for _i in range(26):
        var bubble := MeshInstance3D.new()
        bubble.mesh = bubble_mesh
        bubble.material_override = bubble_material
        bubble.scale = Vector3.ONE * rng.randf_range(0.65, 1.45)
        bubble.position = Vector3(
            rng.randf_range(-5.2, 5.2),
            rng.randf_range(aquarium_bounds.position.y + 0.4, aquarium_bounds.position.y + aquarium_bounds.size.y - 0.4),
            rng.randf_range(-3.4, 3.4)
        )
        add_child(bubble)
        bubbles.append({
            "node": bubble,
            "speed": rng.randf_range(0.35, 0.8),
            "phase": rng.randf_range(0.0, TAU),
            "age": rng.randf_range(0.0, 10.0)
        })

func _update_bubbles(delta: float) -> void:
    var min_bound := aquarium_bounds.position
    var max_bound := aquarium_bounds.position + aquarium_bounds.size

    for i in range(bubbles.size()):
        var item: Dictionary = bubbles[i]
        var bubble = item["node"]
        if not is_instance_valid(bubble):
            continue

        item["age"] = float(item["age"]) + delta
        bubble.position.y += float(item["speed"]) * delta
        bubble.position.x += sin(float(item["age"]) * 1.7 + float(item["phase"])) * 0.08 * delta

        if bubble.position.y > max_bound.y - 0.2:
            bubble.position = Vector3(
                rng.randf_range(min_bound.x + 0.6, max_bound.x - 0.6),
                min_bound.y + 0.35,
                rng.randf_range(min_bound.z + 0.6, max_bound.z - 0.6)
            )
        bubbles[i] = item

func _build_ui() -> void:
    var layer := CanvasLayer.new()
    add_child(layer)

    var panel := PanelContainer.new()
    panel.position = Vector2(14.0, 14.0)
    panel.custom_minimum_size = Vector2(250.0, 0.0)
    var panel_style := StyleBoxFlat.new()
    panel_style.bg_color = Color(0.015, 0.06, 0.08, 0.84)
    panel_style.border_width_left = 1
    panel_style.border_width_top = 1
    panel_style.border_width_right = 1
    panel_style.border_width_bottom = 1
    panel_style.border_color = Color(0.2, 0.75, 0.88, 0.55)
    panel_style.corner_radius_top_left = 10
    panel_style.corner_radius_top_right = 10
    panel_style.corner_radius_bottom_left = 10
    panel_style.corner_radius_bottom_right = 10
    panel.add_theme_stylebox_override("panel", panel_style)
    layer.add_child(panel)

    var box := VBoxContainer.new()
    box.add_theme_constant_override("separation", 5)
    panel.add_child(box)

    var title := Label.new()
    title.text = "JUANITO'S REEF 3D"
    title.add_theme_font_size_override("font_size", 18)
    box.add_child(title)

    var controls := Label.new()
    controls.text = "Drag/touch: orbit   Wheel/pinch: zoom\nTap/click: drop food"
    controls.modulate = Color(0.78, 0.9, 0.95, 1.0)
    box.add_child(controls)

    _add_slider(box, "Fish", 10.0, 100.0, 1.0, float(desired_fish_count), _on_fish_count_changed)
    _add_slider(box, "Vision", 1.4, 5.0, 0.1, vision_radius, _on_vision_changed)
    _add_slider(box, "Cohesion", 0.0, 2.0, 0.05, cohesion_weight, _on_cohesion_changed)
    _add_slider(box, "Separation", 0.0, 3.0, 0.05, separation_weight, _on_separation_changed)
    _add_slider(box, "Alignment", 0.0, 2.0, 0.05, alignment_weight, _on_alignment_changed)
    _add_slider(box, "Speed", 1.0, 5.0, 0.1, max_speed, _on_speed_changed)

    var hunger_toggle := CheckButton.new()
    hunger_toggle.text = "Hunger + feeding"
    hunger_toggle.button_pressed = hunger_enabled
    hunger_toggle.toggled.connect(_on_hunger_toggled)
    box.add_child(hunger_toggle)

    var button_row := HBoxContainer.new()
    box.add_child(button_row)

    pause_button = Button.new()
    pause_button.text = "Pause"
    pause_button.pressed.connect(_toggle_pause)
    button_row.add_child(pause_button)

    var feed_button := Button.new()
    feed_button.text = "Feed"
    feed_button.pressed.connect(_feed_center)
    button_row.add_child(feed_button)

    var reset_button := Button.new()
    reset_button.text = "Reset"
    reset_button.pressed.connect(_reset_simulation)
    button_row.add_child(reset_button)

    stats_label = Label.new()
    stats_label.modulate = Color(0.62, 0.88, 0.72, 1.0)
    box.add_child(stats_label)

func _add_slider(parent: VBoxContainer, label_text: String, minimum: float, maximum: float, step: float, value: float, callback: Callable) -> void:
    var row := HBoxContainer.new()
    parent.add_child(row)

    var label := Label.new()
    label.text = label_text
    label.custom_minimum_size = Vector2(78.0, 0.0)
    row.add_child(label)

    var slider := HSlider.new()
    slider.min_value = minimum
    slider.max_value = maximum
    slider.step = step
    slider.value = value
    slider.size_flags_horizontal = Control.SIZE_EXPAND_FILL
    slider.custom_minimum_size = Vector2(145.0, 0.0)
    slider.value_changed.connect(callback)
    row.add_child(slider)

func _update_stats() -> void:
    if not is_instance_valid(stats_label):
        return
    var living := 0
    var total_hunger := 0.0
    for fish in fishes:
        if is_instance_valid(fish) and not fish.is_dead:
            living += 1
            total_hunger += fish.hunger
    var average_hunger := total_hunger / float(max(living, 1))
    stats_label.text = "Fish %d/%d | Food %d | Hunger %.0f%% | FPS %d" % [living, fishes.size(), foods.size(), average_hunger, Engine.get_frames_per_second()]

func _on_fish_count_changed(value: float) -> void:
    _set_fish_count(int(value))

func _on_vision_changed(value: float) -> void:
    vision_radius = value

func _on_cohesion_changed(value: float) -> void:
    cohesion_weight = value

func _on_separation_changed(value: float) -> void:
    separation_weight = value

func _on_alignment_changed(value: float) -> void:
    alignment_weight = value

func _on_speed_changed(value: float) -> void:
    max_speed = value

func _on_hunger_toggled(enabled: bool) -> void:
    hunger_enabled = enabled
    if not hunger_enabled:
        for fish in fishes:
            if is_instance_valid(fish) and not fish.is_dead:
                fish.hunger = 0.0
