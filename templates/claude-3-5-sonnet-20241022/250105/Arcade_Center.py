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