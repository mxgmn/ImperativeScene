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

# Place platforms in triangular formation
param = 0.3
platforms[0].center.x = scene.center.x
platforms[0].center.y = scene.min.y + param * scene.depth
platforms[0].min.z = scene.min.z
platforms[0].facing = Y_MAX

platforms[1].center.x = scene.min.x + param * scene.width
platforms[1].center.y = scene.max.y - param * scene.depth
platforms[1].min.z = scene.min.z
platforms[1].facing = Y_MIN

platforms[2].center.x = scene.max.x - param * scene.width
platforms[2].center.y = scene.max.y - param * scene.depth
platforms[2].min.z = scene.min.z
platforms[2].facing = Y_MIN

# Place barriers in defensive positions around platforms
barrier_spacing = 0.25
for i, barrier in enumerate(barriers):
    if i < 3:
        set_coordinate_frame(platforms[0])
        barrier.center.x = platforms[0].min.x + (i+1.0) / 4.0 * platforms[0].width
        barrier.min.y = platforms[0].max.y + barrier_spacing
    elif i < 6:
        set_coordinate_frame(platforms[1])
        barrier.center.x = platforms[1].min.x + (i-2.0) / 4.0 * platforms[1].width
        barrier.min.y = platforms[1].max.y + barrier_spacing
    else:
        set_coordinate_frame(platforms[2])
        barrier.center.x = platforms[2].min.x + (i-5.0) / 4.0 * platforms[2].width
        barrier.min.y = platforms[2].max.y + barrier_spacing
    barrier.min.z = scene.min.z
    barrier.facing = Y_MIN
set_coordinate_frame(scene)

# Place crates for cover
crate_param = 0.2
for i, crate in enumerate(crates):
    angle = i * 60.0
    crate.center.x = scene.center.x + crate_param * scene.width * math.cos(math.radians(angle))
    crate.center.y = scene.center.y + crate_param * scene.depth * math.sin(math.radians(angle))
    crate.min.z = scene.min.z
    crate.facing = Y_MAX

# Place containers along walls
container_param = 0.15
for i, container in enumerate(containers):
    if i < 2:
        container.min.x = scene.min.x + container_param * scene.width + i * container.width * 1.2
        container.min.y = scene.min.y
    else:
        container.min.x = scene.max.x - container_param * scene.width - (i-1) * container.width * 1.2
        container.max.y = scene.max.y
    container.min.z = scene.min.z
    container.facing = Y_MAX if i < 2 else Y_MIN

# Place sniper nests in opposite corners
sniper_nests[0].min.x = scene.min.x + container_param * scene.width
sniper_nests[0].min.y = scene.min.y + container_param * scene.depth
sniper_nests[1].max.x = scene.max.x - container_param * scene.width
sniper_nests[1].max.y = scene.max.y - container_param * scene.depth
for nest in sniper_nests:
    nest.min.z = scene.min.z
    nest.facing = Y_MAX

# Place power-up stations
station_param = 0.4
for i, station in enumerate(weapon_stands + health_stations + armor_stations):
    angle = i * 45.0
    station.center.x = scene.center.x + station_param * scene.width * math.cos(math.radians(angle))
    station.center.y = scene.center.y + station_param * scene.depth * math.sin(math.radians(angle))
    station.min.z = scene.min.z
    station.facing = Y_MAX

# Place pipes on walls
pipe_height = 0.7
for i, pipe in enumerate(pipes):
    if i < 3:
        pipe.min.x = scene.min.x
        pipe.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
        pipe.min.z = pipe_height * scene.height
        pipe.facing = X_MAX
    else:
        pipe.max.x = scene.max.x
        pipe.center.y = scene.min.y + (i-2.0) / 4.0 * scene.depth
        pipe.min.z = pipe_height * scene.height
        pipe.facing = X_MIN

# Place warning signs
sign_height = 0.6
for i, sign in enumerate(warning_signs):
    if i < 2:
        sign.min.x = scene.min.x
        sign.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    else:
        sign.max.x = scene.max.x
        sign.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
    sign.min.z = sign_height * scene.height
    sign.facing = X_MAX if i < 2 else X_MIN

# Place doors in cardinal directions
door_param = 0.2
doors[0].center.x = scene.center.x
doors[0].min.y = scene.min.y
doors[0].min.z = scene.min.z
doors[0].facing = Y_MAX

doors[1].center.x = scene.center.x
doors[1].max.y = scene.max.y
doors[1].min.z = scene.min.z
doors[1].facing = Y_MIN

doors[2].min.x = scene.min.x
doors[2].center.y = scene.center.y
doors[2].min.z = scene.min.z
doors[2].facing = X_MAX

doors[3].max.x = scene.max.x
doors[3].center.y = scene.center.y
doors[3].min.z = scene.min.z
doors[3].facing = X_MIN