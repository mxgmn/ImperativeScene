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