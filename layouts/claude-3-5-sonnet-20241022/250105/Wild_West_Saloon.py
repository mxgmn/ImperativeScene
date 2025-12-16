set_title("Wild West Saloon")
set_size(width=12, depth=8, height=3)
set_floor_asset("Wooden Planks Floor", color="8B4513")
set_wall_asset("Wooden Wall", interior=True, color="A0522D")

entrance = Door("Saloon Double Door", width=1.6, depth=0.1, height=2.0, color="CD853F")
back_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.2, depth=0.1, height=1.2, color="F4A460") for _ in range(3)]

# Main bar setup
bar_counter = Object("Bar Counter", width=5.0, depth=0.6, height=1.1, support=STANDING, color="DEB887")
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.8, support=STANDING, color="B8860B") for _ in range(6)]
bar_shelf = Object("Bar Back Shelf", width=4.8, depth=0.3, height=2.0, support=STANDING, color="8B4513")
barrels = [Object("Wooden Barrel", width=0.5, depth=0.5, height=0.8, support=STANDING, color="DAA520") for _ in range(4)]

# Seating areas
tables = [Object("Round Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="CD853F") for _ in range(4)]
chairs = [Object("Wooden Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="D2691E") for _ in range(16)]

# Gaming area
poker_table = Object("Poker Table", width=1.2, depth=1.2, height=0.75, support=STANDING, color="006400")
poker_chairs = [Object("Wooden Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]

# Decorative elements
piano = Object("Upright Piano", width=1.4, depth=0.6, height=1.3, support=STANDING, color="800000")
wanted_posters = [Object("Wanted Poster", width=0.3, depth=0.02, height=0.4, support=MOUNTED, color="F5DEB3") for _ in range(3)]
deer_head = Object("Mounted Deer Head", width=0.8, depth=0.4, height=0.9, support=MOUNTED, color="B8860B")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

back_door.max.x = scene.max.x - 0.2 * scene.width
back_door.max.y = scene.max.y
back_door.min.z = scene.min.z
back_door.facing = Y_MIN

window_spacing = 0.25
for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / (len(windows)+1.0) * scene.width
    window.max.y = scene.max.y
    window.min.z = 1.0
    window.facing = Y_MIN

bar_counter.max.x = scene.max.x - 0.2
bar_counter.max.y = scene.max.y - 0.3
bar_counter.min.z = scene.min.z
bar_counter.facing = Y_MIN

set_coordinate_frame(bar_counter)
for i, stool in enumerate(bar_stools):
    stool.center.x = bar_counter.min.x + (i+1.0) / 7.0 * bar_counter.width
    stool.min.y = bar_counter.min.y - 0.3
    stool.min.z = scene.min.z
    stool.facing = bar_counter

bar_shelf.center.x = bar_counter.center.x
bar_shelf.max.y = bar_counter.max.y
bar_shelf.min.z = scene.min.z
bar_shelf.facing = bar_counter.facing

for i, barrel in enumerate(barrels):
    if i < 2:
        barrel.min.x = bar_counter.max.x + 0.1
        barrel.center.y = bar_counter.max.y - (i+0.5) * barrel.depth
    else:
        barrel.max.x = bar_counter.min.x - 0.1
        barrel.center.y = bar_counter.max.y - (i-1.5) * barrel.depth
    barrel.min.z = scene.min.z
    barrel.facing = bar_counter.facing
set_coordinate_frame(scene)

table_spacing = 0.25
for i, table in enumerate(tables):
    table.center.x = scene.min.x + (i+1.0) / (len(tables)+1.0) * (scene.width * 0.6)
    table.center.y = scene.min.y + 0.4 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MAX

    # Place 4 chairs around each table
    for j in range(4):
        chair_idx = i * 4 + j
        set_coordinate_frame(table)
        chairs[chair_idx].center.x = table.center.x + (0.5 if j % 2 == 0 else -0.5) * table.width
        chairs[chair_idx].center.y = table.center.y + (0.5 if j < 2 else -0.5) * table.depth
        chairs[chair_idx].min.z = scene.min.z
        chairs[chair_idx].facing = table
set_coordinate_frame(scene)

poker_table.center.x = scene.min.x + 0.25 * scene.width
poker_table.center.y = scene.max.y - 0.3 * scene.depth
poker_table.min.z = scene.min.z
poker_table.facing = Y_MIN

for i, chair in enumerate(poker_chairs):
    angle = i * (360.0 / len(poker_chairs))
    chair.center.x = poker_table.center.x + 0.7 * math.cos(math.radians(angle))
    chair.center.y = poker_table.center.y + 0.7 * math.sin(math.radians(angle))
    chair.min.z = scene.min.z
    chair.facing = poker_table

piano.min.x = scene.min.x + 0.1
piano.max.y = scene.max.y - 0.1
piano.min.z = scene.min.z
piano.facing = X_MAX

for i, poster in enumerate(wanted_posters):
    poster.center.x = scene.min.x + (i+1.0) / (len(wanted_posters)+1.0) * scene.width
    poster.min.y = scene.min.y + 0.1
    poster.min.z = 1.5
    poster.facing = Y_MAX

deer_head.center.x = scene.min.x + 0.5 * scene.width
deer_head.max.y = scene.max.y
deer_head.min.z = 1.8
deer_head.facing = Y_MIN