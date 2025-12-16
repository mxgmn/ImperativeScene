main_entrance.max.x = scene.max.x
main_entrance.center.y = scene.min.y + 0.25 * scene.depth
main_entrance.min.z = scene.min.z
main_entrance.facing = X_MIN

backdoor.min.x = scene.min.x
backdoor.center.y = scene.min.y + 0.85 * scene.depth
backdoor.min.z = scene.min.z
backdoor.facing = X_MAX

stage.center.x = scene.center.x
stage.max.y = scene.max.y
stage.min.z = scene.min.z
stage.facing = Y_MIN

set_coordinate_frame(stage)
piano.min.x = stage.min.x + 0.2
piano.center.y = stage.min.y + 0.5 * stage.depth
piano.min.z = stage.max.z
piano.facing = X_MIN
decoration.center.x = stage.center.x
decoration.min.y = stage.min.y
decoration.min.z = stage.max.z
decoration.facing = stage.facing
set_coordinate_frame(scene)

for i, seat in enumerate(seats):
    column = i % 8
    row = i // 8
    seat.center.x = scene.min.x + (column+1.0) / 9.0 * scene.width
    seat.center.y = scene.min.y + (row+1.0) / 6.0 * (scene.depth - stage.depth)
    seat.min.z = scene.min.z
    seat.facing = stage

for i, spotlight in enumerate(spotlights):
    if i % 2 == 0:
        spotlight.min.x = scene.min.x
    else:
        spotlight.max.x = scene.max.x
    if i < 2:
        spotlight.center.y = scene.min.y + 0.15 * scene.depth
    else:
        spotlight.center.y = scene.min.y + 0.55 * scene.depth
    spotlight.max.z = scene.max.z
    spotlight.facing = stage

plants[0].min.x = scene.min.x + 0.1
plants[0].min.y = scene.min.y + 0.1
plants[0].min.z = scene.min.z
plants[0].facing = stage
plants[1].max.x = scene.max.x - 0.1
plants[1].min.y = scene.min.y + 0.1
plants[1].min.z = scene.min.z
plants[1].facing = stage