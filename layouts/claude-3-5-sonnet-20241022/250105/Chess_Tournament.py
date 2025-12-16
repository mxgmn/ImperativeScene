set_title("Chess Tournament Hall")
set_size(width=10, depth=12, height=3)
set_floor_asset("Marble Floor", color="E8E5DE")
set_wall_asset("Painted Wall", interior=True, color="D6D1C4")

entrance = Door("Double Door", width=1.8, depth=0.1, height=2.2, color="8B4513")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Window", width=1.5, depth=0.1, height=1.5, color="87CEEB") for _ in range(4)]

# Chess tables are wider than deep to accommodate the chess board and clock
chess_tables = [Object("Chess Table", width=0.9, depth=0.7, height=0.75, support=STANDING, color="8B4513") for _ in range(12)]
chairs = [Object("Tournament Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="A0522D") for _ in range(24)]

# Judges' area
judges_table = Object("Long Table", width=2.0, depth=0.8, height=0.75, support=STANDING, color="4B0082")
judges_chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="483D8B") for _ in range(3)]

# Display and equipment
scoreboard = Object("Digital Board", width=2.0, depth=0.1, height=1.2, support=MOUNTED, color="4682B4")
trophy_case = Object("Display Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
clock_display = Object("Tournament Clock Display", width=1.5, depth=0.1, height=0.6, support=MOUNTED, color="FF4500")

# Spectator area
benches = [Object("Wooden Bench", width=2.0, depth=0.4, height=0.45, support=STANDING, color="CD853F") for _ in range(4)]
water_dispenser = Object("Water Dispenser", width=0.4, depth=0.4, height=1.2, support=STANDING, color="87CEEB")
trash_bin = Object("Trash Bin", width=0.3, depth=0.3, height=0.5, support=STANDING, color="708090")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

spacing = 0.25 * scene.width
for i, window in enumerate(windows):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) * scene.depth / 5.0
    window.min.z = 1.0
    window.facing = X_MAX

# Chess tables in a grid layout (4x3)
table_spacing_x = 0.2 * scene.width
table_spacing_y = 0.15 * scene.depth
for i, table in enumerate(chess_tables):
    row = i // 4
    col = i % 4
    table.center.x = scene.min.x + (col+1.0) * table_spacing_x
    table.center.y = scene.min.y + (row+1.0) * table_spacing_y
    table.min.z = scene.min.z
    table.facing = Y_MAX

# Two chairs per table
for i, chair in enumerate(chairs):
    table_index = i // 2
    table = chess_tables[table_index]
    set_coordinate_frame(table)
    chair.center.x = table.center.x
    if i % 2 == 0:
        chair.min.y = table.min.y - 0.1
    else:
        chair.max.y = table.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = table
set_coordinate_frame(scene)

judges_table.center.x = scene.max.x - 0.2 * scene.width
judges_table.max.y = scene.max.y
judges_table.min.z = scene.min.z
judges_table.facing = Y_MIN

set_coordinate_frame(judges_table)
for i, chair in enumerate(judges_chairs):
    chair.center.x = judges_table.min.x + (i+1.0) / 4.0 * judges_table.width
    chair.min.y = judges_table.min.y - 0.1
    chair.min.z = scene.min.z
    chair.facing = judges_table
set_coordinate_frame(scene)

scoreboard.center.x = scene.max.x - 0.2 * scene.width
scoreboard.max.y = scene.max.y
scoreboard.min.z = 1.5
scoreboard.facing = Y_MIN

trophy_case.max.x = scene.max.x
trophy_case.center.y = scene.min.y + 0.3 * scene.depth
trophy_case.min.z = scene.min.z
trophy_case.facing = X_MIN

clock_display.center.x = scene.center.x
clock_display.max.y = scene.max.y
clock_display.min.z = 2.0
clock_display.facing = Y_MIN

# Benches along the wall for spectators
for i, bench in enumerate(benches):
    bench.max.x = scene.max.x - 0.1
    bench.center.y = scene.min.y + (i+1.0) * scene.depth / 5.0
    bench.min.z = scene.min.z
    bench.facing = X_MIN

water_dispenser.min.x = scene.min.x + 0.1
water_dispenser.max.y = scene.max.y - 0.1
water_dispenser.min.z = scene.min.z
water_dispenser.facing = X_MAX

trash_bin.min.x = water_dispenser.max.x + 0.1
trash_bin.max.y = scene.max.y - 0.1
trash_bin.min.z = scene.min.z
trash_bin.facing = X_MAX