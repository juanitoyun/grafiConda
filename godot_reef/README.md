# Juanito's Reef 3D - Godot port

Godot/Web port that merges the strongest parts of the two aquarium experiments already present in this repository/account:

- `CC3501_Tarea/tarea3_acuario`: 3D boids, orbital camera, bubbles and aquarium scene.
- `jupyterlite-embed/AcuarioProyect`: live boid parameters, feeding, hunger and reset-style interaction.

## What is included

- 3D boids: separation, cohesion and alignment.
- Aquarium boundary steering.
- Procedural fish meshes and tail animation; no external assets required.
- Procedural seabed, rocks, plants, water volume and bubbles.
- Hunger + tap/click feeding behavior.
- Runtime sliders for fish count, vision, cohesion, separation, alignment and speed.
- Orbit camera on mouse drag or one-finger drag.
- Zoom with wheel or two-finger pinch.
- Responsive Web export preset designed for itch.io.
- Compatibility renderer and single-thread Web export for broad browser/mobile compatibility.

## Run in Godot

1. Install Godot 4.7.2 stable, standard build (not .NET).
2. Import `godot_reef/project.godot`.
3. Press F6/F5.

## Export for itch.io

1. In Godot, install the matching Web export template from `Editor -> Manage Export Templates`.
2. Open `Project -> Export` and select the existing `Web` preset.
3. Export to `build/web/index.html`.
4. Zip the CONTENTS of `build/web/` so `index.html` is at the root of the ZIP.
5. On itch.io create/edit a project, choose `HTML`, upload the ZIP and enable browser play/fullscreen as desired.

The preset intentionally uses `variant/thread_support=false`; this avoids cross-origin isolation requirements and is the friendlier choice for itch.io and Safari/iOS.

## Controls

- Mouse drag / one-finger drag: orbit camera.
- Mouse wheel / pinch: zoom.
- Short click / tap: drop 3-5 food pellets.
- UI: change boid parameters, fish count and speed.
- Feed: drop food in the center.
- Pause / Reset: simulation controls.

## Suggested next upgrades

- Replace procedural fish with GLB models while keeping the same `FishAgent` script.
- Add species presets with separate boid weights and swim speeds.
- Add rock/reef obstacle avoidance.
- Move neighbor lookup to a spatial hash if the target grows beyond ~100-150 fish.
- Add a small-screen UI collapse button for phones.
