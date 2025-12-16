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