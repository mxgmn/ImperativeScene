set_title("Ice City Plaza")
set_size(width=30, depth=30, height=15)
set_floor_asset("Ice Floor", color="E0FFFF")
set_wall_asset("Ice Wall", interior=False, color="F0F8FF")

# Main architectural features
ice_palace = Object("Ice Palace", width=12.0, depth=8.0, height=15.0, support=STANDING, color="B0E2FF")
ice_towers = [Object("Ice Tower", width=3.0, depth=3.0, height=12.0, support=STANDING, color="87CEEB") for _ in range(4)]

# Decorative elements
ice_sculptures = [Object("Ice Sculpture", width=1.5, depth=1.5, height=3.0, support=STANDING, color="F0FFFF") for _ in range(6)]
ice_fountains = [Object("Ice Fountain", width=2.0, depth=2.0, height=3.0, support=STANDING, color="00BFFF") for _ in range(2)]
ice_benches = [Object("Ice Bench", width=2.0, depth=0.6, height=0.5, support=STANDING, color="B9D3EE") for _ in range(8)]

# Light sources (represented as ice crystals that emit light)
ice_crystals = [Object("Ice Crystal", width=0.8, depth=0.8, height=2.0, support=STANDING, color="E0FFFF") for _ in range(12)]

# City walls and gates
ice_gate = Object("Ice Gate", width=6.0, depth=1.0, height=8.0, support=STANDING, color="87CEFA")
ice_walls = [Object("Ice Wall Section", width=8.0, depth=1.0, height=6.0, support=STANDING, color="B0E0E6") for _ in range(4)]

# Market area
market_stalls = [Object("Ice Stall", width=2.0, depth=1.5, height=2.0, support=STANDING, color="4169E1") for _ in range(6)]

# Central palace placement
ice_palace.center.x = scene.center.x
ice_palace.center.y = scene.center.y
ice_palace.min.z = scene.min.z
ice_palace.facing = Y_MAX

# Tower placement at corners of central square
tower_offset = 8.0
for i, tower in enumerate(ice_towers):
    tower.center.x = ice_palace.center.x + (1 if i % 2 == 0 else -1) * tower_offset
    tower.center.y = ice_palace.center.y + (1 if i < 2 else -1) * tower_offset
    tower.min.z = scene.min.z
    tower.facing = Y_MAX

# Ice sculptures in a circular pattern around palace
sculpture_radius = 10.0
for i, sculpture in enumerate(ice_sculptures):
    angle = i * (2.0 * 3.14159 / len(ice_sculptures))
    sculpture.center.x = ice_palace.center.x + sculpture_radius * math.cos(angle)
    sculpture.center.y = ice_palace.center.y + sculpture_radius * math.sin(angle)
    sculpture.min.z = scene.min.z
    sculpture.facing = ice_palace

# Fountains on main axis
fountain_offset = 12.0
for i, fountain in enumerate(ice_fountains):
    fountain.center.x = ice_palace.center.x
    fountain.center.y = ice_palace.center.y + (1 if i == 0 else -1) * fountain_offset
    fountain.min.z = scene.min.z
    fountain.facing = ice_palace

# Benches arranged in pairs
bench_radius = 15.0
for i, bench in enumerate(ice_benches):
    angle = (i // 2) * (2.0 * 3.14159 / (len(ice_benches) / 2))
    bench.center.x = ice_palace.center.x + bench_radius * math.cos(angle)
    bench.center.y = ice_palace.center.y + bench_radius * math.sin(angle)
    bench.min.z = scene.min.z
    bench.facing = ice_palace

# Ice crystals for lighting
crystal_radius = 13.0
for i, crystal in enumerate(ice_crystals):
    angle = i * (2.0 * 3.14159 / len(ice_crystals))
    crystal.center.x = ice_palace.center.x + crystal_radius * math.cos(angle)
    crystal.center.y = ice_palace.center.y + crystal_radius * math.sin(angle)
    crystal.min.z = scene.min.z
    crystal.facing = ice_palace

# Main gate
ice_gate.center.x = scene.center.x
ice_gate.min.y = scene.min.y
ice_gate.min.z = scene.min.z
ice_gate.facing = Y_MAX

# City walls
wall_offset = 0.25 * scene.width
for i, wall in enumerate(ice_walls):
    if i == 0:
        wall.min.x = scene.min.x
        wall.center.y = scene.center.y
        wall.facing = X_MAX
    elif i == 1:
        wall.max.x = scene.max.x
        wall.center.y = scene.center.y
        wall.facing = X_MIN
    elif i == 2:
        wall.center.x = scene.center.x + wall_offset
        wall.max.y = scene.max.y
        wall.facing = Y_MIN
    else:
        wall.center.x = scene.center.x - wall_offset
        wall.max.y = scene.max.y
        wall.facing = Y_MIN
    wall.min.z = scene.min.z

# Market stalls in a semi-circle
stall_radius = 18.0
stall_arc = 3.14159  # half circle
for i, stall in enumerate(market_stalls):
    angle = stall_arc/2 + i * (stall_arc / (len(market_stalls) - 1))
    stall.center.x = ice_palace.center.x + stall_radius * math.cos(angle)
    stall.center.y = ice_palace.center.y + stall_radius * math.sin(angle)
    stall.min.z = scene.min.z
    stall.facing = ice_palace