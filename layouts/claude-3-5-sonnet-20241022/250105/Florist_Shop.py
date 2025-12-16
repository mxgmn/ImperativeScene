set_title("Florist Shop")
set_size(width=8, depth=6, height=3)
set_floor_asset("Wooden Floor", color="9B8579")
set_wall_asset("Painted Wall", interior=True, color="E6E6FA")

entrance_door = Door("Glass Door", width=1.0, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="8B4513")
window = Window("Display Window", width=3.0, depth=0.1, height=2.0, color="B0E0E6")

# Main display and storage furniture
counter = Object("Shop Counter", width=2.0, depth=0.6, height=1.0, support=STANDING, color="E9967A")
register = Object("Cash Register", width=0.3, depth=0.3, height=0.25, support=STANDING, color="708090")
display_shelves = [Object("Display Shelf", width=1.8, depth=0.4, height=1.8, support=STANDING, color="DEB887") for _ in range(3)]
window_display = Object("Display Table", width=2.8, depth=0.6, height=0.8, support=STANDING, color="B8860B")

# Plants and flowers (represented as solid objects)
potted_plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=0.8, support=STANDING, color="228B22") for _ in range(6)]
flower_buckets = [Object("Flower Bucket", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FF69B4") for _ in range(8)]
large_plants = [Object("Large Plant", width=0.6, depth=0.6, height=1.6, support=STANDING, color="006400") for _ in range(2)]

# Storage and supplies
storage_cabinet = Object("Storage Cabinet", width=1.2, depth=0.5, height=1.8, support=STANDING, color="8FBC8F")
work_table = Object("Work Table", width=1.5, depth=0.8, height=0.9, support=STANDING, color="CD853F")
supply_shelf = Object("Wall Shelf", width=1.6, depth=0.3, height=0.05, support=MOUNTED, color="A0522D")
vase_display = [Object("Decorative Vase", width=0.2, depth=0.2, height=0.3, support=STANDING, color="4682B4") for _ in range(5)]

entrance_door.center.x = scene.min.x + 0.3 * scene.width
entrance_door.min.y = scene.min.y
entrance_door.min.z = scene.min.z
entrance_door.facing = Y_MAX

back_door.max.x = scene.max.x - 0.2 * scene.width
back_door.max.y = scene.max.y
back_door.min.z = scene.min.z
back_door.facing = Y_MIN

window.center.x = scene.min.x + 0.6 * scene.width
window.min.y = scene.min.y
window.min.z = 0.8
window.facing = Y_MAX

counter.max.x = scene.max.x - 0.1
counter.center.y = scene.center.y
counter.min.z = scene.min.z
counter.facing = X_MIN

set_coordinate_frame(counter)
register.center.x = counter.center.x
register.center.y = counter.center.y
register.min.z = counter.max.z
register.facing = counter.facing
set_coordinate_frame(scene)

window_display.center.x = window.center.x
window_display.min.y = window.min.y + 0.2
window_display.min.z = scene.min.z
window_display.facing = Y_MAX

for i, shelf in enumerate(display_shelves):
    shelf.min.x = scene.min.x + i * (shelf.width + 0.2)
    shelf.max.y = scene.max.y
    shelf.min.z = scene.min.z
    shelf.facing = Y_MIN

storage_cabinet.max.x = scene.max.x
storage_cabinet.max.y = scene.max.y
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MIN

work_table.max.x = scene.max.x - 0.2
work_table.min.y = scene.min.y + 0.2
work_table.min.z = scene.min.z
work_table.facing = Y_MAX

supply_shelf.max.x = scene.max.x
supply_shelf.center.y = scene.center.y
supply_shelf.min.z = 1.8
supply_shelf.facing = X_MIN

set_coordinate_frame(supply_shelf)
for i, vase in enumerate(vase_display):
    vase.center.x = supply_shelf.min.x + (i+0.5) / 5.0 * supply_shelf.width
    vase.center.y = supply_shelf.center.y
    vase.min.z = supply_shelf.max.z
    vase.facing = supply_shelf.facing
set_coordinate_frame(scene)

set_coordinate_frame(window_display)
for i, plant in enumerate(potted_plants[:3]):
    plant.center.x = window_display.min.x + (i+1.0) / 4.0 * window_display.width
    plant.center.y = window_display.center.y
    plant.min.z = window_display.max.z
    plant.facing = window_display.facing
set_coordinate_frame(scene)

for i, plant in enumerate(potted_plants[3:]):
    plant.center.x = display_shelves[i].center.x
    plant.min.y = display_shelves[i].min.y + 0.1
    plant.min.z = display_shelves[i].max.z - 0.4
    plant.facing = display_shelves[i].facing

for i, bucket in enumerate(flower_buckets):
    bucket.center.x = scene.min.x + (i+1.0) / 9.0 * scene.width
    bucket.center.y = scene.center.y
    bucket.min.z = scene.min.z
    bucket.facing = Y_MAX

large_plants[0].min.x = scene.min.x + 0.1
large_plants[0].min.y = scene.min.y + 0.1
large_plants[0].min.z = scene.min.z
large_plants[0].facing = X_MAX

large_plants[1].max.x = scene.max.x - 0.1
large_plants[1].min.y = scene.min.y + 0.1
large_plants[1].min.z = scene.min.z
large_plants[1].facing = X_MIN