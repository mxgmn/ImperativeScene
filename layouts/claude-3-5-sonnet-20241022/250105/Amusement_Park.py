set_title("Amusement Park Section")
set_size(width=25, depth=25, height=15)
set_floor_asset("Concrete Tiles Floor", color="9B9B9B")
set_wall_asset("Park Fence", interior=False, color="4A4A4A")

entrance_gate = Door("Decorative Gate", width=3.0, depth=0.3, height=3.5, color="4169E1")

# Main attraction - a carousel
carousel_base = Object("Carousel Platform", width=8.0, depth=8.0, height=0.5, support=STANDING, color="FFD700")
carousel_center = Object("Carousel Column", width=1.0, depth=1.0, height=4.0, support=STANDING, color="B22222")
carousel_horses = [Object("Carousel Horse", width=0.8, depth=1.5, height=1.5, support=STANDING, color="FF69B4") for _ in range(8)]

# Food and refreshments
food_stands = [
    Object("Hot Dog Stand", width=2.5, depth=1.5, height=2.2, support=STANDING, color="FF4500"),
    Object("Ice Cream Cart", width=1.8, depth=1.2, height=1.8, support=STANDING, color="87CEEB"),
    Object("Popcorn Stand", width=2.0, depth=1.5, height=2.0, support=STANDING, color="FFFF00")
]

# Seating and rest areas
benches = [Object("Park Bench", width=1.5, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.8, support=STANDING, color="228B22") for _ in range(4)]

# Decorative elements
planters = [Object("Large Planter", width=1.2, depth=1.2, height=0.6, support=STANDING, color="CD853F") for _ in range(4)]
trees = [Object("Decorative Tree", width=2.0, depth=2.0, height=4.0, support=STANDING, color="228B22") for _ in range(3)]
lamp_posts = [Object("Lamp Post", width=0.3, depth=0.3, height=3.0, support=STANDING, color="FFA500") for _ in range(6)]

# Game booths
game_booths = [
    Object("Ring Toss Booth", width=3.0, depth=2.0, height=2.5, support=STANDING, color="9370DB"),
    Object("Balloon Pop Booth", width=3.0, depth=2.0, height=2.5, support=STANDING, color="FF6347")
]

# Ticket booth
ticket_booth = Object("Ticket Booth", width=2.0, depth=2.0, height=2.5, support=STANDING, color="4682B4")

entrance_gate.center.x = scene.center.x
entrance_gate.min.y = scene.min.y
entrance_gate.min.z = scene.min.z
entrance_gate.facing = Y_MAX

# Central carousel placement
carousel_base.center.x = scene.center.x
carousel_base.center.y = scene.center.y
carousel_base.min.z = scene.min.z
carousel_base.facing = Y_MAX

carousel_center.center.x = carousel_base.center.x
carousel_center.center.y = carousel_base.center.y
carousel_center.min.z = carousel_base.max.z
carousel_center.facing = carousel_base.facing

# Place carousel horses in a circle
radius = 3.0
for i, horse in enumerate(carousel_horses):
    angle = i * (2.0 * 3.14159 / len(carousel_horses))
    horse.center.x = carousel_base.center.x + radius * math.cos(angle)
    horse.center.y = carousel_base.center.y + radius * math.sin(angle)
    horse.min.z = carousel_base.max.z
    horse.facing = carousel_center

# Food stands placement
spacing = 0.2 * scene.width
for i, stand in enumerate(food_stands):
    stand.center.x = scene.min.x + (i + 1.0) * spacing
    stand.max.y = scene.max.y - 0.1 * scene.depth
    stand.min.z = scene.min.z
    stand.facing = Y_MIN

# Benches placement
for i, bench in enumerate(benches):
    if i < 3:
        bench.min.x = scene.min.x + (i + 1.0) * scene.width / 4.0
        bench.min.y = scene.min.y + 0.1 * scene.depth
    else:
        bench.min.x = scene.min.x + (i - 2.0) * scene.width / 4.0
        bench.max.y = scene.max.y - 0.2 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = carousel_base

# Trash bins near benches
for i, bin in enumerate(trash_bins):
    if i < 2:
        bin.min.x = benches[i].max.x + 0.1
        bin.center.y = benches[i].center.y
    else:
        bin.min.x = benches[i+2].max.x + 0.1
        bin.center.y = benches[i+2].center.y
    bin.min.z = scene.min.z
    bin.facing = benches[0].facing

# Planters in corners
corner_offsets = [(1.0, 1.0), (1.0, -1.0), (-1.0, 1.0), (-1.0, -1.0)]
for planter, (x_offset, y_offset) in zip(planters, corner_offsets):
    planter.center.x = scene.center.x + x_offset * 0.4 * scene.width
    planter.center.y = scene.center.y + y_offset * 0.4 * scene.depth
    planter.min.z = scene.min.z
    planter.facing = carousel_base

# Trees placement
for i, tree in enumerate(trees):
    angle = i * (2.0 * 3.14159 / len(trees))
    radius = 0.35 * scene.width
    tree.center.x = scene.center.x + radius * math.cos(angle)
    tree.center.y = scene.center.y + radius * math.sin(angle)
    tree.min.z = scene.min.z
    tree.facing = carousel_base

# Lamp posts around the perimeter
for i, lamp in enumerate(lamp_posts):
    if i < 3:
        lamp.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
        lamp.min.y = scene.min.y + 0.05 * scene.depth
    else:
        lamp.center.x = scene.min.x + (i - 2.0) * scene.width / 4.0
        lamp.max.y = scene.max.y - 0.05 * scene.depth
    lamp.min.z = scene.min.z
    lamp.facing = carousel_base

# Game booths placement
for i, booth in enumerate(game_booths):
    booth.min.x = scene.min.x + (i + 1.0) * 0.2 * scene.width
    booth.min.y = scene.min.y + 0.15 * scene.depth
    booth.min.z = scene.min.z
    booth.facing = Y_MAX

# Ticket booth near entrance
ticket_booth.center.x = entrance_gate.center.x + 0.15 * scene.width
ticket_booth.min.y = entrance_gate.min.y + 0.1 * scene.depth
ticket_booth.min.z = scene.min.z
ticket_booth.facing = entrance_gate