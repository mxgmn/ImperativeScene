set_title("Cloudborne Pantheon")
set_size(width=25, depth=25, height=15)
set_floor_asset("Marble Floor", color="E6E6FA")
set_wall_asset("Carved Stone Wall", interior=True, color="B8B8DC")

entrance = Door("Grand Double Door", width=4.0, depth=0.2, height=6.0, color="FFD700")
windows = [Window("Stained Glass Window", width=2.0, depth=0.1, height=4.0, color="87CEEB") for _ in range(8)]

# Central divine elements
central_platform = Object("Floating Platform", width=8.0, depth=8.0, height=0.5, support=FLOATING, color="E0FFFF")
divine_throne = Object("Celestial Throne", width=3.0, depth=2.5, height=4.0, support=FLOATING, color="4169E1")
energy_crystal = Object("Crystal", width=1.5, depth=1.5, height=3.0, support=FLOATING, color="00FFFF")

# Floating platforms arranged in a circle
platforms = [Object("Floating Platform", width=4.0, depth=4.0, height=0.5, support=FLOATING, color="B0E0E6") for _ in range(6)]

# Divine statues on the platforms
statues = [Object("Divine Statue", width=1.5, depth=1.5, height=3.0, support=STANDING, color="F0F8FF") for _ in range(6)]

# Decorative elements
pillars = [Object("Floating Pillar", width=1.0, depth=1.0, height=8.0, support=FLOATING, color="ADD8E6") for _ in range(8)]
offering_altars = [Object("Offering Altar", width=1.2, depth=0.8, height=1.0, support=STANDING, color="7B68EE") for _ in range(4)]
incense_burners = [Object("Incense Burner", width=0.4, depth=0.4, height=0.6, support=STANDING, color="9370DB") for _ in range(6)]

# Energy bridges connecting platforms
bridges = [Object("Energy Bridge", width=4.0, depth=1.0, height=0.2, support=FLOATING, color="87CEFA") for _ in range(6)]

# Mystical artifacts
artifacts = [Object("Floating Artifact", width=0.5, depth=0.5, height=0.5, support=FLOATING, color="E6E6FA") for _ in range(8)]