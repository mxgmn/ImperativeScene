set_title("Skyward Kingdom")
set_size(width=25, depth=25, height=20)
set_floor_asset("Cloud Floor", color="E6F0FF")
set_wall_asset("None", interior=False, color="000000") # No walls, it's in the sky!

# Main floating islands
islands = [
    Object("Floating Island Large", width=8.0, depth=8.0, height=2.0, support=FLOATING, color="7FB069"),  # Main island
    Object("Floating Island Medium", width=6.0, depth=6.0, height=1.5, support=FLOATING, color="85B875"),  # Secondary island
    Object("Floating Island Small", width=4.0, depth=4.0, height=1.0, support=FLOATING, color="8EC081")   # Third island
]

# Celestial architecture
crystal_towers = [Object("Crystal Tower", width=1.2, depth=1.2, height=5.0, support=FLOATING, color="87CEEB") for _ in range(3)]
floating_pavilion = Object("Celestial Pavilion", width=4.0, depth=4.0, height=3.5, support=FLOATING, color="E6B0AA")
sky_bridge = Object("Crystal Bridge", width=1.5, depth=6.0, height=0.3, support=FLOATING, color="B0E0E6")

# Magical elements
crystals = [Object("Floating Crystal", width=0.8, depth=0.8, height=1.2, support=FLOATING, color="FF69B4") for _ in range(6)]
light_beacons = [Object("Light Beacon", width=1.0, depth=1.0, height=2.0, support=FLOATING, color="FFD700") for _ in range(4)]

# Flora
floating_trees = [Object("Celestial Tree", width=2.0, depth=2.0, height=4.0, support=FLOATING, color="98FB98") for _ in range(5)]
sky_flowers = [Object("Glowing Flower", width=0.5, depth=0.5, height=0.8, support=FLOATING, color="FF1493") for _ in range(8)]

# Magical constructs
portal = Object("Magic Portal", width=2.5, depth=0.5, height=3.5, support=FLOATING, color="9370DB")
observatory = Object("Sky Observatory", width=3.0, depth=3.0, height=2.5, support=FLOATING, color="DDA0DD")
sundial = Object("Floating Sundial", width=2.0, depth=2.0, height=1.0, support=FLOATING, color="FFB6C1")

# Guardian elements
sentinel_statues = [Object("Guardian Statue", width=1.0, depth=1.0, height=2.5, support=FLOATING, color="B8860B") for _ in range(4)]