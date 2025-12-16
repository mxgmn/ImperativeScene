set_title("Kindergarten")
set_size(width=8, depth=10, height=3)
set_floor_asset("Rubber Floor", color="9ED2BE")
set_wall_asset("Painted Wall", interior=True, color="FFF4E0")

entrance = Door("Colorful Door", width=0.9, depth=0.1, height=2.0, color="FF69B4")
bathroom_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="DEB887")
windows = [Window("Window", width=1.2, depth=0.1, height=1.2, color="87CEEB") for _ in range(3)]

activity_tables = [Object("Round Table", width=1.2, depth=1.2, height=0.6, support=STANDING, color="FF6B6B") for _ in range(3)]
tiny_chairs = [Object("Small Chair", width=0.3, depth=0.3, height=0.5, support=STANDING, color="4ECDC4") for _ in range(12)]

toy_shelf = Object("Toy Storage Unit", width=2.4, depth=0.4, height=1.2, support=STANDING, color="FFD93D")
book_shelf = Object("Book Shelf", width=1.8, depth=0.3, height=1.0, support=STANDING, color="6C5B7B")
art_easel = Object("Art Easel", width=0.6, depth=0.5, height=1.2, support=STANDING, color="F8B195")

play_kitchen = Object("Play Kitchen Set", width=1.2, depth=0.4, height=0.8, support=STANDING, color="95E1D3")
play_mat = Object("Activity Mat", width=2.0, depth=2.0, height=0.02, support=STANDING, color="A8E6CF")
building_blocks = Object("Block Storage Box", width=0.6, depth=0.4, height=0.4, support=STANDING, color="FF847C")

notice_board = Object("Notice Board", width=1.2, depth=0.05, height=0.8, support=MOUNTED, color="F67280")
alphabet_chart = Object("Alphabet Chart", width=1.5, depth=0.02, height=0.9, support=MOUNTED, color="C06C84")

storage_cubbies = Object("Cubby Storage", width=2.4, depth=0.3, height=1.0, support=STANDING, color="6C5B7B")
teacher_desk = Object("Teacher Desk", width=1.2, depth=0.6, height=0.75, support=STANDING, color="A8A8A8")
teacher_chair = Object("Office Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="355C7D")

entrance.max.x = scene.max.x - 0.2 * scene.width
entrance.max.y = scene.max.y
entrance.min.z = scene.min.z
entrance.facing = Y_MIN

bathroom_door.max.x = scene.max.x
bathroom_door.max.y = scene.max.y - 0.2 * scene.depth
bathroom_door.min.z = scene.min.z
bathroom_door.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

for i, table in enumerate(activity_tables):
    table.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    table.center.y = scene.min.y + 0.4 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MAX

for i, chair in enumerate(tiny_chairs):
    table_index = i // 4
    position = i % 4
    set_coordinate_frame(activity_tables[table_index])
    angle = position * 1.57  # 90 degrees in radians
    radius = 0.8
    chair.center.x = activity_tables[table_index].center.x + radius * math.cos(angle)
    chair.center.y = activity_tables[table_index].center.y + radius * math.sin(angle)
    chair.min.z = scene.min.z
    chair.facing = activity_tables[table_index]
set_coordinate_frame(scene)

toy_shelf.min.x = scene.min.x
toy_shelf.center.y = scene.min.y + 0.7 * scene.depth
toy_shelf.min.z = scene.min.z
toy_shelf.facing = X_MAX

book_shelf.max.x = scene.max.x
book_shelf.center.y = scene.min.y + 0.3 * scene.depth
book_shelf.min.z = scene.min.z
book_shelf.facing = X_MIN

art_easel.max.x = scene.max.x - 0.2
art_easel.center.y = scene.min.y + 0.6 * scene.depth
art_easel.min.z = scene.min.z
art_easel.facing = Y_MIN

play_kitchen.min.x = scene.min.x + 0.2
play_kitchen.max.y = scene.max.y - 0.2
play_kitchen.min.z = scene.min.z
play_kitchen.facing = X_MAX

play_mat.center.x = scene.center.x
play_mat.max.y = scene.max.y - 0.2
play_mat.min.z = scene.min.z
play_mat.facing = Y_MIN

building_blocks.min.x = toy_shelf.max.x + 0.2
building_blocks.center.y = toy_shelf.center.y
building_blocks.min.z = scene.min.z
building_blocks.facing = X_MAX

notice_board.center.x = scene.center.x
notice_board.max.y = scene.max.y
notice_board.min.z = 1.2
notice_board.facing = Y_MIN

alphabet_chart.min.x = scene.min.x
alphabet_chart.center.y = scene.center.y
alphabet_chart.min.z = 1.0
alphabet_chart.facing = X_MAX

storage_cubbies.max.x = scene.max.x
storage_cubbies.min.y = scene.min.y + 0.2
storage_cubbies.min.z = scene.min.z
storage_cubbies.facing = X_MIN

teacher_desk.max.x = scene.max.x - 0.2
teacher_desk.max.y = scene.max.y - 0.3
teacher_desk.min.z = scene.min.z
teacher_desk.facing = Y_MIN

set_coordinate_frame(teacher_desk)
teacher_chair.center.x = teacher_desk.center.x
teacher_chair.min.y = teacher_desk.max.y + 0.1
teacher_chair.min.z = scene.min.z
teacher_chair.facing = teacher_desk
set_coordinate_frame(scene)