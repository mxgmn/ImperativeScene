set_title("Forest Clearing")
set_size(width=20, depth=20, height=8)
set_floor_asset("Grass Floor", color="4A5D23")
set_wall_asset("Forest Background", interior=False, color="2F4F2F")

# Main trees forming the clearing border
trees = [Object("Pine Tree", width=2.0, depth=2.0, height=7.0, support=STANDING, color="2E8B57") for _ in range(15)]
birch_trees = [Object("Birch Tree", width=1.2, depth=1.2, height=6.0, support=STANDING, color="F5DEB3") for _ in range(6)]

# Focal point - large boulder formation
boulders = [
    Object("Large Boulder", width=2.5, depth=2.0, height=1.8, support=STANDING, color="808080"),
    Object("Medium Boulder", width=1.8, depth=1.5, height=1.2, support=STANDING, color="A9A9A9"),
    Object("Small Boulder", width=1.2, depth=1.0, height=0.8, support=STANDING, color="B8B8B8")
]

# Ground details
mushrooms = [Object("Mushroom", width=0.3, depth=0.3, height=0.4, support=STANDING, color="FF8C69") for _ in range(6)]
fallen_logs = [Object("Fallen Log", width=0.8, depth=2.5, height=0.6, support=STANDING, color="8B4513") for _ in range(3)]
bushes = [Object("Bush", width=1.0, depth=1.0, height=1.2, support=STANDING, color="228B22") for _ in range(8)]

# Wildlife elements
deer = Object("Deer Statue", width=1.2, depth=1.8, height=1.5, support=STANDING, color="D2B48C")
bird_bath = Object("Bird Bath", width=0.8, depth=0.8, height=1.0, support=STANDING, color="E6E6FA")

# Mystical elements
standing_stones = [Object("Standing Stone", width=0.6, depth=0.4, height=1.8, support=STANDING, color="708090") for _ in range(3)]
altar_stone = Object("Stone Altar", width=1.2, depth=0.8, height=1.0, support=STANDING, color="B8860B")

# Ground cover
ferns = [Object("Fern", width=0.6, depth=0.6, height=0.4, support=STANDING, color="3CB371") for _ in range(8)]

# Place trees in a rough circle around the clearing
param = 0.4
tree_positions = [(param * scene.width * math.cos(i * 2 * math.pi / 15), 
                   param * scene.depth * math.sin(i * 2 * math.pi / 15)) 
                  for i in range(15)]
for tree, pos in zip(trees, tree_positions):
    tree.center.x = pos[0]
    tree.center.y = pos[1]
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Place birch trees in smaller circle
birch_param = 0.3
birch_positions = [(birch_param * scene.width * math.cos(i * 2 * math.pi / 6), 
                    birch_param * scene.depth * math.sin(i * 2 * math.pi / 6)) 
                   for i in range(6)]
for tree, pos in zip(birch_trees, birch_positions):
    tree.center.x = pos[0]
    tree.center.y = pos[1]
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Boulder formation as focal point
boulders[0].center.x = scene.min.x + 0.2 * scene.width
boulders[0].center.y = scene.min.y + 0.3 * scene.depth
boulders[0].min.z = scene.min.z
boulders[0].facing = Y_MAX

set_coordinate_frame(boulders[0])
boulders[1].min.x = boulders[0].max.x - 0.3
boulders[1].min.y = boulders[0].max.y - 0.2
boulders[1].min.z = scene.min.z
boulders[1].facing = Y_MIN

boulders[2].max.x = boulders[0].min.x + 0.2
boulders[2].max.y = boulders[0].min.y + 0.2
boulders[2].min.z = scene.min.z
boulders[2].facing = X_MAX
set_coordinate_frame(scene)

# Place mushrooms near boulders
mushroom_param = 0.1
for i, mushroom in enumerate(mushrooms):
    angle = i * 2 * math.pi / len(mushrooms)
    mushroom.center.x = boulders[0].center.x + mushroom_param * scene.width * math.cos(angle)
    mushroom.center.y = boulders[0].center.y + mushroom_param * scene.depth * math.sin(angle)
    mushroom.min.z = scene.min.z
    mushroom.facing = Y_MAX

# Fallen logs scattered around
for i, log in enumerate(fallen_logs):
    log.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    log.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    log.min.z = scene.min.z
    log.facing = X_MAX + i  # Different orientations

# Bushes along the perimeter
bush_param = 0.35
for i, bush in enumerate(bushes):
    angle = i * 2 * math.pi / len(bushes)
    bush.center.x = bush_param * scene.width * math.cos(angle)
    bush.center.y = bush_param * scene.depth * math.sin(angle)
    bush.min.z = scene.min.z
    bush.facing = Y_MAX

# Wildlife elements
deer.center.x = scene.min.x + 0.6 * scene.width
deer.center.y = scene.min.y + 0.7 * scene.depth
deer.min.z = scene.min.z
deer.facing = X_MIN

bird_bath.center.x = scene.min.x + 0.3 * scene.width
bird_bath.center.y = scene.min.y + 0.4 * scene.depth
bird_bath.min.z = scene.min.z
bird_bath.facing = Y_MAX

# Standing stones in triangular formation
stone_param = 0.15
for i, stone in enumerate(standing_stones):
    angle = i * 2 * math.pi / 3
    stone.center.x = stone_param * scene.width * math.cos(angle)
    stone.center.y = stone_param * scene.depth * math.sin(angle)
    stone.min.z = scene.min.z
    stone.facing = angle  # Facing outward

altar_stone.center.x = 0.0
altar_stone.center.y = 0.0
altar_stone.min.z = scene.min.z
altar_stone.facing = Y_MAX

# Ferns scattered around
fern_param = 0.25
for i, fern in enumerate(ferns):
    angle = i * 2 * math.pi / len(ferns)
    fern.center.x = fern_param * scene.width * math.cos(angle)
    fern.center.y = fern_param * scene.depth * math.sin(angle)
    fern.min.z = scene.min.z
    fern.facing = Y_MAX