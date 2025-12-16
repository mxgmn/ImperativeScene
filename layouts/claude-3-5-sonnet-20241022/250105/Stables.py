set_title("Stables")
set_size(width=12, depth=8, height=3.5)
set_floor_asset("Dirt Floor", color="8B7355")
set_wall_asset("Wooden Plank Wall", interior=True, color="8B4513")

main_door = Door("Barn Door", width=2.4, depth=0.15, height=2.8, color="A0522D")
side_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.0, depth=0.1, height=1.0, color="87CEEB") for _ in range(4)]

# Horse stalls (main feature)
stalls = [Object("Horse Stall", width=2.0, depth=3.0, height=1.6, support=STANDING, color="DEB887") for _ in range(4)]

# Feeding and storage
hay_bales = [Object("Hay Bale", width=1.2, depth=0.6, height=0.6, support=STANDING, color="F4A460") for _ in range(6)]
feed_bins = [Object("Feed Bin", width=0.6, depth=0.4, height=0.4, support=STANDING, color="CD853F") for _ in range(4)]
water_troughs = [Object("Water Trough", width=0.8, depth=0.4, height=0.4, support=STANDING, color="4682B4") for _ in range(4)]

# Equipment storage
tack_rack = Object("Tack Rack", width=2.0, depth=0.3, height=1.8, support=MOUNTED, color="8B4513")
tool_rack = Object("Tool Rack", width=1.5, depth=0.2, height=1.0, support=MOUNTED, color="A0522D")
wheelbarrow = Object("Wheelbarrow", width=0.8, depth=1.4, height=0.6, support=STANDING, color="CD5C5C")
storage_chest = Object("Storage Chest", width=1.2, depth=0.6, height=0.8, support=STANDING, color="B8860B")

# Grooming area
grooming_station = Object("Grooming Station", width=2.0, depth=1.0, height=1.0, support=STANDING, color="DAA520")

main_door.center.x = scene.min.x + 0.5 * scene.width
main_door.min.y = scene.min.y
main_door.min.z = scene.min.z
main_door.facing = Y_MAX

side_door.max.x = scene.max.x
side_door.max.y = scene.max.y - 0.2 * scene.depth
side_door.min.z = scene.min.z
side_door.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    window.max.y = scene.max.y
    window.min.z = 1.8
    window.facing = Y_MIN

# Place stalls along the right wall
for i, stall in enumerate(stalls):
    stall.max.x = scene.max.x
    stall.center.y = scene.min.y + (i+0.5) / len(stalls) * scene.depth
    stall.min.z = scene.min.z
    stall.facing = X_MIN

# Place hay bales in two rows
for i, hay in enumerate(hay_bales):
    hay.min.x = scene.min.x + 0.2
    hay.center.y = scene.min.y + (i+0.5) / len(hay_bales) * (scene.depth - 1.0)
    hay.min.z = scene.min.z
    hay.facing = X_MAX

# Place feed bins and water troughs near each stall
for i, (feed_bin, water_trough) in enumerate(zip(feed_bins, water_troughs)):
    set_coordinate_frame(stalls[i])
    feed_bin.min.x = stalls[i].min.x - feed_bin.width - 0.2
    feed_bin.center.y = stalls[i].min.y + 0.3
    feed_bin.min.z = scene.min.z
    feed_bin.facing = stalls[i].facing
    
    water_trough.min.x = stalls[i].min.x - water_trough.width - 0.2
    water_trough.center.y = stalls[i].max.y - 0.3
    water_trough.min.z = scene.min.z
    water_trough.facing = stalls[i].facing
set_coordinate_frame(scene)

tack_rack.min.x = scene.min.x
tack_rack.center.y = scene.min.y + 0.3 * scene.depth
tack_rack.min.z = 1.0
tack_rack.facing = X_MAX

tool_rack.min.x = scene.min.x
tool_rack.center.y = scene.min.y + 0.6 * scene.depth
tool_rack.min.z = 1.0
tool_rack.facing = X_MAX

wheelbarrow.center.x = scene.min.x + 0.3 * scene.width
wheelbarrow.min.y = scene.min.y + 0.1
wheelbarrow.min.z = scene.min.z
wheelbarrow.facing = Y_MAX

storage_chest.min.x = scene.min.x + 0.2
storage_chest.max.y = scene.max.y - 0.2
storage_chest.min.z = scene.min.z
storage_chest.facing = X_MAX

grooming_station.center.x = scene.min.x + 0.4 * scene.width
grooming_station.center.y = scene.max.y - 0.2 * scene.depth
grooming_station.min.z = scene.min.z
grooming_station.facing = Y_MIN