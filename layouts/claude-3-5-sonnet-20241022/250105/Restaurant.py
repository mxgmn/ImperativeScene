set_title("Restaurant")
set_size(width=12, depth=8, height=3)
set_floor_asset("Hardwood Floor", color="8B7355")
set_wall_asset("Painted Wall", interior=True, color="E8DCC4")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
kitchen_door = Door("Swing Door", width=0.9, depth=0.1, height=2.0, color="B8B8B8")
windows = [Window("Window", width=1.5, depth=0.1, height=1.5, color="ADD8E6") for _ in range(3)]

# Main dining area furniture
tables_4 = [Object("Dining Table", width=1.0, depth=1.0, height=0.75, support=STANDING, color="8B4513") for _ in range(4)]
tables_2 = [Object("Small Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="8B4513") for _ in range(3)]
chairs = [Object("Dining Chair", width=0.45, depth=0.45, height=0.9, support=STANDING, color="CD853F") for _ in range(22)]

# Service area
host_station = Object("Host Station", width=1.2, depth=0.6, height=1.1, support=STANDING, color="DEB887")
service_counter = Object("Service Counter", width=2.5, depth=0.6, height=1.1, support=STANDING, color="8B7355")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.3, support=STANDING, color="4A4A4A")

# Decor
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(3)]
wall_art = [Object("Framed Art", width=0.8, depth=0.05, height=0.6, support=MOUNTED, color="B8860B") for _ in range(4)]
menu_board = Object("Menu Board", width=1.0, depth=0.05, height=0.8, support=MOUNTED, color="8B4513")

# Storage and service items
storage_cabinet = Object("Storage Cabinet", width=1.8, depth=0.4, height=1.8, support=STANDING, color="A0522D")
water_station = Object("Water Station", width=0.8, depth=0.4, height=1.2, support=STANDING, color="4682B4")

entrance.center.x = scene.min.x + 0.25 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

kitchen_door.max.x = scene.max.x - 0.2 * scene.width
kitchen_door.max.y = scene.max.y
kitchen_door.min.z = scene.min.z
kitchen_door.facing = Y_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

# Tables for 4 people layout
table_spacing = 0.25
for i, table in enumerate(tables_4):
    table.center.x = scene.min.x + (i+1.5) / 5.0 * scene.width
    table.center.y = scene.min.y + 0.6 * scene.depth
    table.min.z = scene.min.z
    table.facing = Y_MIN

# Tables for 2 people along the wall
for i, table in enumerate(tables_2):
    table.max.x = scene.max.x - 0.1
    table.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    table.min.z = scene.min.z
    table.facing = X_MIN

# Place chairs around 4-person tables
chair_count = 0
for table in tables_4:
    set_coordinate_frame(table)
    for j in range(4):
        chair = chairs[chair_count]
        if j == 0:  # Front
            chair.center.x = table.center.x
            chair.min.y = table.min.y - 0.2
        elif j == 1:  # Back
            chair.center.x = table.center.x
            chair.max.y = table.max.y + 0.2
        elif j == 2:  # Left
            chair.min.x = table.min.x - 0.2
            chair.center.y = table.center.y
        else:  # Right
            chair.max.x = table.max.x + 0.2
            chair.center.y = table.center.y
        chair.min.z = scene.min.z
        chair.facing = table
        chair_count += 1
    set_coordinate_frame(scene)

# Place chairs around 2-person tables
for table in tables_2:
    set_coordinate_frame(table)
    for j in range(2):
        chair = chairs[chair_count]
        if j == 0:
            chair.min.x = table.min.x - 0.2
        else:
            chair.max.x = table.max.x + 0.2
        chair.center.y = table.center.y
        chair.min.z = scene.min.z
        chair.facing = table
        chair_count += 1
    set_coordinate_frame(scene)

host_station.min.x = scene.min.x + 0.1
host_station.center.y = scene.min.y + 0.2 * scene.depth
host_station.min.z = scene.min.z
host_station.facing = X_MAX

service_counter.max.x = scene.max.x - 0.1
service_counter.max.y = scene.max.y - 0.1
service_counter.min.z = scene.min.z
service_counter.facing = Y_MIN

set_coordinate_frame(service_counter)
register.center.x = service_counter.center.x
register.center.y = service_counter.center.y
register.min.z = service_counter.max.z
register.facing = service_counter.facing
set_coordinate_frame(scene)

for i, plant in enumerate(plants):
    if i == 0:
        plant.min.x = scene.min.x + 0.1
        plant.min.y = scene.min.y + 0.1
    elif i == 1:
        plant.max.x = scene.max.x - 0.1
        plant.min.y = scene.min.y + 0.1
    else:
        plant.center.x = scene.center.x
        plant.max.y = scene.max.y - 0.1
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

for i, art in enumerate(wall_art):
    art.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    art.max.y = scene.max.y
    art.min.z = 1.5
    art.facing = Y_MIN

menu_board.max.x = scene.max.x - 0.1
menu_board.center.y = scene.min.y + 0.3 * scene.depth
menu_board.min.z = 1.6
menu_board.facing = X_MIN

storage_cabinet.max.x = scene.max.x - 0.1
storage_cabinet.center.y = scene.max.y - 0.2 * scene.depth
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MIN

water_station.min.x = scene.min.x + 0.1
water_station.max.y = scene.max.y - 0.1
water_station.min.z = scene.min.z
water_station.facing = Y_MIN