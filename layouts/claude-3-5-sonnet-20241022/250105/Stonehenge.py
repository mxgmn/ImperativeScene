set_title("Stonehenge")
set_size(width=30, depth=30, height=7)
set_floor_asset("Grass Ground", color="4A5D23")
set_wall_asset("None", interior=False, color="000000")

# The outer circle of standing stones with lintels
outer_stones = [Object("Standing Stone", width=2.2, depth=1.3, height=4.1, support=STANDING, color="787878") for _ in range(30)]
outer_lintels = [Object("Lintel Stone", width=3.2, depth=1.0, height=1.0, support=STANDING, color="696969") for _ in range(30)]

# The inner horseshoe of larger trilithons
inner_trilithon_stones = [Object("Standing Stone", width=2.5, depth=1.5, height=6.7, support=STANDING, color="808080") for _ in range(10)]
inner_trilithon_lintels = [Object("Lintel Stone", width=3.5, depth=1.2, height=1.2, support=STANDING, color="707070") for _ in range(5)]

# The inner horseshoe of smaller bluestones
inner_bluestones = [Object("Standing Stone", width=1.5, depth=0.8, height=2.5, support=STANDING, color="4A5B73") for _ in range(19)]

# The altar stone
altar_stone = Object("Altar Stone", width=4.9, depth=1.0, height=1.0, support=STANDING, color="656565")

# The heel stone
heel_stone = Object("Standing Stone", width=2.4, depth=1.4, height=4.9, support=STANDING, color="736F6E")

# Fallen and leaning stones
fallen_stones = [Object("Standing Stone", width=2.0, depth=1.2, height=3.8, support=STANDING, color="767676") for _ in range(5)]

# Station stones
station_stones = [Object("Standing Stone", width=1.8, depth=1.0, height=2.5, support=STANDING, color="727272") for _ in range(4)]

# Aubrey holes (represented as stone markers since we can't do holes)
aubrey_markers = [Object("Stone Marker", width=0.5, depth=0.5, height=0.3, support=STANDING, color="8B8B83") for _ in range(56)]

# Place outer circle stones and lintels
radius = 12.0
for i, (stone, lintel) in enumerate(zip(outer_stones, outer_lintels)):
    angle = i * 2.0 * 3.14159 / len(outer_stones)
    stone.center.x = radius * cos(angle)
    stone.center.y = radius * sin(angle)
    stone.min.z = scene.min.z
    stone.facing = stone.center
    lintel.center.x = stone.center.x
    lintel.center.y = stone.center.y
    lintel.min.z = stone.max.z
    lintel.facing = stone.facing

# Place inner horseshoe trilithons
inner_radius = 8.0
for i, stone in enumerate(inner_trilithon_stones):
    pair_index = i // 2
    is_left = i % 2 == 0
    angle = (3.14159 / 2.0) + (pair_index * 3.14159 / 4.0)
    stone.center.x = inner_radius * cos(angle)
    stone.center.y = inner_radius * sin(angle)
    stone.min.z = scene.min.z
    stone.facing = stone.center
    
    if is_left and pair_index < len(inner_trilithon_lintels):
        lintel = inner_trilithon_lintels[pair_index]
        lintel.center.x = stone.center.x
        lintel.center.y = stone.center.y
        lintel.min.z = stone.max.z
        lintel.facing = stone.facing

# Place inner bluestone horseshoe
bluestone_radius = 6.0
for i, stone in enumerate(inner_bluestones):
    angle = (3.14159 / 2.0) + (i * 3.14159 / (len(inner_bluestones) - 1))
    stone.center.x = bluestone_radius * cos(angle)
    stone.center.y = bluestone_radius * sin(angle)
    stone.min.z = scene.min.z
    stone.facing = stone.center

# Place altar stone at center
altar_stone.center.x = 0.0
altar_stone.center.y = 0.0
altar_stone.min.z = scene.min.z
altar_stone.facing = Y_MAX

# Place heel stone
heel_stone.center.x = 0.0
heel_stone.min.y = scene.min.y + 0.1 * scene.depth
heel_stone.min.z = scene.min.z
heel_stone.facing = Y_MAX

# Place fallen stones randomly
fallen_positions = [(8.0, -5.0), (-7.0, 6.0), (6.0, 7.0), (-5.0, -8.0), (4.0, -7.0)]
for stone, pos in zip(fallen_stones, fallen_positions):
    stone.center.x = pos[0]
    stone.center.y = pos[1]
    stone.min.z = scene.min.z
    stone.facing = X_MAX

# Place station stones in rectangle corners
station_positions = [(8.0, 8.0), (-8.0, 8.0), (8.0, -8.0), (-8.0, -8.0)]
for stone, pos in zip(station_stones, station_positions):
    stone.center.x = pos[0]
    stone.center.y = pos[1]
    stone.min.z = scene.min.z
    stone.facing = stone.center

# Place Aubrey hole markers in a circle
aubrey_radius = 14.0
for i, marker in enumerate(aubrey_markers):
    angle = i * 2.0 * 3.14159 / len(aubrey_markers)
    marker.center.x = aubrey_radius * cos(angle)
    marker.center.y = aubrey_radius * sin(angle)
    marker.min.z = scene.min.z
    marker.facing = marker.center