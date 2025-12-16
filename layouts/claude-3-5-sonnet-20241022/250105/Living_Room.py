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

entrance_door.max.x = scene.max.x
entrance_door.center.y = scene.min.y + 0.2 * scene.depth
entrance_door.min.z = scene.min.z
entrance_door.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

tv_stand.center.x = scene.min.x + 0.3 * scene.width
tv_stand.min.y = scene.min.y
tv_stand.min.z = scene.min.z
tv_stand.facing = Y_MAX

set_coordinate_frame(tv_stand)
tv.center.x = tv_stand.center.x
tv.min.y = tv_stand.min.y
tv.min.z = tv_stand.max.z + 0.1
tv.facing = tv_stand.facing
set_coordinate_frame(scene)

sofa.center.x = scene.min.x + 0.6 * scene.width
sofa.max.y = scene.max.y
sofa.min.z = scene.min.z
sofa.facing = tv

for i, armchair in enumerate(armchairs):
    if i == 0:
        armchair.min.x = sofa.min.x - armchair.width - 0.3
    else:
        armchair.max.x = sofa.max.x + armchair.width + 0.3
    armchair.center.y = sofa.center.y - 0.3
    armchair.min.z = scene.min.z
    armchair.facing = tv

coffee_table.center.x = sofa.center.x
coffee_table.center.y = sofa.center.y - sofa.depth - 0.5
coffee_table.min.z = scene.min.z
coffee_table.facing = sofa

rug.center = coffee_table.center
rug.min.z = scene.min.z
rug.facing = coffee_table.facing

bookshelf.max.x = scene.max.x
bookshelf.max.y = scene.max.y
bookshelf.min.z = scene.min.z
bookshelf.facing = X_MIN

console_table.min.x = scene.min.x
console_table.center.y = scene.center.y
console_table.min.z = scene.min.z
console_table.facing = X_MAX

side_table.center.x = sofa.min.x - 0.1
side_table.min.y = sofa.min.y
side_table.min.z = scene.min.z
side_table.facing = sofa

plants[0].min.x = scene.min.x
plants[0].min.y = scene.min.y
plants[0].min.z = scene.min.z
plants[0].facing = Y_MAX

set_coordinate_frame(console_table)
plants[1].center.x = console_table.center.x
plants[1].center.y = console_table.center.y
plants[1].min.z = console_table.max.z
plants[1].facing = console_table.facing
set_coordinate_frame(scene)

for i, painting in enumerate(paintings):
    if i == 0:
        painting.center.x = tv_stand.center.x
        painting.max.y = scene.max.y
    else:
        painting.center.x = console_table.center.x
        painting.min.y = scene.min.y
    painting.min.z = 1.8
    painting.facing = Y_MIN if i == 0 else Y_MAX