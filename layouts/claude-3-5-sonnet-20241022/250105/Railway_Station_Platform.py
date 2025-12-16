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

# Place doors and windows along the back wall
for i, door in enumerate(entrance_doors):
    door.max.y = scene.max.y
    door.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
    door.min.z = scene.min.z
    door.facing = Y_MIN

for i, window in enumerate(windows):
    window.max.y = scene.max.y
    window.center.x = scene.min.x + (i + 1.0) * scene.width / 7.0
    window.min.z = 1.0
    window.facing = Y_MIN

# Place warning strip near platform edge
warning_strips[0].center.x = scene.center.x
warning_strips[0].min.y = scene.min.y + 0.5
warning_strips[0].min.z = scene.min.z
warning_strips[0].facing = Y_MAX

# Place benches with regular spacing
spacing = scene.width / 7.0
for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i + 1.0) * spacing
    bench.center.y = scene.max.y - 2.0
    bench.min.z = scene.min.z
    bench.facing = Y_MIN

# Place ticket machine and info board
ticket_machine.min.x = scene.min.x + 0.2 * scene.width
ticket_machine.max.y = scene.max.y
ticket_machine.min.z = scene.min.z
ticket_machine.facing = Y_MIN

info_board.center.x = scene.center.x
info_board.max.y = scene.max.y
info_board.min.z = 1.5
info_board.facing = Y_MIN

# Place clock
clock.center.x = scene.center.x
clock.max.y = scene.max.y
clock.min.z = 2.5
clock.facing = Y_MIN

# Place vending machines
for i, machine in enumerate(vending_machines):
    machine.center.x = scene.min.x + (i + 2.0) * scene.width / 3.0
    machine.max.y = scene.max.y
    machine.min.z = scene.min.z
    machine.facing = Y_MIN

# Place trash bins with regular spacing
for i, bin in enumerate(trash_bins):
    bin.center.x = scene.min.x + (i + 1.0) * scene.width / 5.0
    bin.max.y = scene.max.y - 1.0
    bin.min.z = scene.min.z
    bin.facing = Y_MIN

# Place platform signs
for i, sign in enumerate(platform_signs):
    sign.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
    sign.max.y = scene.max.y
    sign.min.z = 2.2
    sign.facing = Y_MIN

# Place information posts
for i, post in enumerate(information_posts):
    post.center.x = scene.min.x + (i + 1.0) * scene.width / 5.0
    post.min.y = scene.min.y + 1.0
    post.min.z = scene.min.z
    post.facing = Y_MAX

# Place route map
route_map.max.x = scene.max.x - 0.2 * scene.width
route_map.max.y = scene.max.y
route_map.min.z = 1.2
route_map.facing = Y_MIN

# Place waiting shelter
waiting_shelter.center.x = scene.center.x
waiting_shelter.center.y = scene.max.y - 2.5
waiting_shelter.min.z = scene.min.z
waiting_shelter.facing = Y_MIN