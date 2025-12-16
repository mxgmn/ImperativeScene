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