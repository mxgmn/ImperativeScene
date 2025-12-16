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

set_coordinate_frame(nightstands[0])
plants[0].center.x = nightstands[0].center.x
plants[0].center.y = nightstands[0].center.y
plants[0].min.z = nightstands[0].max.z
plants[0].facing = nightstands[0].facing
set_coordinate_frame(scene)

set_coordinate_frame(dresser)
plants[1].max.x = dresser.max.x - 0.1
plants[1].min.y = dresser.min.y + 0.1
plants[1].min.z = dresser.max.z
plants[1].facing = dresser.facing
set_coordinate_frame(scene)

for i, painting in enumerate(paintings):
    painting.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    painting.max.y = scene.max.y
    painting.min.z = 1.4
    painting.facing = Y_MIN