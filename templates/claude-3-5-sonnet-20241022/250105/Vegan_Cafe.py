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