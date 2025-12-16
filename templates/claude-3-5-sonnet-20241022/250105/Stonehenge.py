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