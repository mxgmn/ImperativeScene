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

track.center.x = scene.center.x
track.center.y = scene.center.y
track.min.z = scene.min.z
track.facing = Y_MAX

param = 0.5
track_barriers[0].center.x = track.center.x - track.width * param
track_barriers[0].center.y = track.center.y
track_barriers[0].min.z = scene.min.z
track_barriers[0].facing = Y_MAX

track_barriers[1].center.x = track.center.x + track.width * param
track_barriers[1].center.y = track.center.y
track_barriers[1].min.z = scene.min.z
track_barriers[1].facing = Y_MAX

set_coordinate_frame(track)
car[0].center.x = track.center.x - 0.2 * track.width
car[0].center.y = track.min.y + 0.3 * track.depth
car[0].min.z = track.max.z
car[0].facing = Y_MAX

car[1].center.x = track.center.x + 0.2 * track.width
car[1].center.y = track.min.y + 0.4 * track.depth
car[1].min.z = track.max.z
car[1].facing = Y_MAX
set_coordinate_frame(scene)

spacing = 0.33
for i, post in enumerate(marshal_posts):
    post.min.x = track_barriers[1].max.x + 1.0
    post.center.y = scene.min.y + (i + 1.0) * spacing * scene.depth
    post.min.z = scene.min.z
    post.facing = track

spacing = 0.2
for i, board in enumerate(advertising_boards):
    board.max.x = track_barriers[0].min.x - 1.0
    board.center.y = scene.min.y + (i + 1.0) * spacing * scene.depth
    board.min.z = scene.min.z
    board.facing = X_MAX

camera_towers[0].min.x = track_barriers[0].min.x - 2.0
camera_towers[0].min.y = scene.min.y + 0.1 * scene.depth
camera_towers[0].min.z = scene.min.z
camera_towers[0].facing = track

camera_towers[1].max.x = track_barriers[1].max.x + 2.0
camera_towers[1].max.y = scene.max.y - 0.1 * scene.depth
camera_towers[1].min.z = scene.min.z
camera_towers[1].facing = track

safety_car.min.x = track_barriers[1].max.x + 2.0
safety_car.min.y = scene.min.y + 0.2 * scene.depth
safety_car.min.z = scene.min.z
safety_car.facing = Y_MAX

ambulance.min.x = track_barriers[1].max.x + 2.0
ambulance.max.y = scene.max.y - 0.2 * scene.depth
ambulance.min.z = scene.min.z
ambulance.facing = Y_MAX

display.max.x = track_barriers[0].min.x - 1.0
display.max.y = scene.max.y - 0.1 * scene.depth
display.min.z = scene.min.z
display.facing = X_MAX

tool_cart.min.x = track_barriers[1].max.x + 1.0
tool_cart.center.y = scene.center.y
tool_cart.min.z = scene.min.z
tool_cart.facing = X_MIN

fuel_tank.min.x = track_barriers[1].max.x + 3.0
fuel_tank.center.y = scene.center.y
fuel_tank.min.z = scene.min.z
fuel_tank.facing = X_MIN