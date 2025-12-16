set_title("Data Center")
set_size(width=12, depth=8, height=3)
set_floor_asset("Raised Floor Tiles", color="7A8B8B")
set_wall_asset("Industrial Wall", interior=True, color="B8B8B8")

security_door = Door("Security Door", width=1.2, depth=0.15, height=2.2, color="4682B4")
emergency_exit = Door("Emergency Door", width=0.9, depth=0.15, height=2.2, color="B22222")

# Main server racks - the core of the data center
server_racks = [Object("Server Rack", width=0.6, depth=1.0, height=2.0, support=STANDING, color="2F4F4F") for _ in range(12)]

# Network equipment cabinets
network_cabinets = [Object("Network Cabinet", width=0.8, depth=0.6, height=1.8, support=STANDING, color="4682B4") for _ in range(3)]

# Cooling infrastructure
ac_units = [Object("AC Unit", width=1.2, depth=0.6, height=2.0, support=STANDING, color="87CEEB") for _ in range(4)]

# Power distribution
power_units = [Object("Power Distribution Unit", width=0.5, depth=0.4, height=1.8, support=STANDING, color="CD853F") for _ in range(2)]

# Monitoring station
monitoring_desk = Object("Computer Desk", width=2.8, depth=0.8, height=0.75, support=STANDING, color="A0522D")
office_chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="4B0082") for _ in range(2)]
monitors = [Object("Monitor", width=0.6, depth=0.1, height=0.4, support=STANDING, color="1E90FF") for _ in range(2)]

# Fire suppression system
fire_suppression = [Object("Fire Suppression Unit", width=0.4, depth=0.4, height=0.8, support=MOUNTED, color="FF4500") for _ in range(4)]

# Security equipment
security_cameras = [Object("Security Camera", width=0.2, depth=0.2, height=0.2, support=MOUNTED, color="483D8B") for _ in range(4)]
card_reader = Object("Card Reader", width=0.15, depth=0.1, height=0.2, support=MOUNTED, color="32CD32")

security_door.max.x = scene.max.x
security_door.center.y = scene.min.y + 0.2 * scene.depth
security_door.min.z = scene.min.z
security_door.facing = X_MIN

emergency_exit.min.x = scene.min.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MAX

# Server racks in two rows
rack_spacing = 0.4
for i, rack in enumerate(server_racks):
    if i < 6:  # First row
        rack.center.x = scene.min.x + (i+1.0) / 7.0 * scene.width
        rack.center.y = scene.min.y + 0.35 * scene.depth
    else:  # Second row
        rack.center.x = scene.min.x + ((i-6)+1.0) / 7.0 * scene.width
        rack.center.y = scene.min.y + 0.65 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = Y_MAX

# Network cabinets along the wall
for i, cabinet in enumerate(network_cabinets):
    cabinet.max.x = scene.max.x - 0.2
    cabinet.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    cabinet.min.z = scene.min.z
    cabinet.facing = X_MIN

# AC units in corners and middle
for i, ac in enumerate(ac_units):
    if i < 2:
        ac.min.x = scene.min.x
        ac.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    else:
        ac.max.x = scene.max.x
        ac.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
    ac.min.z = scene.min.z
    ac.facing = X_MAX if i < 2 else X_MIN

# Power distribution units
for i, pdu in enumerate(power_units):
    pdu.min.x = scene.min.x + 0.2
    pdu.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    pdu.min.z = scene.min.z
    pdu.facing = X_MAX

# Monitoring station
monitoring_desk.center.x = scene.max.x - 0.2 * scene.width
monitoring_desk.max.y = scene.max.y - 0.1
monitoring_desk.min.z = scene.min.z
monitoring_desk.facing = Y_MIN

set_coordinate_frame(monitoring_desk)
for i, chair in enumerate(office_chairs):
    chair.center.x = monitoring_desk.min.x + (i+1.0) / 3.0 * monitoring_desk.width
    chair.min.y = monitoring_desk.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = monitoring_desk

for i, monitor in enumerate(monitors):
    monitor.center.x = monitoring_desk.min.x + (i+1.0) / 3.0 * monitoring_desk.width
    monitor.center.y = monitoring_desk.center.y
    monitor.min.z = monitoring_desk.max.z
    monitor.facing = monitoring_desk.facing
set_coordinate_frame(scene)

# Fire suppression units in corners
for i, unit in enumerate(fire_suppression):
    if i % 2 == 0:
        unit.min.x = scene.min.x + 0.1
    else:
        unit.max.x = scene.max.x - 0.1
    unit.center.y = scene.min.y + (0.25 if i < 2 else 0.75) * scene.depth
    unit.max.z = scene.max.z - 0.1
    unit.facing = Y_MIN

# Security cameras in corners
for i, camera in enumerate(security_cameras):
    if i % 2 == 0:
        camera.min.x = scene.min.x + 0.1
    else:
        camera.max.x = scene.max.x - 0.1
    camera.center.y = scene.min.y + (0.2 if i < 2 else 0.8) * scene.depth
    camera.max.z = scene.max.z - 0.1
    camera.facing = Y_MIN if i < 2 else Y_MAX

# Card reader next to security door
set_coordinate_frame(security_door)
card_reader.min.x = security_door.min.x - 0.2
card_reader.center.y = security_door.center.y
card_reader.min.z = 1.2
card_reader.facing = security_door.facing