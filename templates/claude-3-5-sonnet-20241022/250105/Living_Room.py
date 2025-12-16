set_title("Living Room")
set_size(width=8, depth=6, height=3)
set_floor_asset("Hardwood Floor", color="8B7355")
set_wall_asset("Painted Wall", interior=True, color="E8E5DE")

entrance_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="87CEEB") for _ in range(2)]

# Main furniture pieces
sofa = Object("Sofa", width=2.2, depth=0.9, height=0.9, support=STANDING, color="4682B4")
armchairs = [Object("Armchair", width=1.0, depth=0.9, height=0.9, support=STANDING, color="4169E1") for _ in range(2)]
coffee_table = Object("Coffee Table", width=1.2, depth=0.6, height=0.45, support=STANDING, color="8B4513")
tv_stand = Object("TV Stand", width=1.8, depth=0.4, height=0.6, support=STANDING, color="A0522D")
tv = Object("Television", width=1.6, depth=0.1, height=0.9, support=MOUNTED, color="2F4F4F")

# Storage and decoration
bookshelf = Object("Bookshelf", width=1.8, depth=0.4, height=2.0, support=STANDING, color="8B7355")
console_table = Object("Console Table", width=1.2, depth=0.35, height=0.8, support=STANDING, color="DEB887")
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=1.2, support=STANDING, color="228B22") for _ in range(2)]
rug = Object("Area Rug", width=2.4, depth=1.8, height=0.02, support=STANDING, color="B8860B")
paintings = [Object("Painting", width=0.8, depth=0.05, height=1.0, support=MOUNTED, color="CD853F") for _ in range(2)]
side_table = Object("Side Table", width=0.5, depth=0.5, height=0.6, support=STANDING, color="8B4513")