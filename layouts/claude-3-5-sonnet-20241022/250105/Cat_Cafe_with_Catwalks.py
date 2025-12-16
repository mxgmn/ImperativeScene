set_title("Cat Cafe with Catwalks")
set_size(width=8, depth=10, height=3)
set_floor_asset("Wooden Floor", color="BC8F5F")
set_wall_asset("Painted Wall", interior=True, color="FFF0E6")

entrance = Door("Glass Door", width=1.0, depth=0.1, height=2.2, color="87CEEB")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="ADD8E6") for _ in range(3)]

# Cat-specific furniture
wall_shelves = [Object("Cat Wall Shelf", width=1.2, depth=0.4, height=0.15, support=MOUNTED, color="8B4513") for _ in range(4)]
catwalks = [Object("Catwalk Bridge", width=1.8, depth=0.4, height=0.1, support=MOUNTED, color="8B7355") for _ in range(2)]
cat_trees = [Object("Cat Tree", width=0.8, depth=0.8, height=2.0, support=STANDING, color="E6B800") for _ in range(3)]
cat_beds = [Object("Cat Bed", width=0.5, depth=0.5, height=0.2, support=STANDING, color="FF69B4") for _ in range(4)]
scratching_posts = [Object("Scratching Post", width=0.4, depth=0.4, height=1.0, support=STANDING, color="D2B48C") for _ in range(2)]

# Cafe furniture
tables = [Object("Round Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="A0522D") for _ in range(4)]
chairs = [Object("Cushioned Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="FF8C69") for _ in range(8)]
counter = Object("Service Counter", width=2.0, depth=0.6, height=1.1, support=STANDING, color="DEB887")
display_case = Object("Pastry Display", width=1.2, depth=0.5, height=1.4, support=STANDING, color="F4A460")

# Decor
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=0.8, support=STANDING, color="228B22") for _ in range(3)]
cat_art = [Object("Cat Painting", width=0.6, depth=0.05, height=0.8, support=MOUNTED, color="FF7F50") for _ in range(2)]
menu_board = Object("Menu Board", width=1.0, depth=0.05, height=0.8, support=MOUNTED, color="4682B4")

entrance.max.x = scene.max.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

counter.min.x = scene.min.x + 0.1
counter.max.y = scene.max.y
counter.min.z = scene.min.z
counter.facing = Y_MIN

set_coordinate_frame(counter)
display_case.min.x = counter.max.x + 0.2
display_case.center.y = counter.center.y
display_case.min.z = scene.min.z
display_case.facing = counter.facing
menu_board.center.x = counter.center.x
menu_board.min.y = counter.min.y
menu_board.min.z = counter.max.z + 0.2
menu_board.facing = counter.facing
set_coordinate_frame(scene)

# Arrange tables in a grid pattern
for i, table in enumerate(tables):
    table.center.x = scene.min.x + (i % 2 + 1.0) / 3.0 * scene.width
    table.center.y = scene.min.y + (i // 2 + 1.0) / 3.0 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MIN

# Place chairs around tables
for i, chair in enumerate(chairs):
    table = tables[i // 2]
    set_coordinate_frame(table)
    if i % 2 == 0:
        chair.min.y = table.max.y + 0.1
    else:
        chair.max.y = table.min.y - 0.1
    chair.center.x = table.center.x
    chair.min.z = scene.min.z
    chair.facing = table
set_coordinate_frame(scene)

# Mount wall shelves at different heights
shelf_heights = [1.2, 1.6, 2.0, 2.4]
for i, shelf in enumerate(wall_shelves):
    shelf.max.x = scene.max.x
    shelf.center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    shelf.min.z = shelf_heights[i]
    shelf.facing = X_MIN

# Position catwalks to connect wall shelves
for i, catwalk in enumerate(catwalks):
    catwalk.center.x = scene.max.x - 0.3 * scene.width
    catwalk.center.y = scene.min.y + (i+2.0) / 4.0 * scene.depth
    catwalk.min.z = 1.8
    catwalk.facing = Y_MAX

# Distribute cat trees
for i, tree in enumerate(cat_trees):
    tree.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    tree.min.y = scene.min.y + 0.1
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Place cat beds on shelves and floor
for i, bed in enumerate(cat_beds):
    if i < 2:
        set_coordinate_frame(wall_shelves[i])
        bed.center.x = wall_shelves[i].center.x
        bed.center.y = wall_shelves[i].center.y
        bed.min.z = wall_shelves[i].max.z
        bed.facing = wall_shelves[i].facing
    else:
        set_coordinate_frame(scene)
        bed.center.x = scene.min.x + (i-1.0) / 3.0 * scene.width
        bed.max.y = scene.max.y - 0.2
        bed.min.z = scene.min.z
        bed.facing = Y_MIN
set_coordinate_frame(scene)

# Position scratching posts
for i, post in enumerate(scratching_posts):
    post.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    post.min.y = scene.min.y + 0.2
    post.min.z = scene.min.z
    post.facing = Y_MAX

# Arrange plants and art
for i, plant in enumerate(plants):
    plant.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    plant.max.y = scene.max.y - 0.1
    plant.min.z = scene.min.z
    plant.facing = Y_MIN

for i, art in enumerate(cat_art):
    art.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    art.max.y = scene.max.y
    art.min.z = 1.5
    art.facing = Y_MIN