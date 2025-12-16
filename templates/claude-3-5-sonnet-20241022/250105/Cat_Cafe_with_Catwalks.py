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