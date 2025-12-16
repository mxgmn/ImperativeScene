set_title("Factory Floor")
set_size(width=15, depth=20, height=4)
set_floor_asset("Industrial Concrete Floor", color="787878")
set_wall_asset("Metal Panel Wall", interior=True, color="9BA1A8")

loading_door = Door("Industrial Sliding Door", width=3.0, depth=0.2, height=3.0, color="4A4A4A")
personnel_door = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="708090")
windows = [Window("Industrial Window", width=1.5, depth=0.1, height=1.2, color="A5C5E8") for _ in range(4)]

# Main production line
conveyor_belts = [Object("Conveyor Belt", width=1.0, depth=4.0, height=0.8, support=STANDING, color="FFA500") for _ in range(3)]
robotic_arms = [Object("Industrial Robot", width=1.2, depth=1.2, height=2.0, support=STANDING, color="1E90FF") for _ in range(3)]
control_panels = [Object("Control Panel", width=0.8, depth=0.4, height=1.5, support=STANDING, color="4682B4") for _ in range(3)]

# Storage and equipment
storage_racks = [Object("Storage Rack", width=2.5, depth=0.8, height=3.0, support=STANDING, color="CD853F") for _ in range(3)]
pallets = [Object("Wooden Pallet", width=1.2, depth=0.8, height=0.15, support=STANDING, color="8B4513") for _ in range(6)]
forklift = Object("Forklift", width=1.2, depth=2.4, height=2.0, support=STANDING, color="FFD700")

# Work areas
workbenches = [Object("Industrial Workbench", width=1.8, depth=0.8, height=0.9, support=STANDING, color="2F4F4F") for _ in range(2)]
tool_cabinets = [Object("Tool Cabinet", width=1.0, depth=0.5, height=1.8, support=STANDING, color="B22222") for _ in range(2)]

# Safety equipment
first_aid = Object("First Aid Station", width=0.6, depth=0.2, height=0.6, support=MOUNTED, color="FF0000")
safety_station = Object("Safety Equipment Station", width=1.0, depth=0.3, height=1.8, support=MOUNTED, color="32CD32")

# Waste management
waste_bins = [Object("Industrial Bin", width=0.8, depth=0.8, height=1.0, support=STANDING, color="808080") for _ in range(3)]