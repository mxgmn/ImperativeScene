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