set_title("Race Track Section")
set_size(width=30.0, depth=22.0, height=3.0)
set_floor_asset("Grass", color="228B22")
set_wall_asset("Safety Barrier", interior=False, color="E0E0E0")

track = Object("Asphalt Road", width=7.0, depth=30.0, height=0.02, support=STANDING, color="696969")
track_barriers = [Object("Safety Barrier", width=30.0, depth=0.3, height=1.0, support=STANDING, color="FF0000") for _ in range(2)]
car = [Object("Racing Car", width=1.8, depth=4.7, height=1.1, support=STANDING, color=color) for color in ["FF2800", "004B49"]]

marshal_posts = [Object("Marshal Post", width=1.5, depth=1.5, height=2.0, support=STANDING, color="FFA500") for _ in range(3)]
advertising_boards = [Object("Advertisement Board", width=4.0, depth=0.2, height=1.5, support=STANDING, color="4169E1") for _ in range(5)]
camera_towers = [Object("Camera Tower", width=1.0, depth=1.0, height=2.0, support=STANDING, color="808080") for _ in range(2)]
safety_car = Object("Safety Car", width=1.8, depth=4.5, height=1.4, support=STANDING, color="FFFF00")
ambulance = Object("Ambulance", width=2.0, depth=5.0, height=2.0, support=STANDING, color="FFFFFF")
display = Object("Timing Display", width=2.0, depth=0.2, height=1.0, support=STANDING, color="32CD32")
tool_cart = Object("Tool Cart", width=1.0, depth=0.6, height=1.0, support=STANDING, color="1E90FF")
fuel_tank = Object("Fuel Tank", width=0.8, depth=0.8, height=1.2, support=STANDING, color="B8860B")