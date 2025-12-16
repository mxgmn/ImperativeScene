set_title("Mancave")
set_size(width=8, depth=6, height=2.8)
set_floor_asset("Wood Planks Floor", color="8B4513")
set_wall_asset("Wood Panel Wall", interior=True, color="6B4423")

door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
window = Window("Small Window", width=1.2, depth=0.1, height=1.0, color="87CEEB")

# Main entertainment setup
tv = Object("Flat Screen TV", width=1.8, depth=0.1, height=1.0, support=MOUNTED, color="2F4F4F")
tv_stand = Object("TV Console", width=2.0, depth=0.5, height=0.6, support=STANDING, color="A0522D")
gaming_console = Object("Gaming Console", width=0.3, depth=0.25, height=0.1, support=STANDING, color="1E90FF")

# Seating
recliner = Object("Leather Recliner", width=1.0, depth=1.2, height=1.1, support=STANDING, color="8B0000")
couch = Object("Large Sofa", width=2.2, depth=1.0, height=0.9, support=STANDING, color="A52A2A")
bean_bag = Object("Bean Bag Chair", width=0.9, depth=0.9, height=0.5, support=STANDING, color="FF4500")

# Entertainment elements
pool_table = Object("Pool Table", width=2.8, depth=1.4, height=0.8, support=STANDING, color="006400")
dart_board = Object("Dart Board", width=0.5, depth=0.05, height=0.5, support=MOUNTED, color="CD853F")

# Storage and decor
mini_fridge = Object("Mini Fridge", width=0.6, depth=0.6, height=0.8, support=STANDING, color="708090")
bar_cabinet = Object("Bar Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
trophy_case = Object("Trophy Case", width=1.0, depth=0.3, height=1.8, support=STANDING, color="B8860B")
posters = [Object("Sports Poster", width=0.8, depth=0.02, height=1.2, support=MOUNTED, color="4169E1") for _ in range(3)]

# Additional furniture
side_table = Object("Side Table", width=0.5, depth=0.5, height=0.6, support=STANDING, color="8B4513")
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.75, support=STANDING, color="B22222") for _ in range(2)]

door.max.x = scene.max.x - 0.2 * scene.width
door.min.y = scene.min.y
door.min.z = scene.min.z
door.facing = Y_MAX

window.min.x = scene.min.x
window.center.y = scene.min.y + 0.3 * scene.depth
window.min.z = 1.2
window.facing = X_MAX

tv_stand.center.x = scene.min.x + 0.3 * scene.width
tv_stand.min.y = scene.min.y
tv_stand.min.z = scene.min.z
tv_stand.facing = Y_MAX

tv.center.x = tv_stand.center.x
tv.min.y = tv_stand.min.y
tv.min.z = tv_stand.max.z + 0.2
tv.facing = tv_stand.facing

set_coordinate_frame(tv_stand)
gaming_console.center.x = tv_stand.center.x
gaming_console.center.y = tv_stand.center.y
gaming_console.min.z = tv_stand.max.z
gaming_console.facing = tv_stand.facing
set_coordinate_frame(scene)

couch.center.x = tv.center.x
couch.center.y = scene.min.y + 0.35 * scene.depth
couch.min.z = scene.min.z
couch.facing = tv

recliner.min.x = couch.max.x + 0.3
recliner.center.y = couch.center.y
recliner.min.z = scene.min.z
recliner.facing = tv

bean_bag.max.x = couch.min.x - 0.3
bean_bag.center.y = couch.center.y
bean_bag.min.z = scene.min.z
bean_bag.facing = tv

pool_table.center.x = scene.max.x - 0.3 * scene.width
pool_table.max.y = scene.max.y - 0.2
pool_table.min.z = scene.min.z
pool_table.facing = X_MAX

dart_board.max.x = scene.max.x
dart_board.center.y = scene.min.y + 0.3 * scene.depth
dart_board.min.z = 1.5
dart_board.facing = X_MIN

mini_fridge.min.x = scene.min.x
mini_fridge.max.y = scene.max.y
mini_fridge.min.z = scene.min.z
mini_fridge.facing = X_MAX

bar_cabinet.min.x = mini_fridge.max.x + 0.2
bar_cabinet.max.y = scene.max.y
bar_cabinet.min.z = scene.min.z
bar_cabinet.facing = Y_MIN

trophy_case.max.x = scene.max.x
trophy_case.max.y = scene.max.y
trophy_case.min.z = scene.min.z
trophy_case.facing = X_MIN

side_table.min.x = recliner.min.x
side_table.min.y = recliner.max.y + 0.1
side_table.min.z = scene.min.z
side_table.facing = recliner.facing

set_coordinate_frame(bar_cabinet)
for i, stool in enumerate(bar_stools):
    stool.center.x = bar_cabinet.min.x + (i+1.0) / 3.0 * bar_cabinet.width
    stool.min.y = bar_cabinet.max.y + 0.1
    stool.min.z = scene.min.z
    stool.facing = bar_cabinet
set_coordinate_frame(scene)

spacing = 0.25
for i, poster in enumerate(posters):
    poster.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    poster.max.y = scene.max.y
    poster.min.z = 1.0
    poster.facing = Y_MIN