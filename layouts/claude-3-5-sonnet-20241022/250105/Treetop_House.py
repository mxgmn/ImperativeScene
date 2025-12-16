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

trunk.center.x = scene.center.x
trunk.center.y = scene.center.y
trunk.min.z = scene.min.z
trunk.facing = Y_MAX

platform.center.x = scene.center.x
platform.center.y = scene.center.y
platform.min.z = trunk.max.z
platform.facing = Y_MAX

set_coordinate_frame(platform)
# Place railings around the platform
railing[0].center.x = platform.center.x
railing[0].min.y = platform.min.y
railing[0].min.z = platform.max.z
railing[0].facing = Y_MAX

railing[1].center.x = platform.center.x
railing[1].max.y = platform.max.y
railing[1].min.z = platform.max.z
railing[1].facing = Y_MIN

railing[2].min.x = platform.min.x
railing[2].center.y = platform.center.y
railing[2].min.z = platform.max.z
railing[2].facing = X_MAX

railing[3].max.x = platform.max.x
railing[3].center.y = platform.center.y
railing[3].min.z = platform.max.z
railing[3].facing = X_MIN

bed.min.x = platform.min.x + 0.2
bed.max.y = platform.max.y - 0.2
bed.min.z = platform.max.z
bed.facing = Y_MIN

table.center.x = platform.center.x
table.min.y = platform.min.y + 0.2
table.min.z = platform.max.z
table.facing = Y_MAX

for i, chair in enumerate(chairs):
    chair.center.x = table.center.x + (i-1.0) * 0.5
    chair.min.y = table.max.y + 0.1
    chair.min.z = platform.max.z
    chair.facing = table

bookshelf.max.x = platform.max.x - 0.2
bookshelf.min.y = platform.min.y + 0.2
bookshelf.min.z = platform.max.z
bookshelf.facing = X_MIN

chest.min.x = platform.min.x + 0.2
chest.min.y = platform.min.y + 0.2
chest.min.z = platform.max.z
chest.facing = X_MAX

plants[0].min.x = platform.min.x + 0.2
plants[0].center.y = platform.center.y
plants[0].min.z = platform.max.z
plants[0].facing = X_MAX

plants[1].max.x = platform.max.x - 0.2
plants[1].center.y = platform.center.y
plants[1].min.z = platform.max.z
plants[1].facing = X_MIN

hammock.max.x = platform.max.x - 0.2
hammock.max.y = platform.max.y - 0.2
hammock.min.z = platform.max.z
hammock.facing = X_MIN

telescope.max.x = platform.max.x - 0.2
telescope.min.y = platform.min.y + 0.2
telescope.min.z = platform.max.z
telescope.facing = Y_MAX

set_coordinate_frame(scene)