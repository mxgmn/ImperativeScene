set_title("Treetop House")
set_size(width=8, depth=8, height=4)
set_floor_asset("Wooden Planks Floor", color="8B7355")
set_wall_asset("no walls", interior=False, color="A0522D")

# Main structural elements
trunk = Object("Tree Trunk", width=0.5, depth=0.5, height=2.0, support=STANDING, color="654321")
platform = Object("Wooden Platform", width=6.0, depth=6.0, height=0.2, support=STANDING, color="DEB887")
railing = [Object("Wooden Railing", width=5.8, depth=0.1, height=1.0, support=STANDING, color="B8860B") for _ in range(4)]

# Furniture and decorations
bed = Object("Rustic Bed", width=1.2, depth=2.0, height=0.5, support=STANDING, color="8B4513")
table = Object("Round Table", width=1.0, depth=1.0, height=0.75, support=STANDING, color="DAA520")
chairs = [Object("Wooden Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="CD853F") for _ in range(3)]
bookshelf = Object("Wooden Bookshelf", width=1.8, depth=0.4, height=2.0, support=STANDING, color="D2691E")
chest = Object("Storage Chest", width=1.0, depth=0.6, height=0.5, support=STANDING, color="8B4513")
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=0.6, support=STANDING, color="228B22") for _ in range(2)]
hammock = Object("Hammock", width=1.8, depth=0.8, height=0.4, support=STANDING, color="F4A460")
telescope = Object("Telescope", width=0.3, depth=0.8, height=1.2, support=STANDING, color="B8860B")