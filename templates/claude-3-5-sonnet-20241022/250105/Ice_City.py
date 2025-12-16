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