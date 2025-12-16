set_title("Railway Station Platform")
set_size(width=30, depth=8, height=4)
set_floor_asset("Concrete Platform Floor", color="9B9B9B")
set_wall_asset("Brick Wall", interior=False, color="8B7355")

# Doors leading to station building
entrance_doors = [Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB") for _ in range(3)]
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(6)]

# Main platform features
benches = [Object("Platform Bench", width=1.8, depth=0.5, height=0.45, support=STANDING, color="8B4513") for _ in range(6)]
ticket_machine = Object("Ticket Machine", width=0.8, depth=0.6, height=1.7, support=STANDING, color="4169E1")
info_board = Object("Information Board", width=3.0, depth=0.1, height=1.5, support=MOUNTED, color="1E90FF")
clock = Object("Station Clock", width=0.8, depth=0.1, height=0.8, support=MOUNTED, color="FFD700")

# Platform equipment
vending_machines = [Object("Vending Machine", width=1.0, depth=0.8, height=2.0, support=STANDING, color="FF4500") for _ in range(2)]
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.8, support=STANDING, color="2E8B57") for _ in range(4)]
platform_signs = [Object("Platform Sign", width=0.8, depth=0.1, height=0.4, support=MOUNTED, color="FF6347") for _ in range(3)]

# Safety and guidance
warning_strips = [Object("Warning Strip", width=29.0, depth=0.3, height=0.01, support=STANDING, color="FFD700")]
information_posts = [Object("Information Post", width=0.3, depth=0.3, height=2.0, support=STANDING, color="4682B4") for _ in range(4)]
route_map = Object("Route Map", width=1.5, depth=0.1, height=1.2, support=MOUNTED, color="F0E68C")

# Shelter
waiting_shelter = Object("Platform Shelter", width=4.0, depth=2.0, height=2.5, support=STANDING, color="708090")