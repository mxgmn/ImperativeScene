set_title("Greenhouse")
set_size(width=8, depth=12, height=3.5)
set_floor_asset("Stone Tile Floor", color="8B8682")
set_wall_asset("Glass Wall", interior=True, color="B5D1D7")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="ADD8E6")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.0, color="B0E0E6") for _ in range(6)]

# Main planting areas
planter_boxes = [Object("Planter Box", width=1.8, depth=0.8, height=0.6, support=STANDING, color="8B4513") for _ in range(6)]

# Plants of various sizes
large_plants = [Object("Indoor Plant", width=0.8, depth=0.8, height=2.0, support=STANDING, color="228B22") for _ in range(4)]
medium_plants = [Object("Potted Plant", width=0.5, depth=0.5, height=1.2, support=STANDING, color="32CD32") for _ in range(6)]
small_plants = [Object("Small Plant", width=0.3, depth=0.3, height=0.6, support=STANDING, color="90EE90") for _ in range(12)]

# Furniture and equipment
potting_bench = Object("Potting Bench", width=2.0, depth=0.6, height=0.9, support=STANDING, color="8B7355")
storage_cabinet = Object("Storage Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
watering_station = Object("Sink", width=0.8, depth=0.6, height=0.9, support=STANDING, color="B8B8B8")
tool_rack = Object("Tool Rack", width=1.0, depth=0.1, height=1.2, support=MOUNTED, color="CD853F")
shelf_unit = Object("Wire Shelf Unit", width=1.8, depth=0.4, height=1.8, support=STANDING, color="808080")

# Decorative elements
wind_chime = Object("Wind Chime", width=0.2, depth=0.2, height=0.4, support=MOUNTED, color="E6E6FA")
garden_gnome = Object("Garden Gnome", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FF6347")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

# Windows on side walls
for i, window in enumerate(windows[:3]):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    window.min.z = 0.8
    window.facing = X_MAX

for i, window in enumerate(windows[3:]):
    window.max.x = scene.max.x
    window.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    window.min.z = 0.8
    window.facing = X_MIN

# Planter boxes in two rows
for i, box in enumerate(planter_boxes[:3]):
    box.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    box.center.y = scene.min.y + 0.3 * scene.depth
    box.min.z = scene.min.z
    box.facing = Y_MAX

for i, box in enumerate(planter_boxes[3:]):
    box.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    box.center.y = scene.min.y + 0.7 * scene.depth
    box.min.z = scene.min.z
    box.facing = Y_MIN

# Large plants in corners
param = 0.15
for i, plant in enumerate(large_plants):
    if i == 0:
        plant.min.x = scene.min.x + param * scene.width
        plant.min.y = scene.min.y + param * scene.depth
    elif i == 1:
        plant.max.x = scene.max.x - param * scene.width
        plant.min.y = scene.min.y + param * scene.depth
    elif i == 2:
        plant.min.x = scene.min.x + param * scene.width
        plant.max.y = scene.max.y - param * scene.depth
    else:
        plant.max.x = scene.max.x - param * scene.width
        plant.max.y = scene.max.y - param * scene.depth
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

# Medium plants along walls
for i, plant in enumerate(medium_plants[:3]):
    plant.min.x = scene.min.x + 0.1
    plant.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    plant.min.z = scene.min.z
    plant.facing = X_MAX

for i, plant in enumerate(medium_plants[3:]):
    plant.max.x = scene.max.x - 0.1
    plant.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    plant.min.z = scene.min.z
    plant.facing = X_MIN

# Small plants on planter boxes
for i, plant in enumerate(small_plants):
    box = planter_boxes[i // 2]
    set_coordinate_frame(box)
    plant.center.x = box.min.x + ((i % 2) + 0.5) / 2.0 * box.width
    plant.center.y = box.center.y
    plant.min.z = box.max.z
    plant.facing = box.facing
set_coordinate_frame(scene)

potting_bench.max.x = scene.max.x - 0.2
potting_bench.max.y = scene.max.y - 0.2
potting_bench.min.z = scene.min.z
potting_bench.facing = X_MIN

storage_cabinet.min.x = scene.min.x + 0.2
storage_cabinet.max.y = scene.max.y - 0.2
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MAX

watering_station.max.x = scene.max.x - 0.2
watering_station.min.y = scene.min.y + 0.2
watering_station.min.z = scene.min.z
watering_station.facing = Y_MAX

set_coordinate_frame(storage_cabinet)
tool_rack.center.x = storage_cabinet.center.x
tool_rack.min.y = storage_cabinet.min.y
tool_rack.min.z = storage_cabinet.max.z + 0.1
tool_rack.facing = storage_cabinet.facing
set_coordinate_frame(scene)

shelf_unit.center.x = scene.center.x
shelf_unit.max.y = scene.max.y - 0.2
shelf_unit.min.z = scene.min.z
shelf_unit.facing = Y_MIN

wind_chime.center.x = entrance.center.x
wind_chime.min.y = entrance.min.y + 0.1
wind_chime.max.z = scene.max.z - 0.1
wind_chime.facing = Y_MAX

garden_gnome.min.x = scene.min.x + 0.3
garden_gnome.min.y = scene.min.y + 0.3
garden_gnome.min.z = scene.min.z
garden_gnome.facing = Y_MAX