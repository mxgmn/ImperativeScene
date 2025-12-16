set_title("Electronics Shop")
set_size(width=8, depth=10, height=3)
set_floor_asset("Vinyl Floor", color="9BA0A8")
set_wall_asset("Painted Wall", interior=True, color="E6E6E8")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="708090")
windows = [Window("Display Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(2)]

# Main display shelves along walls
wall_shelves = [Object("Display Shelf", width=2.0, depth=0.4, height=2.0, support=STANDING, color="F5F5F5") for _ in range(4)]

# Central display islands
display_islands = [Object("Display Table", width=1.2, depth=0.8, height=0.9, support=STANDING, color="E0E0E0") for _ in range(2)]

# Counter area
counter = Object("Sales Counter", width=2.0, depth=0.6, height=1.0, support=STANDING, color="4682B4")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.2, support=STANDING, color="1E90FF")

# Display items (representing groups of products)
laptops = [Object("Laptop", width=0.4, depth=0.3, height=0.02, support=STANDING, color="AAAAAA") for _ in range(6)]
smartphones = [Object("Smartphone", width=0.05, depth=0.1, height=0.01, support=STANDING, color="FF4500") for _ in range(8)]
tv_displays = [Object("Television", width=1.2, depth=0.1, height=0.7, support=MOUNTED, color="000080") for _ in range(2)]
gaming_console = Object("Gaming Console", width=0.15, depth=0.4, height=0.5, support=STANDING, color="32CD32")
security_camera = Object("Security Camera", width=0.1, depth=0.1, height=0.1, support=MOUNTED, color="4B0082")

# Storage and workspace
repair_desk = Object("Repair Desk", width=1.4, depth=0.7, height=0.8, support=STANDING, color="8B4513")
tool_cabinet = Object("Tool Cabinet", width=1.0, depth=0.5, height=1.8, support=STANDING, color="2F4F4F")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

back_door.max.x = scene.max.x - 0.2 * scene.width
back_door.max.y = scene.max.y
back_door.min.z = scene.min.z
back_door.facing = Y_MIN

windows[0].min.x = scene.min.x
windows[0].min.y = scene.min.y
windows[0].min.z = 0.5
windows[0].facing = X_MAX

windows[1].max.x = scene.max.x
windows[1].min.y = scene.min.y
windows[1].min.z = 0.5
windows[1].facing = X_MIN

# Wall shelves placement
wall_shelves[0].min.x = scene.min.x
wall_shelves[0].center.y = scene.min.y + 0.3 * scene.depth
wall_shelves[0].min.z = scene.min.z
wall_shelves[0].facing = X_MAX

wall_shelves[1].max.x = scene.max.x
wall_shelves[1].center.y = scene.min.y + 0.3 * scene.depth
wall_shelves[1].min.z = scene.min.z
wall_shelves[1].facing = X_MIN

wall_shelves[2].min.x = scene.min.x
wall_shelves[2].center.y = scene.min.y + 0.7 * scene.depth
wall_shelves[2].min.z = scene.min.z
wall_shelves[2].facing = X_MAX

wall_shelves[3].max.x = scene.max.x
wall_shelves[3].center.y = scene.min.y + 0.7 * scene.depth
wall_shelves[3].min.z = scene.min.z
wall_shelves[3].facing = X_MIN

# Display islands in center
display_islands[0].center.x = scene.min.x + 0.35 * scene.width
display_islands[0].center.y = scene.center.y
display_islands[0].min.z = scene.min.z
display_islands[0].facing = Y_MAX

display_islands[1].center.x = scene.min.x + 0.65 * scene.width
display_islands[1].center.y = scene.center.y
display_islands[1].min.z = scene.min.z
display_islands[1].facing = Y_MAX

# Counter area
counter.center.x = scene.center.x
counter.max.y = scene.max.y - 0.1
counter.min.z = scene.min.z
counter.facing = Y_MIN

set_coordinate_frame(counter)
register.center.x = counter.min.x + 0.25 * counter.width
register.center.y = counter.center.y
register.min.z = counter.max.z
register.facing = counter.facing
set_coordinate_frame(scene)

# Display items placement
for i, laptop in enumerate(laptops):
    if i < 3:
        set_coordinate_frame(display_islands[0])
        laptop.center.x = display_islands[0].min.x + (i+1.0)/4.0 * display_islands[0].width
        laptop.center.y = display_islands[0].center.y
    else:
        set_coordinate_frame(display_islands[1])
        laptop.center.x = display_islands[1].min.x + ((i-3)+1.0)/4.0 * display_islands[1].width
        laptop.center.y = display_islands[1].center.y
    laptop.min.z = display_islands[0].max.z
    laptop.facing = display_islands[0].facing
set_coordinate_frame(scene)

for i, phone in enumerate(smartphones):
    set_coordinate_frame(wall_shelves[i//4])
    phone.center.x = wall_shelves[i//4].min.x + (i%4+1.0)/5.0 * wall_shelves[i//4].width
    phone.center.y = wall_shelves[i//4].center.y
    phone.min.z = wall_shelves[i//4].max.z - 0.5
    phone.facing = wall_shelves[i//4].facing
set_coordinate_frame(scene)

for i, tv in enumerate(tv_displays):
    tv.center.x = scene.min.x + (i+1.0)/3.0 * scene.width
    tv.max.y = scene.max.y
    tv.min.z = 1.0
    tv.facing = Y_MIN

gaming_console.center.x = display_islands[1].center.x
gaming_console.center.y = display_islands[1].center.y
gaming_console.min.z = display_islands[1].max.z
gaming_console.facing = display_islands[1].facing

security_camera.max.x = scene.max.x - 0.1
security_camera.min.y = scene.min.y + 0.1
security_camera.max.z = scene.max.z - 0.1
security_camera.facing = Y_MAX

repair_desk.min.x = scene.min.x + 0.1
repair_desk.max.y = scene.max.y - 0.1
repair_desk.min.z = scene.min.z
repair_desk.facing = X_MAX

tool_cabinet.min.x = repair_desk.max.x + 0.1
tool_cabinet.max.y = scene.max.y - 0.1
tool_cabinet.min.z = scene.min.z
tool_cabinet.facing = X_MAX