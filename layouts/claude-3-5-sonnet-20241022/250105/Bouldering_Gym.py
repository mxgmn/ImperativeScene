set_title("Bouldering Gym")
set_size(width=15, depth=20, height=4.5)
set_floor_asset("Padded Floor", color="4A4A4A")
set_wall_asset("Concrete Wall", interior=True, color="8B8B83")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD5C5C")
windows = [Window("Window", width=2.0, depth=0.1, height=1.5, color="87CEEB") for _ in range(3)]

climbing_walls = [Object("Climbing Wall", width=5.0, depth=0.3, height=4.0, support=STANDING, color="E6B800") for _ in range(6)]
crash_pads = [Object("Crash Pad", width=2.0, depth=1.5, height=0.3, support=STANDING, color="4682B4") for _ in range(12)]

# Training area equipment
campus_board = Object("Campus Board", width=1.2, depth=0.2, height=2.5, support=MOUNTED, color="8B4513")
hangboard = Object("Hangboard", width=1.0, depth=0.2, height=0.3, support=MOUNTED, color="DEB887")
training_benches = [Object("Training Bench", width=1.2, depth=0.6, height=0.45, support=STANDING, color="708090") for _ in range(2)]

# Reception and storage
counter = Object("Reception Counter", width=2.0, depth=0.6, height=1.1, support=STANDING, color="A0522D")
shoe_rack = Object("Shoe Rack", width=1.8, depth=0.4, height=2.0, support=STANDING, color="556B2F")
lockers = Object("Locker Unit", width=2.4, depth=0.5, height=1.8, support=STANDING, color="5F9EA0")

# Seating area
benches = [Object("Bench", width=1.5, depth=0.4, height=0.45, support=STANDING, color="8FBC8F") for _ in range(3)]
water_dispenser = Object("Water Dispenser", width=0.4, depth=0.4, height=1.2, support=STANDING, color="20B2AA")

entrance.center.x = scene.min.x + 0.3 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth # 0.2
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 1.5
    window.facing = Y_MAX

# Left wall
for i in range(3):
    climbing_walls[i].min.x = scene.min.x
    climbing_walls[i].center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    climbing_walls[i].min.z = scene.min.z
    climbing_walls[i].facing = X_MAX

# Right wall
for i in range(3):
    climbing_walls[i+3].max.x = scene.max.x
    climbing_walls[i+3].center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    climbing_walls[i+3].min.z = scene.min.z
    climbing_walls[i+3].facing = X_MIN

# Place crash pads in front of climbing walls
for i, pad in enumerate(crash_pads):
    wall = climbing_walls[i // 2]
    set_coordinate_frame(wall)
    pad.center.x = wall.center.x + (0.25 if i % 2 == 0 else -0.25) * wall.width
    pad.min.y = wall.max.y + 0.1
    pad.min.z = scene.min.z
    pad.facing = wall
set_coordinate_frame(scene)

campus_board.max.x = scene.max.x - 0.2 * scene.width
campus_board.max.y = scene.max.y
campus_board.min.z = 1.0
campus_board.facing = X_MIN

hangboard.center.x = campus_board.center.x - 1.5
hangboard.max.y = scene.max.y
hangboard.min.z = 2.0
hangboard.facing = Y_MIN

for i, bench in enumerate(training_benches):
    bench.center.x = campus_board.center.x + (i-0.5) * bench.width
    bench.max.y = scene.max.y - 1.0
    bench.min.z = scene.min.z
    bench.facing = Y_MIN

counter.center.x = scene.min.x + 0.2 * scene.width
counter.min.y = scene.min.y + 0.1 * scene.depth
counter.min.z = scene.min.z
counter.facing = Y_MAX

shoe_rack.min.x = counter.max.x + 0.5
shoe_rack.min.y = scene.min.y + 0.1 * scene.depth
shoe_rack.min.z = scene.min.z
shoe_rack.facing = Y_MAX

lockers.min.x = shoe_rack.max.x + 0.5
lockers.min.y = scene.min.y + 0.1 * scene.depth
lockers.min.z = scene.min.z
lockers.facing = Y_MAX

for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + 0.2 * scene.width
    bench.center.y = scene.min.y + (i+2.0) / 5.0 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = X_MAX

water_dispenser.min.x = counter.max.x + 0.2
water_dispenser.min.y = scene.min.y + 0.3 * scene.depth
water_dispenser.min.z = scene.min.z
water_dispenser.facing = Y_MAX