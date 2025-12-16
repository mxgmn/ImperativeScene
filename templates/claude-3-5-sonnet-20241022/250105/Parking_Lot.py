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