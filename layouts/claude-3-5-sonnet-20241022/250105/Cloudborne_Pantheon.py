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

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

# Place windows evenly around the walls
window_offset = 0.2
for i, window in enumerate(windows):
    if i < 2:  # Front wall
        window.center.x = scene.min.x + (i+1.0) * scene.width / 3.0
        window.min.y = scene.min.y
        window.min.z = scene.height * 0.4
        window.facing = Y_MAX
    elif i < 4:  # Back wall
        window.center.x = scene.min.x + (i-1.0) * scene.width / 3.0
        window.max.y = scene.max.y
        window.min.z = scene.height * 0.4
        window.facing = Y_MIN
    elif i < 6:  # Left wall
        window.min.x = scene.min.x
        window.center.y = scene.min.y + (i-3.0) * scene.depth / 3.0
        window.min.z = scene.height * 0.4
        window.facing = X_MAX
    else:  # Right wall
        window.max.x = scene.max.x
        window.center.y = scene.min.y + (i-5.0) * scene.depth / 3.0
        window.min.z = scene.height * 0.4
        window.facing = X_MIN

# Central elements
central_platform.center.x = scene.center.x
central_platform.center.y = scene.center.y
central_platform.min.z = scene.height * 0.3
central_platform.facing = Y_MIN

divine_throne.center.x = central_platform.center.x
divine_throne.center.y = central_platform.center.y
divine_throne.min.z = central_platform.max.z
divine_throne.facing = Y_MIN

energy_crystal.center.x = central_platform.center.x
energy_crystal.center.y = central_platform.center.y
energy_crystal.min.z = divine_throne.max.z + 1.0
energy_crystal.facing = Y_MIN

# Arrange platforms in a circle
platform_radius = 8.0
for i, platform in enumerate(platforms):
    angle = i * (2.0 * 3.14159 / len(platforms))
    platform.center.x = scene.center.x + platform_radius * math.cos(angle)
    platform.center.y = scene.center.y + platform_radius * math.sin(angle)
    platform.min.z = scene.height * 0.2
    platform.facing = Y_MIN

# Place statues on platforms
for i, (statue, platform) in enumerate(zip(statues, platforms)):
    statue.center.x = platform.center.x
    statue.center.y = platform.center.y
    statue.min.z = platform.max.z
    statue.facing = central_platform

# Place pillars in octagon formation
pillar_radius = 10.0
for i, pillar in enumerate(pillars):
    angle = i * (2.0 * 3.14159 / len(pillars))
    pillar.center.x = scene.center.x + pillar_radius * math.cos(angle)
    pillar.center.y = scene.center.y + pillar_radius * math.sin(angle)
    pillar.min.z = scene.min.z
    pillar.facing = Y_MIN

# Place offering altars
altar_radius = 6.0
for i, altar in enumerate(offering_altars):
    angle = i * (2.0 * 3.14159 / len(offering_altars))
    altar.center.x = scene.center.x + altar_radius * math.cos(angle)
    altar.center.y = scene.center.y + altar_radius * math.sin(angle)
    altar.min.z = scene.min.z
    altar.facing = central_platform

# Place bridges connecting central platform to outer platforms
for i, bridge in enumerate(bridges):
    bridge.center.x = (central_platform.center.x + platforms[i].center.x) / 2.0
    bridge.center.y = (central_platform.center.y + platforms[i].center.y) / 2.0
    bridge.min.z = central_platform.min.z
    angle = math.atan2(platforms[i].center.y - central_platform.center.y,
                      platforms[i].center.x - central_platform.center.x)
    bridge.facing = angle

# Place floating artifacts in spiral pattern
artifact_radius = 4.0
for i, artifact in enumerate(artifacts):
    angle = i * (2.0 * 3.14159 / len(artifacts))
    height_offset = i * scene.height * 0.1
    artifact.center.x = scene.center.x + artifact_radius * math.cos(angle)
    artifact.center.y = scene.center.y + artifact_radius * math.sin(angle)
    artifact.min.z = scene.height * 0.3 + height_offset
    artifact.facing = Y_MIN

# Place incense burners on platforms
for i, burner in enumerate(incense_burners):
    if i < len(platforms):
        burner.center.x = platforms[i].center.x
        burner.min.y = platforms[i].min.y + 0.1
        burner.min.z = platforms[i].max.z
        burner.facing = central_platform