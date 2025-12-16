set_title("Parking Lot")
set_size(width=24, depth=20, height=3)
set_floor_asset("Asphalt Floor", color="2F4F4F")
set_wall_asset("Concrete Wall", interior=False, color="808080")

# Main entrance/exit
gate = Door("Barrier Gate", width=3.0, depth=0.1, height=1.0, color="FF4500")

# Parked vehicles (varied sizes for different vehicle types)
cars = [Object("Car", width=1.8, depth=4.2, height=1.4, support=STANDING, color="4682B4") for _ in range(6)]
suvs = [Object("SUV", width=2.0, depth=4.8, height=1.7, support=STANDING, color="2E8B57") for _ in range(3)]
vans = [Object("Van", width=2.2, depth=5.2, height=2.0, support=STANDING, color="CD853F") for _ in range(2)]

# Infrastructure
ticket_machine = Object("Parking Meter", width=0.3, depth=0.3, height=1.2, support=STANDING, color="FFD700")
light_poles = [Object("Light Pole", width=0.3, depth=0.3, height=2.8, support=STANDING, color="FFA500") for _ in range(4)]
trash_bins = [Object("Trash Bin", width=0.5, depth=0.5, height=0.8, support=STANDING, color="8B0000") for _ in range(2)]

# Safety and guidance
signs = [Object("Parking Sign", width=0.4, depth=0.1, height=1.8, support=STANDING, color="4169E1") for _ in range(3)]
bollards = [Object("Bollard", width=0.2, depth=0.2, height=0.9, support=STANDING, color="B8860B") for _ in range(8)]

# Greenery (around the edges)
trees = [Object("Tree", width=2.0, depth=2.0, height=2.8, support=STANDING, color="228B22") for _ in range(4)]
bushes = [Object("Bush", width=1.0, depth=1.0, height=0.8, support=STANDING, color="32CD32") for _ in range(6)]

gate.center.x = scene.min.x + 0.25 * scene.width
gate.min.y = scene.min.y
gate.min.z = scene.min.z
gate.facing = Y_MAX

# Arrange cars in two rows
parking_angle = 0.2 # slight angle for diagonal parking
for i, car in enumerate(cars):
    row = i // 3
    col = i % 3
    car.center.x = scene.min.x + (col + 1.0) / 4.0 * scene.width
    if row == 0:
        car.center.y = scene.min.y + 0.3 * scene.depth
    else:
        car.center.y = scene.min.y + 0.6 * scene.depth
    car.min.z = scene.min.z
    car.facing = Y_MIN

# SUVs in a row
for i, suv in enumerate(suvs):
    suv.center.x = scene.max.x - (i + 1.0) / 4.0 * scene.width
    suv.center.y = scene.max.y - 0.3 * scene.depth
    suv.min.z = scene.min.z
    suv.facing = Y_MAX

# Vans at the back
for i, van in enumerate(vans):
    van.center.x = scene.min.x + (i + 1.0) / 3.0 * scene.width
    van.max.y = scene.max.y
    van.min.z = scene.min.z
    van.facing = Y_MIN

ticket_machine.min.x = gate.max.x + 0.5
ticket_machine.min.y = scene.min.y
ticket_machine.min.z = scene.min.z
ticket_machine.facing = Y_MAX

# Light poles at corners
corner_offset = 0.1
for i, pole in enumerate(light_poles):
    if i % 2 == 0:
        pole.min.x = scene.min.x + corner_offset
    else:
        pole.max.x = scene.max.x - corner_offset
    if i < 2:
        pole.min.y = scene.min.y + corner_offset
    else:
        pole.max.y = scene.max.y - corner_offset
    pole.min.z = scene.min.z
    pole.facing = Y_MAX

# Trash bins near entrance and back
for i, bin in enumerate(trash_bins):
    bin.min.x = scene.min.x + (i + 1.0) / 3.0 * scene.width
    if i == 0:
        bin.min.y = scene.min.y + 0.1
    else:
        bin.max.y = scene.max.y - 0.1
    bin.min.z = scene.min.z
    bin.facing = Y_MAX

# Signs distributed across the lot
for i, sign in enumerate(signs):
    sign.center.x = scene.min.x + (i + 1.0) / 4.0 * scene.width
    sign.center.y = scene.center.y
    sign.min.z = scene.min.z
    sign.facing = Y_MAX

# Bollards along entrance
bollard_spacing = 0.15
for i, bollard in enumerate(bollards):
    if i < 4:
        bollard.center.x = gate.min.x + (i + 1.0) / 5.0 * gate.width
        bollard.min.y = gate.min.y - bollard_spacing
    else:
        bollard.center.x = gate.min.x + (i - 3.0) / 5.0 * gate.width
        bollard.max.y = gate.max.y + bollard_spacing
    bollard.min.z = scene.min.z
    bollard.facing = Y_MAX

# Trees in corners
for i, tree in enumerate(trees):
    if i % 2 == 0:
        tree.min.x = scene.min.x
    else:
        tree.max.x = scene.max.x
    if i < 2:
        tree.min.y = scene.min.y
    else:
        tree.max.y = scene.max.y
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Bushes along sides
for i, bush in enumerate(bushes):
    if i < 3:
        bush.min.x = scene.min.x
        bush.center.y = scene.min.y + (i + 1.0) / 4.0 * scene.depth
    else:
        bush.max.x = scene.max.x
        bush.center.y = scene.min.y + (i - 2.0) / 4.0 * scene.depth
    bush.min.z = scene.min.z
    bush.facing = Y_MAX