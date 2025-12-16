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