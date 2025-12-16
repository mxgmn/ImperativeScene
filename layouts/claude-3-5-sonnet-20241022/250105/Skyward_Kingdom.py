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

# Position the main islands in a triangular formation
islands[0].center.x = scene.center.x
islands[0].center.y = scene.center.y
islands[0].min.z = scene.min.z + 5.0
islands[0].facing = Y_MAX

islands[1].center.x = scene.center.x + 0.3 * scene.width
islands[1].center.y = scene.center.y - 0.2 * scene.depth
islands[1].min.z = scene.min.z + 7.0
islands[1].facing = X_MIN

islands[2].center.x = scene.center.x - 0.3 * scene.width
islands[2].center.y = scene.center.y + 0.2 * scene.depth
islands[2].min.z = scene.min.z + 6.0
islands[2].facing = X_MAX

# Position crystal towers on the main island
set_coordinate_frame(islands[0])
for i, tower in enumerate(crystal_towers):
    angle = i * 2.0 * 3.14159 / 3.0
    radius = 0.3
    tower.center.x = islands[0].center.x + radius * islands[0].width * math.cos(angle)
    tower.center.y = islands[0].center.y + radius * islands[0].depth * math.sin(angle)
    tower.min.z = islands[0].max.z
    tower.facing = i
set_coordinate_frame(scene)

# Position the pavilion on the second island
floating_pavilion.center.x = islands[1].center.x
floating_pavilion.center.y = islands[1].center.y
floating_pavilion.min.z = islands[1].max.z
floating_pavilion.facing = islands[0]

# Create bridge between main and secondary island
sky_bridge.center.x = (islands[0].center.x + islands[1].center.x) / 2.0
sky_bridge.center.y = (islands[0].center.y + islands[1].center.y) / 2.0
sky_bridge.center.z = (islands[0].center.z + islands[1].center.z) / 2.0
sky_bridge.facing = islands[1]

# Distribute crystals around the islands
for i, crystal in enumerate(crystals):
    if i < 3:
        set_coordinate_frame(islands[0])
        angle = i * 2.0 * 3.14159 / 3.0
        radius = 0.4
    else:
        set_coordinate_frame(islands[1])
        angle = (i-3) * 2.0 * 3.14159 / 3.0
        radius = 0.35
    crystal.center.x = radius * islands[0].width * math.cos(angle)
    crystal.center.y = radius * islands[0].depth * math.sin(angle)
    crystal.min.z = 2.0
set_coordinate_frame(scene)

# Position light beacons
for i, beacon in enumerate(light_beacons):
    if i < 2:
        set_coordinate_frame(islands[0])
    else:
        set_coordinate_frame(islands[1])
    angle = i * 3.14159
    radius = 0.25
    beacon.center.x = radius * islands[0].width * math.cos(angle)
    beacon.center.y = radius * islands[0].depth * math.sin(angle)
    beacon.min.z = 1.0
set_coordinate_frame(scene)

# Distribute trees
for i, tree in enumerate(floating_trees):
    if i < 3:
        set_coordinate_frame(islands[0])
    else:
        set_coordinate_frame(islands[1])
    angle = i * 2.0 * 3.14159 / 3.0
    radius = 0.2
    tree.center.x = radius * islands[0].width * math.cos(angle)
    tree.center.y = radius * islands[0].depth * math.sin(angle)
    tree.min.z = 0.0
set_coordinate_frame(scene)

# Position magical constructs
portal.center.x = islands[2].center.x
portal.center.y = islands[2].center.y
portal.min.z = islands[2].max.z
portal.facing = islands[0]

observatory.center.x = islands[1].center.x
observatory.center.y = islands[1].center.y
observatory.min.z = islands[1].max.z + 1.0
observatory.facing = islands[0]

sundial.center.x = islands[0].center.x
sundial.center.y = islands[0].center.y
sundial.min.z = islands[0].max.z
sundial.facing = Y_MAX

# Position sentinel statues
for i, statue in enumerate(sentinel_statues):
    set_coordinate_frame(islands[0])
    angle = i * 2.0 * 3.14159 / 4.0
    radius = 0.45
    statue.center.x = radius * islands[0].width * math.cos(angle)
    statue.center.y = radius * islands[0].depth * math.sin(angle)
    statue.min.z = 0.0
    statue.facing = i
set_coordinate_frame(scene)

# Scatter sky flowers
for i, flower in enumerate(sky_flowers):
    if i < 4:
        set_coordinate_frame(islands[0])
    else:
        set_coordinate_frame(islands[1])
    angle = i * 2.0 * 3.14159 / 4.0
    radius = 0.3
    flower.center.x = radius * islands[0].width * math.cos(angle)
    flower.center.y = radius * islands[0].depth * math.sin(angle)
    flower.min.z = 1.5
set_coordinate_frame(scene)