set_title("College Gym")
set_size(width=20, depth=15, height=4)
set_floor_asset("Rubber Floor", color="2F4F4F")
set_wall_asset("Painted Wall", interior=True, color="E5E5E5")

entrance = Door("Double Door", width=1.8, depth=0.1, height=2.2, color="4682B4")
emergency_exit = Door("Emergency Door", width=1.0, depth=0.1, height=2.2, color="B22222")
windows = [Window("Window", width=1.5, depth=0.1, height=1.2, color="87CEEB") for _ in range(4)]

# Main exercise equipment
treadmills = [Object("Treadmill", width=0.9, depth=1.8, height=1.4, support=STANDING, color="2E8B57") for _ in range(5)]
ellipticals = [Object("Elliptical", width=0.8, depth=1.6, height=1.7, support=STANDING, color="4169E1") for _ in range(3)]
exercise_bikes = [Object("Exercise Bike", width=0.6, depth=1.2, height=1.2, support=STANDING, color="FF4500") for _ in range(4)]

# Weight area
weight_racks = [Object("Weight Rack", width=1.8, depth=0.6, height=1.8, support=STANDING, color="8B4513") for _ in range(2)]
bench_press = [Object("Weight Bench", width=0.6, depth=1.5, height=0.5, support=STANDING, color="CD853F") for _ in range(3)]
dumbell_rack = Object("Dumbbell Rack", width=2.4, depth=0.5, height=0.9, support=STANDING, color="A0522D")

# Functional training area
squat_racks = [Object("Squat Rack", width=1.2, depth=1.2, height=2.2, support=STANDING, color="696969") for _ in range(2)]
mirrors = [Object("Wall Mirror", width=2.5, depth=0.05, height=2.0, support=MOUNTED, color="B0C4DE") for _ in range(4)]

# Accessories and furniture
water_fountain = Object("Water Fountain", width=0.5, depth=0.5, height=1.0, support=STANDING, color="4682B4")
benches = [Object("Bench", width=1.2, depth=0.4, height=0.45, support=STANDING, color="8B4513") for _ in range(3)]
lockers = [Object("Locker Unit", width=1.8, depth=0.5, height=1.8, support=STANDING, color="20B2AA") for _ in range(2)]

# Notice board and decorative elements
notice_board = Object("Notice Board", width=1.2, depth=0.05, height=0.9, support=MOUNTED, color="CD853F")
college_banner = Object("Banner", width=2.0, depth=0.02, height=1.0, support=MOUNTED, color="4B0082")

entrance.center.x = scene.min.x + 0.3 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.center.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    window.max.y = scene.max.y
    window.min.z = 2.0
    window.facing = Y_MIN

# Cardio section near entrance
spacing = 0.4
for i, treadmill in enumerate(treadmills):
    treadmill.center.x = scene.min.x + (i+1.0) / 6.0 * scene.width
    treadmill.center.y = scene.min.y + 0.2 * scene.depth
    treadmill.min.z = scene.min.z
    treadmill.facing = Y_MAX

for i, bike in enumerate(exercise_bikes):
    bike.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    bike.center.y = scene.min.y + 0.4 * scene.depth
    bike.min.z = scene.min.z
    bike.facing = Y_MAX

for i, elliptical in enumerate(ellipticals):
    elliptical.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    elliptical.center.y = scene.min.y + 0.6 * scene.depth
    elliptical.min.z = scene.min.z
    elliptical.facing = Y_MAX

# Weight area
for i, rack in enumerate(weight_racks):
    rack.max.x = scene.max.x - i * (rack.width + spacing)
    rack.center.y = scene.min.y + 0.3 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = X_MIN

for i, bench in enumerate(bench_press):
    bench.max.x = scene.max.x - 0.2 * scene.width
    bench.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = X_MIN

dumbell_rack.max.x = scene.max.x
dumbell_rack.center.y = scene.max.y - 0.3 * scene.depth
dumbell_rack.min.z = scene.min.z
dumbell_rack.facing = X_MIN

# Functional area
for i, rack in enumerate(squat_racks):
    rack.center.x = scene.center.x + (i-0.5) * (rack.width + spacing)
    rack.max.y = scene.max.y - 0.1 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = Y_MIN

for i, mirror in enumerate(mirrors):
    mirror.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    mirror.min.y = scene.min.y
    mirror.min.z = 0.5
    mirror.facing = Y_MAX

# Accessories
water_fountain.min.x = scene.min.x
water_fountain.center.y = scene.center.y
water_fountain.min.z = scene.min.z
water_fountain.facing = X_MAX

for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    bench.min.y = scene.min.y + 0.8 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

for i, locker in enumerate(lockers):
    locker.min.x = scene.min.x
    locker.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    locker.min.z = scene.min.z
    locker.facing = X_MAX

notice_board.max.x = scene.max.x - 0.1 * scene.width
notice_board.min.y = scene.min.y
notice_board.min.z = 1.5
notice_board.facing = Y_MAX

college_banner.center.x = scene.center.x
college_banner.max.y = scene.max.y
college_banner.min.z = 2.5
college_banner.facing = Y_MIN