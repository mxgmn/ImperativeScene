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

loading_door.center.x = scene.min.x + 0.3 * scene.width
loading_door.min.y = scene.min.y
loading_door.min.z = scene.min.z
loading_door.facing = Y_MAX

personnel_door.max.x = scene.max.x
personnel_door.max.y = scene.max.y - 0.2 * scene.depth
personnel_door.min.z = scene.min.z
personnel_door.facing = X_MIN

for i, window in enumerate(windows):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    window.min.z = 2.0
    window.facing = X_MAX

# Production line setup
for i, conveyor in enumerate(conveyor_belts):
    conveyor.center.x = scene.min.x + 0.4 * scene.width
    conveyor.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    conveyor.min.z = scene.min.z
    conveyor.facing = Y_MAX

for i, robot in enumerate(robotic_arms):
    robot.min.x = conveyor_belts[i].max.x + 0.5
    robot.center.y = conveyor_belts[i].center.y
    robot.min.z = scene.min.z
    robot.facing = conveyor_belts[i]

for i, panel in enumerate(control_panels):
    panel.min.x = robotic_arms[i].max.x + 0.5
    panel.center.y = robotic_arms[i].center.y
    panel.min.z = scene.min.z
    panel.facing = robotic_arms[i]

# Storage area setup
for i, rack in enumerate(storage_racks):
    rack.max.x = scene.max.x - 0.2
    rack.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = X_MIN

for i, pallet in enumerate(pallets):
    if i < 3:
        pallet.min.x = storage_racks[i].min.x - 1.5
    else:
        pallet.min.x = storage_racks[i-3].min.x - 3.0
    pallet.center.y = storage_racks[i % 3].center.y
    pallet.min.z = scene.min.z
    pallet.facing = storage_racks[0].facing

forklift.center.x = scene.min.x + 0.7 * scene.width
forklift.center.y = scene.min.y + 0.3 * scene.depth
forklift.min.z = scene.min.z
forklift.facing = Y_MAX

# Work area setup
for i, bench in enumerate(workbenches):
    bench.min.x = scene.min.x + 0.2
    bench.center.y = scene.max.y - (i+1.0) / 3.0 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = X_MAX

for i, cabinet in enumerate(tool_cabinets):
    cabinet.min.x = workbenches[i].max.x + 0.5
    cabinet.center.y = workbenches[i].center.y
    cabinet.min.z = scene.min.z
    cabinet.facing = workbenches[i].facing

# Safety equipment placement
first_aid.max.x = scene.max.x
first_aid.center.y = scene.min.y + 0.3 * scene.depth
first_aid.min.z = 1.2
first_aid.facing = X_MIN

safety_station.max.x = scene.max.x
safety_station.center.y = scene.min.y + 0.6 * scene.depth
safety_station.min.z = scene.min.z
safety_station.facing = X_MIN

# Waste management setup
for i, bin in enumerate(waste_bins):
    bin.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    bin.min.y = scene.min.y + 0.2
    bin.min.z = scene.min.z
    bin.facing = Y_MAX