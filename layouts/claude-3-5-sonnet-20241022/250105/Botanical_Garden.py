set_title("Botanical Garden")
set_size(width=15, depth=15, height=4.1)
set_floor_asset("Stone Path", color="9B8E83")
set_wall_asset("Glass Wall", interior=True, color="A3C1D1")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.5, color="87CEEB") for _ in range(6)]

# Main features
large_planters = [Object("Large Planter", width=2.0, depth=2.0, height=0.6, support=STANDING, color="8B4513") for _ in range(4)]
medium_planters = [Object("Medium Planter", width=1.2, depth=1.2, height=0.5, support=STANDING, color="A0522D") for _ in range(6)]
small_planters = [Object("Small Planter", width=0.8, depth=0.8, height=0.4, support=STANDING, color="8B4513") for _ in range(8)]

# Plants (using the planters as bases)
palm_trees = [Object("Palm Tree", width=1.8, depth=1.8, height=3.5, support=STANDING, color="228B22") for _ in range(2)]
ferns = [Object("Large Fern", width=1.0, depth=1.0, height=1.2, support=STANDING, color="32CD32") for _ in range(4)]
bamboo = [Object("Bamboo Plant", width=0.6, depth=0.6, height=2.5, support=STANDING, color="90EE90") for _ in range(6)]
orchids = [Object("Orchid Plant", width=0.4, depth=0.4, height=0.6, support=STANDING, color="FF69B4") for _ in range(8)]

# Furniture and decorative elements
benches = [Object("Garden Bench", width=1.5, depth=0.6, height=0.9, support=STANDING, color="8B7355") for _ in range(4)]
fountain = Object("Stone Fountain", width=2.0, depth=2.0, height=1.5, support=STANDING, color="B8860B")
information_boards = [Object("Information Board", width=0.8, depth=0.1, height=1.2, support=MOUNTED, color="DEB887") for _ in range(3)]
stone_path = [Object("Decorative Stone", width=0.4, depth=0.4, height=0.05, support=STANDING, color="808080") for _ in range(12)]

# Maintenance area
tool_cabinet = Object("Tool Cabinet", width=1.2, depth=0.6, height=1.8, support=STANDING, color="556B2F")
watering_station = Object("Watering Station", width=0.8, depth=0.6, height=1.0, support=STANDING, color="4682B4")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

for i, window in enumerate(windows):
    if i < 3:
        window.min.x = scene.min.x
        window.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
        window.facing = X_MAX
    else:
        window.max.x = scene.max.x
        window.center.y = scene.min.y + (i-2.0) / 4.0 * scene.depth
        window.facing = X_MIN
    window.min.z = 0.5

fountain.center.x = scene.center.x
fountain.center.y = scene.center.y
fountain.min.z = scene.min.z
fountain.facing = Y_MAX

param = 0.3
positions = [(param, param), (-param, param), (param, -param), (-param, -param)]
for i, planter in enumerate(large_planters):
    planter.center.x = scene.center.x + positions[i][0] * scene.width
    planter.center.y = scene.center.y + positions[i][1] * scene.depth
    planter.min.z = scene.min.z
    planter.facing = Y_MAX

param = 0.4
for i, planter in enumerate(medium_planters):
    angle = i * (2.0 * 3.14159 / len(medium_planters))
    planter.center.x = scene.center.x + param * scene.width * math.cos(angle)
    planter.center.y = scene.center.y + param * scene.depth * math.sin(angle)
    planter.min.z = scene.min.z
    planter.facing = Y_MAX

param = 0.45
for i, planter in enumerate(small_planters):
    angle = i * (2.0 * 3.14159 / len(small_planters))
    planter.center.x = scene.center.x + param * scene.width * math.cos(angle)
    planter.center.y = scene.center.y + param * scene.depth * math.sin(angle)
    planter.min.z = scene.min.z
    planter.facing = Y_MAX

for i, (tree, planter) in enumerate(zip(palm_trees, large_planters[:2])):
    tree.center.x = planter.center.x
    tree.center.y = planter.center.y
    tree.min.z = planter.max.z
    tree.facing = planter.facing

for i, (fern, planter) in enumerate(zip(ferns, large_planters[2:])):
    fern.center.x = planter.center.x
    fern.center.y = planter.center.y
    fern.min.z = planter.max.z
    fern.facing = planter.facing

for i, (bamboo, planter) in enumerate(zip(bamboo, medium_planters)):
    bamboo.center.x = planter.center.x
    bamboo.center.y = planter.center.y
    bamboo.min.z = planter.max.z
    bamboo.facing = planter.facing

for i, (orchid, planter) in enumerate(zip(orchids, small_planters)):
    orchid.center.x = planter.center.x
    orchid.center.y = planter.center.y
    orchid.min.z = planter.max.z
    orchid.facing = planter.facing

param = 0.35
for i, bench in enumerate(benches):
    angle = i * (2.0 * 3.14159 / len(benches))
    bench.center.x = scene.center.x + param * scene.width * math.cos(angle)
    bench.center.y = scene.center.y + param * scene.depth * math.sin(angle)
    bench.min.z = scene.min.z
    bench.facing = fountain

for i, board in enumerate(information_boards):
    board.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    board.min.y = scene.min.y
    board.min.z = 1.0
    board.facing = Y_MAX

param = 0.25
for i, stone in enumerate(stone_path):
    angle = i * (2.0 * 3.14159 / len(stone_path))
    stone.center.x = scene.center.x + param * scene.width * math.cos(angle)
    stone.center.y = scene.center.y + param * scene.depth * math.sin(angle)
    stone.min.z = scene.min.z
    stone.facing = Y_MAX

tool_cabinet.min.x = scene.min.x + 0.1
tool_cabinet.max.y = scene.max.y - 0.1
tool_cabinet.min.z = scene.min.z
tool_cabinet.facing = X_MAX

watering_station.min.x = tool_cabinet.max.x + 0.2
watering_station.max.y = scene.max.y - 0.1
watering_station.min.z = scene.min.z
watering_station.facing = X_MAX