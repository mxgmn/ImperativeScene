set_title("Cozy Italian Restaurant")
set_size(width=7, depth=4, height=3)
set_floor_asset("Terracotta Tiles Floor")
set_wall_asset("Venetian Plaster Wall", interior=True)

kitchen_door = Door("Metal Door", width=0.75, depth=0.1, height=2.0)
entrance_door = Door("Wooden Door", width=0.85, depth=0.1, height=2.0)
window = Window("Window", width=2.4, depth=0.1, height=1.5)
tables = [Object("Vintage Table", width=1.3, depth=0.8, height=0.6, support=STANDING, dynamic=False) for _ in range(2)]
chairs = [Object("Durable Chair", 0.45, 0.45, height=0.8, support=STANDING, dynamic=True) for _ in range(4 * len(tables))]
counter = Object("Counter", width=3.0, depth=0.4, height=1.1, support=STANDING, dynamic=False)
stools = [Object("Bar Stool", 0.4, 0.4, height=0.75, support=STANDING, dynamic=True) for _ in range(3)]
register = Object("Cash Register", 0.3, 0.3, height=0.2, support=STANDING, dynamic=True)
menu = Object("Menu Board", width=0.5, depth=0.05, height=0.85, support=MOUNTED, dynamic=False)
shelf = Object("Wall-mounted Shelf", width=1.6, depth=0.4, height=0.05, support=MOUNTED, dynamic=False)
cheese_wheels = [Object("Cheese Wheel", 0.2 * scale, 0.2 * scale, height=0.15 * scale, support=STANDING, dynamic=True) for i in range(4) for scale in [1.0 + i * 0.3]]
paintings = [Object("Still Life Painting", width=0.6, depth=0.04, height=0.5, support=MOUNTED, dynamic=False) for _ in range(3)]

kitchen_door.max.x = scene.max.x
kitchen_door.max.y = scene.max.y - 0.2
kitchen_door.min.z = scene.min.z
kitchen_door.facing = X_MIN

entrance_door.min.x = scene.min.x + 0.5
entrance_door.max.y = scene.max.y
entrance_door.min.z = scene.min.z
entrance_door.facing = Y_MIN

window.min.x = scene.min.x
window.center.y = scene.min.y + 0.5 * scene.depth
window.min.z = 0.8
window.facing = X_MAX

for i, table in enumerate(tables):
    table.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    table.center.y = scene.min.y + 0.33 * scene.depth
    table.min.z = scene.min.z
    table.facing = X_MIN

for i, chair in enumerate(chairs):
    table = tables[i // 4]
    set_coordinate_frame(table)
    chair.center.x = table.min.x + (0.25 if (i//2) % 2 == 0 else 0.75) * table.width
    if i % 2 == 0:
        chair.max.y = table.min.y - 0.1
    else:
        chair.min.y = table.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = table
set_coordinate_frame(scene)

counter.center.x = scene.min.x + 0.5 * scene.width
counter.max.y = scene.max.y
counter.min.z = scene.min.z
counter.facing = Y_MIN

set_coordinate_frame(counter)
for i, stool in enumerate(stools):
    stool.center.x = counter.min.x + (i+1.0) / 4.0 * counter.width
    stool.min.y = counter.max.y + 0.1
    stool.min.z = scene.min.z
    stool.facing = counter
register.center.x = counter.min.x + 0.25 * counter.width
register.center.y = counter.center.y
register.min.z = counter.max.z
register.facing = counter.facing
set_coordinate_frame(scene)

menu.center.x = counter.min.x + 0.33 * counter.width
menu.max.y = scene.max.y
menu.min.z = 1.5
menu.facing = Y_MIN

shelf.max.x = scene.max.x
shelf.center.y = scene.min.y + 0.5 * scene.depth
shelf.min.z = 1.6
shelf.facing = X_MIN

set_coordinate_frame(shelf)
for i, cheese in enumerate(cheese_wheels):
    cheese.center.x = shelf.min.x + (i+0.5) / 4.0 * shelf.width # shelf is divided into 4 squares, each cheese wheel is centered on the corresponding square
    cheese.center.y = shelf.center.y
    cheese.min.z = shelf.max.z
    cheese.facing = shelf.facing
set_coordinate_frame(scene)

for i, painting in enumerate(paintings):
    painting.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    painting.min.y = scene.min.y
    painting.min.z = 1.7
    painting.facing = Y_MAX