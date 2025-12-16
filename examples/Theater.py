set_title("Theater")
set_size(width=10, depth=12, height=4)
set_floor_asset("Carpet Floor")
set_wall_asset("Fabric Panels Wall", interior=True)

main_entrance = Door("Entrance Double Door", width=2.0, depth=0.1, height=2.0)
backdoor = Door("Wooden Door", width=0.8, depth=0.1, height=2.0)
stage = Object("Theater Stage", width=8, depth=4, height=0.5, support=STANDING, dynamic=False)
piano = Object("Upright Piano", width=1.5, depth=0.6, height=1.2, support=STANDING, dynamic=False)
decoration = Object("Theatrical Decoration of a Victorian Mansion", width=stage.width, depth=0.2, height = scene.height - stage.height, support=STANDING, dynamic=False)
seats = [Object("Seat", width=0.5, depth=0.4, height=0.8, support=STANDING, dynamic=False) for _ in range(5 * 8)]
spotlights = [Object("Spotlight", 0.2, 0.2, 0.2, support=MOUNTED, dynamic=False) for _ in range(4)]
plants = [Object("Potted Plant", 0.3, 0.3, height=0.5, support=STANDING, dynamic=True) for _ in range(2)]

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

for i, plant in enumerate(plants):
    if i % 2 == 0:
        plant.min.x = scene.min.x + 0.1
    else:
        plant.max.x = scene.max.x - 0.1
    plant.min.y = scene.min.y + 0.1
    plant.min.z = scene.min.z
    plant.facing = stage