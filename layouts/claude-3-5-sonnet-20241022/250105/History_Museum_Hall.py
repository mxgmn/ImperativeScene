set_title("History Museum Hall")
set_size(width=15, depth=20, height=4)
set_floor_asset("Marble Floor", color="E8E6E1")
set_wall_asset("Painted Wall", interior=True, color="EAE6DD")

entrance = Door("Double Glass Door", width=2.0, depth=0.1, height=2.4, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Tall Window", width=1.5, depth=0.1, height=2.5, color="B0E0E6") for _ in range(4)]

# Main exhibits
dinosaur = Object("Dinosaur Skeleton", width=4.0, depth=8.0, height=3.5, support=STANDING, color="E3DAC9")
mammoth = Object("Mammoth Skeleton", width=3.0, depth=5.0, height=3.0, support=STANDING, color="DED5C4")

# Display cases
artifact_cases = [Object("Glass Display Case", width=1.2, depth=0.8, height=1.2, support=STANDING, color="87CEFA") for _ in range(6)]
weapon_cases = [Object("Long Display Case", width=2.0, depth=0.6, height=1.0, support=STANDING, color="87CEFA") for _ in range(3)]

# Information displays
info_panels = [Object("Information Panel", width=0.8, depth=0.1, height=1.5, support=MOUNTED, color="4682B4") for _ in range(8)]

# Seating and rest areas
benches = [Object("Museum Bench", width=1.8, depth=0.5, height=0.45, support=STANDING, color="8B4513") for _ in range(4)]

# Interactive elements
touchscreens = [Object("Interactive Display", width=0.6, depth=0.1, height=1.2, support=MOUNTED, color="4169E1") for _ in range(3)]

# Decorative elements
columns = [Object("Decorative Column", width=0.8, depth=0.8, height=3.8, support=STANDING, color="F5F5DC") for _ in range(6)]
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(4)]

# Security
security_desk = Object("Security Desk", width=2.0, depth=0.8, height=1.1, support=STANDING, color="A0522D")
barrier_ropes = [Object("Barrier Post", width=0.1, depth=0.1, height=0.9, support=STANDING, color="B8860B") for _ in range(8)]

entrance.center.x = scene.center.x
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

for i, window in enumerate(windows):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    window.min.z = 0.8
    window.facing = X_MAX

dinosaur.center.x = scene.center.x - 0.2 * scene.width
dinosaur.center.y = scene.center.y + 0.1 * scene.depth
dinosaur.min.z = scene.min.z
dinosaur.facing = Y_MIN

mammoth.center.x = scene.center.x + 0.2 * scene.width
mammoth.center.y = scene.center.y - 0.2 * scene.depth
mammoth.min.z = scene.min.z
mammoth.facing = Y_MAX

spacing = 0.2 * scene.width
for i, case in enumerate(artifact_cases):
    if i < 3:
        case.center.x = scene.min.x + (i+1.0) * spacing
    else:
        case.center.x = scene.max.x - (i-2.0) * spacing
    case.max.y = scene.max.y - 0.1 * scene.depth
    case.min.z = scene.min.z
    case.facing = Y_MIN

for i, case in enumerate(weapon_cases):
    case.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    case.min.y = scene.min.y + 0.15 * scene.depth
    case.min.z = scene.min.z
    case.facing = Y_MAX

for i, panel in enumerate(info_panels):
    if i < 4:
        panel.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    else:
        panel.center.x = scene.max.x - (i-3.0) / 5.0 * scene.width
    panel.center.y = scene.center.y
    panel.min.z = 0.1
    panel.facing = Y_MIN

bench_spacing = 0.15 * scene.depth
for i, bench in enumerate(benches):
    bench.center.x = scene.center.x
    bench.center.y = scene.min.y + (i+1.0) * bench_spacing
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

for i, screen in enumerate(touchscreens):
    screen.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    screen.max.y = scene.max.y
    screen.min.z = 0.8
    screen.facing = Y_MIN

column_spacing = 0.2 * scene.width
for i, column in enumerate(columns):
    if i < 3:
        column.center.x = scene.min.x + (i+1.0) * column_spacing
    else:
        column.center.x = scene.max.x - (i-2.0) * column_spacing
    column.center.y = scene.center.y
    column.min.z = scene.min.z
    column.facing = Y_MIN

plant_spacing = 0.25 * scene.depth
for i, plant in enumerate(plants):
    if i < 2:
        plant.min.x = scene.min.x + 0.1
    else:
        plant.max.x = scene.max.x - 0.1
    plant.center.y = scene.min.y + (i%2+1.0) * plant_spacing
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

security_desk.min.x = scene.min.x + 0.1
security_desk.min.y = scene.min.y + 0.15 * scene.depth
security_desk.min.z = scene.min.z
security_desk.facing = X_MAX

barrier_spacing = 0.15 * scene.width
for i, barrier in enumerate(barrier_ropes):
    if i < 4:
        barrier.center.x = dinosaur.min.x + (i+1.0) * barrier_spacing
        barrier.center.y = dinosaur.min.y - 0.5
    else:
        barrier.center.x = mammoth.min.x + (i-3.0) * barrier_spacing
        barrier.center.y = mammoth.min.y - 0.5
    barrier.min.z = scene.min.z
    barrier.facing = Y_MAX