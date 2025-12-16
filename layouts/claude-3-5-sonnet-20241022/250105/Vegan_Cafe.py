set_title("Vegan Cafe")
set_size(width=8, depth=10, height=3)
set_floor_asset("Bamboo Floor", color="C4A484")
set_wall_asset("Painted Wall", interior=True, color="E8E4D6")

entrance = Door("Glass Door", width=1.0, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="ADD8E6") for _ in range(3)]

counter = Object("Service Counter", width=2.5, depth=0.6, height=1.1, support=STANDING, color="7B9E89")
coffee_machine = Object("Coffee Machine", width=0.8, depth=0.4, height=0.4, support=STANDING, color="FF6B6B")
tables = [Object("Round Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="8FBC8F") for _ in range(6)]
chairs = [Object("Modern Chair", width=0.45, depth=0.45, height=0.85, support=STANDING, color="E9967A") for _ in range(18)]
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=1.2, support=STANDING, color="228B22") for _ in range(4)]
menu_board = Object("Menu Board", width=1.2, depth=0.05, height=0.8, support=MOUNTED, color="FFA07A")
shelf_unit = Object("Shelving Unit", width=1.6, depth=0.4, height=2.0, support=STANDING, color="B8860B")
sofa = Object("Lounge Sofa", width=1.8, depth=0.8, height=0.9, support=STANDING, color="FF8C69")
coffee_table = Object("Coffee Table", width=1.2, depth=0.6, height=0.45, support=STANDING, color="DEB887")
art_pieces = [Object("Wall Art", width=0.6, depth=0.05, height=0.8, support=MOUNTED, color="FF69B4") for _ in range(3)]
display_case = Object("Display Case", width=1.8, depth=0.5, height=1.2, support=STANDING, color="98FB98")

entrance.center.x = scene.min.x + 0.3 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

back_door.max.x = scene.max.x
back_door.max.y = scene.max.y - 0.2 * scene.depth
back_door.min.z = scene.min.z
back_door.facing = X_MIN

window_spacing = 0.25
for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

counter.max.x = scene.max.x - 0.2
counter.max.y = scene.max.y
counter.min.z = scene.min.z
counter.facing = Y_MIN

set_coordinate_frame(counter)
coffee_machine.center.x = counter.center.x
coffee_machine.center.y = counter.center.y
coffee_machine.min.z = counter.max.z
coffee_machine.facing = counter.facing
set_coordinate_frame(scene)

table_spacing = 0.3
for i, table in enumerate(tables):
    if i < 3:
        table.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
        table.center.y = scene.min.y + 0.3 * scene.depth
    else:
        table.center.x = scene.min.x + (i-2.0) / 4.0 * scene.width
        table.center.y = scene.min.y + 0.6 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MAX

chair_spacing = 0.1
for i, chair in enumerate(chairs):
    table_idx = i // 3
    chair_pos = i % 3
    table = tables[table_idx]
    set_coordinate_frame(table)
    angle = chair_pos * 2.0 * 3.14159 / 3.0
    chair.center.x = table.center.x + 0.5 * math.cos(angle)
    chair.center.y = table.center.y + 0.5 * math.sin(angle)
    chair.min.z = scene.min.z
    chair.facing = table
set_coordinate_frame(scene)

for i, plant in enumerate(plants):
    if i < 2:
        plant.min.x = scene.min.x + i * 0.5
        plant.min.y = scene.min.y
    else:
        plant.max.x = scene.max.x - (i-2) * 0.5
        plant.min.y = scene.min.y
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

menu_board.center.x = counter.center.x
menu_board.max.y = scene.max.y
menu_board.min.z = 1.8
menu_board.facing = Y_MIN

shelf_unit.min.x = scene.min.x
shelf_unit.max.y = scene.max.y
shelf_unit.min.z = scene.min.z
shelf_unit.facing = X_MAX

sofa.min.x = scene.min.x
sofa.center.y = scene.center.y
sofa.min.z = scene.min.z
sofa.facing = X_MAX

coffee_table.center.x = sofa.center.x + sofa.width
coffee_table.center.y = sofa.center.y
coffee_table.min.z = scene.min.z
coffee_table.facing = sofa.facing

for i, art in enumerate(art_pieces):
    art.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    art.max.y = scene.max.y
    art.min.z = 1.5
    art.facing = Y_MIN

display_case.min.x = counter.min.x
display_case.max.y = counter.max.y
display_case.min.z = scene.min.z
display_case.facing = counter.facing