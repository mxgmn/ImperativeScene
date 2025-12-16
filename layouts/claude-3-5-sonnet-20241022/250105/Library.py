set_title("Library")
set_size(width=15, depth=12, height=3.5)
set_floor_asset("Hardwood Floor", color="8B4513")
set_wall_asset("Painted Wall", interior=True, color="E8DCC4")

entrance = Door("Double Door", width=1.6, depth=0.1, height=2.2, color="8B4513")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="87CEEB") for _ in range(3)]

# Main bookshelves along the walls
wall_bookshelves = [Object("Tall Bookshelf", width=1.8, depth=0.4, height=2.8, support=STANDING, color="8B4513") for _ in range(8)]

# Island bookshelves in the middle
island_bookshelves = [Object("Double-sided Bookshelf", width=2.4, depth=0.8, height=1.8, support=STANDING, color="A0522D") for _ in range(3)]

# Reading areas
reading_tables = [Object("Reading Table", width=1.2, depth=0.8, height=0.75, support=STANDING, color="DEB887") for _ in range(3)]
chairs = [Object("Library Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="8B008B") for _ in range(12)]

# Librarian's area
desk = Object("Librarian Desk", width=1.8, depth=0.8, height=0.75, support=STANDING, color="CD853F")
office_chair = Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="4B0082")
computer = Object("Desktop Computer", width=0.5, depth=0.4, height=0.4, support=STANDING, color="708090")

# Reading nook
armchairs = [Object("Armchair", width=0.9, depth=0.9, height=1.0, support=STANDING, color="483D8B") for _ in range(2)]
side_table = Object("Side Table", width=0.5, depth=0.5, height=0.6, support=STANDING, color="B8860B")
reading_lamp = Object("Table Lamp", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FFD700")

# Book return cart
cart = Object("Book Cart", width=0.9, depth=0.6, height=1.0, support=STANDING, color="4682B4")

# Decorative elements
globe = Object("Globe", width=0.4, depth=0.4, height=0.6, support=STANDING, color="32CD32")
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(3)]

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.max.y = scene.max.y
    window.min.z = 1.2
    window.facing = Y_MIN

# Wall bookshelves placement
for i in range(4):  # Left wall
    wall_bookshelves[i].min.x = scene.min.x
    wall_bookshelves[i].center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    wall_bookshelves[i].min.z = scene.min.z
    wall_bookshelves[i].facing = X_MAX

for i in range(4):  # Right wall
    wall_bookshelves[i+4].max.x = scene.max.x
    wall_bookshelves[i+4].center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    wall_bookshelves[i+4].min.z = scene.min.z
    wall_bookshelves[i+4].facing = X_MIN

# Island bookshelves in the middle
for i, shelf in enumerate(island_bookshelves):
    shelf.center.x = scene.center.x
    shelf.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    shelf.min.z = scene.min.z
    shelf.facing = X_MAX

# Reading tables and chairs
for i, table in enumerate(reading_tables):
    table.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    table.center.y = scene.min.y + 0.3 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MIN
    
    # Four chairs per table
    for j in range(4):
        chair_idx = i * 4 + j
        set_coordinate_frame(table)
        chairs[chair_idx].center.x = table.min.x + (0.25 if j < 2 else 0.75) * table.width
        if j % 2 == 0:
            chairs[chair_idx].max.y = table.min.y - 0.1
        else:
            chairs[chair_idx].min.y = table.max.y + 0.1
        chairs[chair_idx].min.z = scene.min.z
        chairs[chair_idx].facing = table
set_coordinate_frame(scene)

# Librarian's area
desk.max.x = scene.max.x - 0.5
desk.max.y = scene.max.y - 0.5
desk.min.z = scene.min.z
desk.facing = Y_MIN

set_coordinate_frame(desk)
office_chair.center.x = desk.center.x
office_chair.min.y = desk.max.y + 0.1
office_chair.min.z = scene.min.z
office_chair.facing = desk

computer.center.x = desk.center.x
computer.center.y = desk.center.y
computer.min.z = desk.max.z
computer.facing = desk.facing
set_coordinate_frame(scene)

# Reading nook
param = 0.3
for i, chair in enumerate(armchairs):
    chair.min.x = scene.min.x + param
    chair.center.y = scene.max.y - (i+1.0) * chair.depth - param
    chair.min.z = scene.min.z
    chair.facing = X_MAX

side_table.min.x = scene.min.x + param
side_table.center.y = (armchairs[0].center.y + armchairs[1].center.y) / 2.0
side_table.min.z = scene.min.z
side_table.facing = X_MAX

set_coordinate_frame(side_table)
reading_lamp.center.x = side_table.center.x
reading_lamp.center.y = side_table.center.y
reading_lamp.min.z = side_table.max.z
reading_lamp.facing = side_table.facing
set_coordinate_frame(scene)

cart.min.x = entrance.max.x + 0.5
cart.min.y = scene.min.y + 0.5
cart.min.z = scene.min.z
cart.facing = X_MAX

globe.min.x = desk.min.x - 0.5
globe.max.y = desk.max.y
globe.min.z = scene.min.z
globe.facing = Y_MIN

for i, plant in enumerate(plants):
    if i == 0:
        plant.min.x = scene.min.x + 0.5
        plant.max.y = scene.max.y - 0.5
    elif i == 1:
        plant.max.x = scene.max.x - 0.5
        plant.min.y = scene.min.y + 0.5
    else:
        plant.center.x = scene.center.x
        plant.min.y = scene.min.y + 0.5
    plant.min.z = scene.min.z
    plant.facing = Y_MIN