set_title("Spacious Family Kitchen")
set_size(width=10, depth=8, height=3)
set_floor_asset("Tile Floor", color="B5B5B5")
set_wall_asset("Painted Wall", interior=True, color="E6E6FA")

# Doors and windows
main_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.1, color="8B4513")
patio_door = Door("Glass Door", width=1.8, depth=0.1, height=2.1, color="87CEEB")
windows = [Window("Window", width=1.2, depth=0.1, height=1.2, color="ADD8E6") for _ in range(3)]

# Seating
dining_table = Object("Large Dining Table", width=4.8, depth=1.5, height=0.75, support=STANDING, color="CD853F")
chairs = [Object("Dining Chair", width=0.45, depth=0.45, height=0.95, support=STANDING, color="B8860B") for _ in range(12)]
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.65, support=STANDING, color="B8860B") for _ in range(4)]

# Major appliances and fixtures
refrigerator = Object("Double Door Refrigerator", width=1.2, depth=0.8, height=2.0, support=STANDING, color="E0E0E0")
stove = Object("Industrial Stove", width=1.2, depth=0.7, height=0.9, support=STANDING, color="484848")
dishwasher = Object("Dishwasher", width=0.6, depth=0.6, height=0.85, support=STANDING, color="C0C0C0")
sink = Object("Double Sink", width=0.9, depth=0.6, height=0.9, support=STANDING, color="CFD7D9")

# Storage and counters
island = Object("Kitchen Island", width=2.4, depth=1.2, height=0.9, support=STANDING, color="8B4513")
cabinets = [Object("Cabinet", width=0.6, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]
wall_cabinets = [Object("Wall Cabinet", width=0.6, depth=0.3, height=0.7, support=MOUNTED, color="8B4513") for _ in range(4)]
pantry = Object("Pantry Cabinet", width=1.2, depth=0.6, height=2.0, support=STANDING, color="8B4513")

# Appliances
microwave = Object("Microwave", width=0.6, depth=0.4, height=0.4, support=STANDING, color="696969")
coffee_maker = Object("Coffee Maker", width=0.3, depth=0.25, height=0.35, support=STANDING, color="8B0000")
toaster = Object("Toaster", width=0.3, depth=0.2, height=0.2, support=STANDING, color="CD853F")

# Storage and organization
spice_rack = Object("Spice Rack", width=0.6, depth=0.1, height=0.4, support=MOUNTED, color="DEB887")
pot_rack = Object("Pot Rack", width=1.2, depth=0.3, height=0.02, support=MOUNTED, color="B8860B")

main_door.max.x = scene.max.x
main_door.max.y = scene.max.y - 0.2 * scene.depth
main_door.min.z = scene.min.z
main_door.facing = X_MIN

patio_door.center.x = scene.min.x + 0.5 * scene.width
patio_door.min.y = scene.min.y
patio_door.min.z = scene.min.z
patio_door.facing = Y_MAX

window_spacing = 0.25
for i, window in enumerate(windows):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) * scene.depth / 4.0
    window.min.z = 1.0
    window.facing = X_MAX

dining_table.center.x = scene.min.x + 0.35 * scene.width
dining_table.center.y = scene.center.y
dining_table.min.z = scene.min.z
dining_table.facing = Y_MAX

set_coordinate_frame(dining_table)
for i, chair in enumerate(chairs):
    side = i // 6
    pos = i % 6
    if side == 0:
        chair.min.y = dining_table.min.y - 0.1
    else:
        chair.max.y = dining_table.max.y + 0.1
    chair.center.x = dining_table.min.x + (pos + 0.5) * dining_table.width / 6.0
    chair.min.z = scene.min.z
    chair.facing = dining_table
set_coordinate_frame(scene)

island.center.x = scene.min.x + 0.7 * scene.width
island.center.y = scene.center.y
island.min.z = scene.min.z
island.facing = Y_MAX

set_coordinate_frame(island)
for i, stool in enumerate(bar_stools):
    stool.center.x = island.min.x + (i+1.0) * island.width / 5.0
    stool.min.y = island.min.y - 0.1
    stool.min.z = scene.min.z
    stool.facing = island
set_coordinate_frame(scene)

refrigerator.max.x = scene.max.x
refrigerator.min.y = scene.min.y + 0.1
refrigerator.min.z = scene.min.z
refrigerator.facing = X_MIN

stove.max.x = scene.max.x
stove.center.y = scene.center.y
stove.min.z = scene.min.z
stove.facing = X_MIN

sink.max.x = scene.max.x
sink.max.y = scene.max.y - 0.1
sink.min.z = scene.min.z
sink.facing = X_MIN

dishwasher.max.x = scene.max.x
dishwasher.max.y = sink.min.y - 0.1
dishwasher.min.z = scene.min.z
dishwasher.facing = X_MIN

cabinet_spacing = 0.05
for i, cabinet in enumerate(cabinets):
    cabinet.max.x = scene.max.x
    cabinet.center.y = scene.min.y + (i+1.0) * scene.depth / 7.0
    cabinet.min.z = scene.min.z
    cabinet.facing = X_MIN

for i, wcabinet in enumerate(wall_cabinets):
    wcabinet.max.x = scene.max.x
    wcabinet.center.y = scene.min.y + (i+1.0) * scene.depth / 5.0
    wcabinet.min.z = 1.8
    wcabinet.facing = X_MIN

pantry.min.x = scene.min.x
pantry.max.y = scene.max.y
pantry.min.z = scene.min.z
pantry.facing = X_MAX

set_coordinate_frame(island)
microwave.center.x = island.center.x
microwave.center.y = island.center.y
microwave.min.z = island.max.z
microwave.facing = island.facing

coffee_maker.min.x = island.min.x + 0.1
coffee_maker.min.y = island.min.y + 0.1
coffee_maker.min.z = island.max.z
coffee_maker.facing = island.facing

toaster.max.x = island.max.x - 0.1
toaster.max.y = island.max.y - 0.1
toaster.min.z = island.max.z
toaster.facing = island.facing
set_coordinate_frame(scene)

spice_rack.max.x = scene.max.x
spice_rack.center.y = stove.center.y
spice_rack.min.z = 1.2
spice_rack.facing = X_MIN

pot_rack.center.x = island.center.x
pot_rack.center.y = island.center.y
pot_rack.max.z = scene.max.z - 0.3
pot_rack.facing = Y_MAX