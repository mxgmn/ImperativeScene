set_title("Modern Open-Plan Office")
set_size(width=15, depth=12, height=3)
set_floor_asset("Commercial Carpet Floor", color="7B8B8E")
set_wall_asset("Modern Wall", interior=True, color="E5E5E5")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
windows = [Object("Window Panel", width=2.0, depth=0.1, height=2.0, support=MOUNTED, color="ADD8E6") for _ in range(4)]

# Main work areas
desks = [Object("Office Desk", width=1.4, depth=0.8, height=0.75, support=STANDING, color="F5F5F5") for _ in range(8)]
chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.1, support=STANDING, color="4682B4") for _ in range(8)]
computers = [Object("Computer Monitor", width=0.6, depth=0.2, height=0.4, support=STANDING, color="2F4F4F") for _ in range(8)]

# Collaborative area
meeting_table = Object("Conference Table", width=2.4, depth=1.2, height=0.75, support=STANDING, color="B8860B")
meeting_chairs = [Object("Meeting Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="4682B4") for _ in range(6)]

# Storage and organization
filing_cabinets = [Object("Filing Cabinet", width=0.5, depth=0.6, height=1.3, support=STANDING, color="708090") for _ in range(3)]
bookshelf = Object("Bookshelf", width=1.8, depth=0.4, height=1.8, support=STANDING, color="8B4513")

# Break area
kitchenette = Object("Kitchen Counter", width=2.0, depth=0.6, height=0.9, support=STANDING, color="DCDCDC")
water_cooler = Object("Water Dispenser", width=0.4, depth=0.4, height=1.2, support=STANDING, color="87CEEB")
coffee_machine = Object("Coffee Machine", width=0.4, depth=0.3, height=0.35, support=STANDING, color="CD853F")

# Plants for better atmosphere
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=1.2, support=STANDING, color="228B22") for _ in range(4)]

# Presentation area
whiteboard = Object("Whiteboard", width=2.0, depth=0.05, height=1.2, support=MOUNTED, color="FFFFFF")

entrance.max.x = scene.max.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

# Arrange desks in two rows of four
for i, desk in enumerate(desks):
    row = i // 4
    col = i % 4
    desk.center.x = scene.min.x + (col+1.0) / 5.0 * scene.width
    desk.center.y = scene.min.y + (row+1.0) / 3.0 * scene.depth
    desk.min.z = scene.min.z
    desk.facing = Y_MAX

    # Place chair and computer for each desk
    set_coordinate_frame(desk)
    chairs[i].center.x = desk.center.x
    chairs[i].min.y = desk.max.y + 0.1
    chairs[i].min.z = scene.min.z
    chairs[i].facing = desk
    
    computers[i].center.x = desk.center.x
    computers[i].center.y = desk.center.y
    computers[i].min.z = desk.max.z
    computers[i].facing = desk.facing
set_coordinate_frame(scene)

# Meeting area in the corner
meeting_table.max.x = scene.max.x - 0.3
meeting_table.max.y = scene.max.y - 0.3
meeting_table.min.z = scene.min.z
meeting_table.facing = Y_MIN

set_coordinate_frame(meeting_table)
for i, chair in enumerate(meeting_chairs):
    if i < 3:  # chairs on one side
        chair.center.x = meeting_table.min.x + (i+1.0) / 4.0 * meeting_table.width
        chair.min.y = meeting_table.min.y - 0.2
    else:  # chairs on the other side
        chair.center.x = meeting_table.min.x + ((i-3)+1.0) / 4.0 * meeting_table.width
        chair.max.y = meeting_table.max.y + 0.2
    chair.min.z = scene.min.z
    chair.facing = meeting_table
set_coordinate_frame(scene)

# Storage area
for i, cabinet in enumerate(filing_cabinets):
    cabinet.min.x = scene.min.x
    cabinet.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    cabinet.min.z = scene.min.z
    cabinet.facing = X_MAX

bookshelf.min.x = scene.min.x
bookshelf.max.y = scene.max.y
bookshelf.min.z = scene.min.z
bookshelf.facing = X_MAX

# Break area
kitchenette.max.x = scene.max.x
kitchenette.min.y = scene.min.y
kitchenette.min.z = scene.min.z
kitchenette.facing = X_MIN

set_coordinate_frame(kitchenette)
water_cooler.min.x = kitchenette.min.x
water_cooler.center.y = kitchenette.center.y
water_cooler.min.z = kitchenette.max.z
water_cooler.facing = kitchenette.facing

coffee_machine.center.x = kitchenette.center.x
coffee_machine.center.y = kitchenette.center.y
coffee_machine.min.z = kitchenette.max.z
coffee_machine.facing = kitchenette.facing
set_coordinate_frame(scene)

# Plants distributed around the space
for i, plant in enumerate(plants):
    if i == 0:
        plant.min.x = scene.min.x + 0.2
        plant.min.y = scene.min.y + 0.2
    elif i == 1:
        plant.max.x = scene.max.x - 0.2
        plant.min.y = scene.min.y + 0.2
    elif i == 2:
        plant.min.x = scene.min.x + 0.2
        plant.max.y = scene.max.y - 0.2
    else:
        plant.max.x = scene.max.x - 0.2
        plant.max.y = scene.max.y - 0.2
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

# Presentation area
whiteboard.max.x = scene.max.x - 0.3
whiteboard.center.y = scene.max.y - 0.3
whiteboard.min.z = 1.0
whiteboard.facing = X_MIN