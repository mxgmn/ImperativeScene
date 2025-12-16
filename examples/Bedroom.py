set_title("Bedroom")
set_size(width=5, depth=6, height=2.8)
set_floor_asset("Wooden Floor")
set_wall_asset("Painted Wall", interior=True)

door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0)
window = Window("Window", width=1.8, depth=0.1, height=1.5)
bed = Object("Double Bed", width=1.6, depth=2.0, height=0.6, support=STANDING, dynamic=False)
nightstands = [Object("Nightstand", width=0.5, depth=0.4, height=0.6, support=STANDING, dynamic=False) for _ in range(2)]
wardrobe = Object("Wardrobe", width=1.2, depth=0.6, height=2.2, support=STANDING, dynamic=False)
dresser = Object("Dresser", width=1.2, depth=0.5, height=0.8, support=STANDING, dynamic=False)
mirror = Object("Wall Mirror", width=0.8, depth=0.05, height=1.2, support=MOUNTED, dynamic=False)
rug = Object("Area Rug", width=2.0, depth=1.6, height=0.02, support=STANDING, dynamic=False)
desk = Object("Study Desk", width=1.2, depth=0.6, height=0.75, support=STANDING, dynamic=False)
chair = Object("Desk Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, dynamic=True)
lamp = Object("Table Lamp", width=0.3, depth=0.3, height=0.4, support=STANDING, dynamic=True)
plants = [Object("Indoor Plant", width=0.3, depth=0.3, height=0.6, support=STANDING, dynamic=True) for _ in range(2)]
paintings = [Object("Wall Art", width=0.6, depth=0.05, height=0.8, support=MOUNTED, dynamic=False) for _ in range(2)]

door.max.x = scene.max.x
door.center.y = scene.min.y + 0.2 * scene.depth
door.min.z = scene.min.z
door.facing = X_MIN

window.center.x = scene.min.x + 0.5 * scene.width
window.min.y = scene.min.y
window.min.z = 0.8
window.facing = Y_MAX

bed.center.x = scene.min.x + 0.5 * scene.width
bed.max.y = scene.max.y
bed.min.z = scene.min.z
bed.facing = Y_MIN

set_coordinate_frame(bed)
for i, nightstand in enumerate(nightstands):
    if i == 0:
        nightstand.max.x = bed.min.x - 0.1
    else:
        nightstand.min.x = bed.max.x + 0.1
    nightstand.min.y = bed.min.y
    nightstand.min.z = scene.min.z
    nightstand.facing = bed.facing
set_coordinate_frame(scene)

wardrobe.min.x = scene.min.x
wardrobe.min.y = scene.min.y + 0.1 * scene.depth
wardrobe.min.z = scene.min.z
wardrobe.facing = X_MAX

dresser.max.x = scene.max.x
dresser.center.y = scene.min.y + 0.5 * scene.depth
dresser.min.z = scene.min.z
dresser.facing = X_MIN

set_coordinate_frame(dresser)
mirror.center.x = dresser.center.x
mirror.min.y = dresser.min.y
mirror.min.z = dresser.max.z + 0.2
mirror.facing = dresser.facing
set_coordinate_frame(scene)

rug.center.x = bed.center.x
rug.max.y = bed.min.y - 0.3
rug.min.z = scene.min.z
rug.facing = bed

desk.min.x = scene.min.x
desk.center.y = scene.min.y + 0.5 * scene.depth
desk.min.z = scene.min.z
desk.facing = X_MAX

set_coordinate_frame(desk)
chair.center.x = desk.center.x
chair.min.y = desk.max.y + 0.1
chair.min.z = scene.min.z
chair.facing = desk
lamp.max.x = desk.max.x - 0.1
lamp.min.y = desk.min.y + 0.1
lamp.min.z = desk.max.z
lamp.facing = desk.facing
set_coordinate_frame(scene)

for i, plant in enumerate(plants):
    nightstand = nightstands[i]
    set_coordinate_frame(nightstand)
    plant.center.x = nightstand.center.x
    plant.center.y = nightstand.center.y
    plant.min.z = nightstand.max.z
    plant.facing = nightstand.facing
    set_coordinate_frame(scene)

for i, painting in enumerate(paintings):
    painting.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    painting.max.y = scene.max.y
    painting.min.z = 1.4
    painting.facing = Y_MIN