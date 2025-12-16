set_title("Arena Showdown")
set_size(width=30, depth=30, height=6)
set_floor_asset("Metal Floor", color="2F4F4F")
set_wall_asset("Industrial Wall", interior=True, color="4A4A4A")

# Main structural elements
platforms = [
    Object("Platform", width=6.0, depth=6.0, height=2.0, support=STANDING, color="696969"),
    Object("Platform", width=4.0, depth=4.0, height=1.0, support=STANDING, color="696969"),
    Object("Platform", width=5.0, depth=5.0, height=1.5, support=STANDING, color="696969")
]

barriers = [Object("Barrier Block", width=2.0, depth=0.3, height=1.2, support=STANDING, color="CD853F") for _ in range(8)]

# Cover objects
crates = [Object("Metal Crate", width=1.2, depth=1.2, height=1.2, support=STANDING, color="B8860B") for _ in range(6)]
containers = [Object("Shipping Container", width=2.4, depth=6.0, height=2.4, support=STANDING, color="8B0000") for _ in range(4)]

# Strategic points
sniper_nests = [Object("Sniper Platform", width=2.0, depth=2.0, height=3.0, support=STANDING, color="2F4F4F") for _ in range(2)]

# Power-up locations
weapon_stands = [Object("Weapon Stand", width=0.8, depth=0.8, height=1.0, support=STANDING, color="4169E1") for _ in range(4)]
health_stations = [Object("Health Station", width=0.8, depth=0.8, height=1.6, support=STANDING, color="32CD32") for _ in range(2)]
armor_stations = [Object("Armor Station", width=0.8, depth=0.8, height=1.6, support=STANDING, color="FFD700") for _ in range(2)]

# Aesthetic elements
pipes = [Object("Industrial Pipe", width=0.4, depth=3.0, height=0.4, support=MOUNTED, color="B87333") for _ in range(6)]
warning_signs = [Object("Warning Sign", width=0.6, depth=0.05, height=0.6, support=MOUNTED, color="FFD700") for _ in range(4)]

# Entry/Exit points
doors = [Door("Sliding Door", width=1.5, depth=0.2, height=2.2, color="4682B4") for _ in range(4)]