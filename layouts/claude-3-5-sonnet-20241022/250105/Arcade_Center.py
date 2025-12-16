set_title("Arcade Center")
set_size(width=15, depth=12, height=3)
set_floor_asset("Neon Pattern Carpet", color="1A1A2E")
set_wall_asset("Painted Wall", interior=True, color="2E1A3D")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="4169E1")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="B22222")
windows = [Window("Window", width=2.0, depth=0.1, height=1.5, color="4B0082") for _ in range(3)]

arcade_machines = [
    Object("Racing Arcade Machine", width=1.2, depth=1.8, height=1.8, support=STANDING, color="FF4500"),
    Object("Fighting Arcade Machine", width=0.8, depth=0.9, height=1.8, support=STANDING, color="32CD32"),
    Object("Shooting Arcade Machine", width=1.4, depth=1.2, height=1.8, support=STANDING, color="FFD700"),
    Object("Dancing Arcade Machine", width=1.8, depth=1.8, height=0.3, support=STANDING, color="FF69B4"),
    Object("Classic Arcade Machine", width=0.7, depth=0.8, height=1.8, support=STANDING, color="4169E1"),
    Object("Pinball Machine", width=0.8, depth=1.6, height=1.2, support=STANDING, color="9932CC")
]

# Multiple instances of classic arcade machines
classic_machines = [Object("Classic Arcade Machine", width=0.7, depth=0.8, height=1.8, support=STANDING, color=color) 
                   for color in ["FF6B6B", "4ECDC4", "45B7D1", "96CEB4"]]

counter = Object("Service Counter", width=3.0, depth=0.8, height=1.1, support=STANDING, color="483D8B")
prize_display = Object("Prize Display Case", width=2.0, depth=0.4, height=1.8, support=STANDING, color="9370DB")
benches = [Object("Bench", width=1.2, depth=0.4, height=0.5, support=STANDING, color="4B0082") for _ in range(3)]
vending_machines = [Object("Vending Machine", width=1.0, depth=0.8, height=2.0, support=STANDING, color="E6399B") for _ in range(2)]
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.6, support=STANDING, color="708090") for _ in range(3)]

# Decorative elements
neon_signs = [Object("Neon Sign", width=1.2, depth=0.1, height=0.6, support=MOUNTED, color=color) 
              for color in ["FF1493", "00FF7F", "FF4500"]]

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x - 0.2 * scene.width
emergency_exit.max.y = scene.max.y
emergency_exit.min.z = scene.min.z
emergency_exit.facing = Y_MIN

spacing = 0.25 * scene.width
for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i + 1.0) * spacing
    window.min.y = scene.min.y
    window.min.z = 1.0
    window.facing = Y_MAX

# Main arcade machines layout
arcade_machines[0].min.x = scene.min.x + 0.1  # Racing
arcade_machines[0].center.y = scene.center.y
arcade_machines[0].min.z = scene.min.z
arcade_machines[0].facing = X_MAX

arcade_machines[1].center.x = scene.center.x - 0.2 * scene.width  # Fighting
arcade_machines[1].max.y = scene.max.y - 0.1
arcade_machines[1].min.z = scene.min.z
arcade_machines[1].facing = Y_MIN

arcade_machines[2].max.x = scene.max.x - 0.1  # Shooting
arcade_machines[2].center.y = scene.center.y
arcade_machines[2].min.z = scene.min.z
arcade_machines[2].facing = X_MIN

arcade_machines[3].center.x = scene.center.x + 0.2 * scene.width  # Dancing
arcade_machines[3].center.y = scene.center.y
arcade_machines[3].min.z = scene.min.z
arcade_machines[3].facing = Y_MIN

# Classic machines in a row
spacing = 0.15 * scene.width
for i, machine in enumerate(classic_machines):
    machine.center.x = scene.min.x + (i + 1.0) * spacing
    machine.min.y = scene.min.y + 0.2 * scene.depth
    machine.min.z = scene.min.z
    machine.facing = Y_MAX

counter.max.x = scene.max.x - 0.1
counter.min.y = scene.min.y + 0.15 * scene.depth
counter.min.z = scene.min.z
counter.facing = X_MIN

prize_display.max.x = scene.max.x - 0.1
prize_display.min.y = counter.max.y + 0.1
prize_display.min.z = scene.min.z
prize_display.facing = X_MIN

# Benches spread around
spacing = 0.2 * scene.width
for i, bench in enumerate(benches):
    bench.center.x = scene.center.x + (i - 1.0) * spacing
    bench.center.y = scene.center.y
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

# Vending machines
for i, machine in enumerate(vending_machines):
    machine.max.x = scene.max.x - 0.1
    machine.center.y = scene.min.y + (i + 1.0) * 0.3 * scene.depth
    machine.min.z = scene.min.z
    machine.facing = X_MIN

# Trash bins at strategic locations
spacing = 0.4 * scene.width
for i, bin in enumerate(trash_bins):
    bin.center.x = scene.min.x + (i + 1.0) * spacing
    bin.min.y = scene.min.y + 0.1
    bin.min.z = scene.min.z
    bin.facing = Y_MAX

# Neon signs on walls
for i, sign in enumerate(neon_signs):
    sign.center.x = scene.min.x + (i + 1.0) * 0.25 * scene.width
    sign.max.y = scene.max.y
    sign.min.z = 2.0
    sign.facing = Y_MIN

arcade_machines[4].center.x = scene.center.x  # Classic
arcade_machines[4].min.y = scene.min.y + 0.4 * scene.depth
arcade_machines[4].min.z = scene.min.z
arcade_machines[4].facing = Y_MAX

arcade_machines[5].center.x = scene.center.x - 0.15 * scene.width  # Pinball
arcade_machines[5].center.y = scene.center.y - 0.2 * scene.depth
arcade_machines[5].min.z = scene.min.z
arcade_machines[5].facing = Y_MAX