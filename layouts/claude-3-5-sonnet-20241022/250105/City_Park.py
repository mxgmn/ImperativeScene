set_title("City Park")
set_size(width=25, depth=25, height=4)
set_floor_asset("Grass Floor", color="4F7942")
set_wall_asset("Iron Fence", interior=False, color="2F4F4F")

entrance_gate = Door("Iron Gate", width=3.0, depth=0.2, height=2.5, color="4A4A4A")

# Main pathway
path = Object("Stone Path", width=3.0, depth=25.0, height=0.1, support=STANDING, color="9B8B7D")
crossing_path = Object("Stone Path", width=15.0, depth=3.0, height=0.1, support=STANDING, color="9B8B7D")

# Seating areas
benches = [Object("Park Bench", width=1.8, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]

# Greenery
trees = [Object("Maple Tree", width=3.0, depth=3.0, height=4.0, support=STANDING, color="228B22") for _ in range(8)]
bushes = [Object("Flowering Bush", width=1.2, depth=1.2, height=1.0, support=STANDING, color="32CD32") for _ in range(12)]

# Central feature
fountain = Object("Fountain", width=4.0, depth=4.0, height=2.0, support=STANDING, color="87CEEB")

# Recreation
playground = Object("Playground Set", width=6.0, depth=6.0, height=3.0, support=STANDING, color="FFA500")
sandbox = Object("Sandbox", width=3.0, depth=3.0, height=0.3, support=STANDING, color="F4A460")

# Amenities
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.8, support=STANDING, color="2E8B57") for _ in range(4)]
bike_rack = Object("Bike Rack", width=2.0, depth=0.3, height=0.8, support=STANDING, color="CD853F")

# Information
info_board = Object("Information Board", width=1.5, depth=0.1, height=1.8, support=STANDING, color="8B4513")

entrance_gate.center.x = scene.center.x
entrance_gate.min.y = scene.min.y
entrance_gate.min.z = scene.min.z
entrance_gate.facing = Y_MAX

path.center.x = scene.center.x
path.center.y = scene.center.y
path.min.z = scene.min.z
path.facing = Y_MAX

crossing_path.center.x = scene.center.x
crossing_path.center.y = scene.center.y
crossing_path.min.z = scene.min.z
crossing_path.facing = X_MAX

fountain.center.x = scene.center.x
fountain.center.y = scene.center.y
fountain.min.z = scene.min.z
fountain.facing = Y_MAX

# Place benches along the paths
param = 0.25
for i, bench in enumerate(benches):
    if i < 3:
        bench.min.x = path.max.x + 0.5
        bench.center.y = scene.min.y + (i + 1.0) * param * scene.depth
    else:
        bench.max.x = path.min.x - 0.5
        bench.center.y = scene.min.y + (i - 2.0) * param * scene.depth
    bench.min.z = scene.min.z
    bench.facing = path

# Place trees in a natural arrangement
tree_param = 0.2
for i, tree in enumerate(trees):
    if i < 4:
        tree.center.x = scene.min.x + (i + 1.0) * tree_param * scene.width
        tree.center.y = scene.min.y + tree_param * scene.depth
    else:
        tree.center.x = scene.min.x + (i - 3.0) * tree_param * scene.width
        tree.center.y = scene.max.y - tree_param * scene.depth
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Arrange bushes around the fountain
bush_param = 45.0
for i, bush in enumerate(bushes):
    angle = i * (360.0 / len(bushes))
    radius = 3.0
    bush.center.x = fountain.center.x + radius * math.cos(math.radians(angle))
    bush.center.y = fountain.center.y + radius * math.sin(math.radians(angle))
    bush.min.z = scene.min.z
    bush.facing = Y_MAX

playground.max.x = scene.max.x - 2.0
playground.max.y = scene.max.y - 2.0
playground.min.z = scene.min.z
playground.facing = X_MIN

sandbox.min.x = playground.min.x - 4.0
sandbox.center.y = playground.center.y
sandbox.min.z = scene.min.z
sandbox.facing = playground

# Place trash bins at path intersections
for i, bin in enumerate(trash_bins):
    if i == 0:
        bin.center.x = path.max.x + 0.5
        bin.center.y = crossing_path.max.y + 0.5
    elif i == 1:
        bin.center.x = path.min.x - 0.5
        bin.center.y = crossing_path.max.y + 0.5
    elif i == 2:
        bin.center.x = path.max.x + 0.5
        bin.center.y = crossing_path.min.y - 0.5
    else:
        bin.center.x = path.min.x - 0.5
        bin.center.y = crossing_path.min.y - 0.5
    bin.min.z = scene.min.z
    bin.facing = Y_MAX

bike_rack.min.x = scene.min.x + 2.0
bike_rack.min.y = scene.min.y + 2.0
bike_rack.min.z = scene.min.z
bike_rack.facing = X_MAX

info_board.min.x = entrance_gate.max.x + 1.0
info_board.min.y = scene.min.y + 1.0
info_board.min.z = scene.min.z
info_board.facing = X_MIN