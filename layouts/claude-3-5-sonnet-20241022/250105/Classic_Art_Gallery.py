set_title("Classic Art Gallery")
set_size(width=15, depth=12, height=3.5)
set_floor_asset("Marble Floor", color="E8E6E1")
set_wall_asset("Smooth Wall", interior=True, color="F5F5F5")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(3)]

# Main artwork displays
paintings = [
    Object("Large Painting", width=2.0, depth=0.1, height=1.5, support=MOUNTED, color="B22222"),
    Object("Large Painting", width=1.8, depth=0.1, height=1.4, support=MOUNTED, color="4B0082"),
    Object("Large Painting", width=2.0, depth=0.1, height=1.5, support=MOUNTED, color="84B222"),
    Object("Large Painting", width=1.8, depth=0.1, height=1.4, support=MOUNTED, color="005782"),
    Object("Medium Painting", width=1.5, depth=0.1, height=1.2, support=MOUNTED, color="006400"),
    Object("Medium Painting", width=1.4, depth=0.1, height=1.1, support=MOUNTED, color="CD853F"),
    Object("Small Painting", width=1.0, depth=0.1, height=0.8, support=MOUNTED, color="4682B4"),
    Object("Small Painting", width=0.9, depth=0.1, height=0.7, support=MOUNTED, color="DAA520")
]

# Sculptures and pedestals
pedestals = [Object("Display Pedestal", width=0.6, depth=0.6, height=1.0, support=STANDING, color="D3D3D3") for _ in range(4)]
sculptures = [
    Object("Classical Sculpture", width=0.4, depth=0.4, height=0.8, support=STANDING, color="F0F8FF"),
    Object("Modern Sculpture", width=0.5, depth=0.5, height=1.2, support=STANDING, color="FFD700"),
    Object("Abstract Sculpture", width=0.6, depth=0.6, height=0.9, support=STANDING, color="FF4500"),
    Object("Bronze Statue", width=0.4, depth=0.4, height=1.0, support=STANDING, color="CD853F")
]

# Furniture and amenities
benches = [Object("Gallery Bench", width=1.2, depth=0.4, height=0.45, support=STANDING, color="8B4513") for _ in range(3)]
information_desk = Object("Reception Desk", width=2.0, depth=0.8, height=1.0, support=STANDING, color="A0522D")
brochure_stand = Object("Brochure Stand", width=0.4, depth=0.3, height=1.2, support=STANDING, color="4682B4")
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(4)]

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x - 0.2 * scene.width
emergency_exit.max.y = scene.max.y
emergency_exit.min.z = scene.min.z
emergency_exit.facing = Y_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

# Left wall paintings
for i in range(4):
    paintings[i].min.x = scene.min.x
    paintings[i].center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    paintings[i].min.z = 1.0
    paintings[i].facing = X_MAX

# Right wall paintings
for i in range(4, 8):
    paintings[i].max.x = scene.max.x
    paintings[i].center.y = scene.min.y + (i-3.0) / 5.0 * scene.depth
    paintings[i].min.z = 1.0
    paintings[i].facing = X_MIN

# Pedestals and sculptures in center area
param = 0.25
positions = [(param, param), (-param, param), (param, -param), (-param, -param)]
for i, (pedestal, sculpture) in enumerate(zip(pedestals, sculptures)):
    pedestal.center.x = scene.center.x + positions[i][0] * scene.width
    pedestal.center.y = scene.center.y + positions[i][1] * scene.depth
    pedestal.min.z = scene.min.z
    pedestal.facing = Y_MAX
    
    sculpture.center.x = pedestal.center.x
    sculpture.center.y = pedestal.center.y
    sculpture.min.z = pedestal.max.z
    sculpture.facing = pedestal.facing

# Benches
for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    bench.center.y = scene.center.y
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

information_desk.min.x = scene.min.x + 0.1
information_desk.min.y = scene.min.y + 0.1
information_desk.min.z = scene.min.z
information_desk.facing = X_MAX

brochure_stand.min.x = information_desk.max.x + 0.1
brochure_stand.center.y = information_desk.center.y
brochure_stand.min.z = scene.min.z
brochure_stand.facing = information_desk.facing

# Corner plants
positions = [(1.0, 1.0), (-1.0, 1.0), (1.0, -1.0), (-1.0, -1.0)]
margin = 0.1
for i, plant in enumerate(plants):
    plant.center.x = scene.center.x + positions[i][0] * (scene.width/2.0 - margin)
    plant.center.y = scene.center.y + positions[i][1] * (scene.depth/2.0 - margin)
    plant.min.z = scene.min.z
    plant.facing = Y_MAX