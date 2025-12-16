set_title("Graveyard")
set_size(width=15, depth=15, height=3)
set_floor_asset("Grass Floor", color="3B4D2D")
set_wall_asset("Stone Wall", interior=False, color="6B7275")

entrance_gate = Door("Iron Gate", width=2.0, depth=0.15, height=2.5, color="4A4A4A")

# Main path through the graveyard
path = Object("Gravel Path", width=2.0, depth=12.0, height=0.05, support=STANDING, color="9B9B9B")

# Gravestones of various sizes
gravestones_large = [Object("Large Gravestone", width=0.8, depth=0.3, height=1.5, support=STANDING, color="8B8B83") for _ in range(6)]
gravestones_small = [Object("Small Gravestone", width=0.5, depth=0.2, height=0.8, support=STANDING, color="A39F93") for _ in range(8)]

# Decorative elements
statues = [Object("Angel Statue", width=0.8, depth=0.8, height=2.0, support=STANDING, color="E6E6E6") for _ in range(2)]
benches = [Object("Stone Bench", width=1.2, depth=0.4, height=0.5, support=STANDING, color="8B8378") for _ in range(3)]

# Vegetation
trees = [Object("Dead Tree", width=1.5, depth=1.5, height=3.0, support=STANDING, color="4A3728") for _ in range(4)]
bushes = [Object("Bush", width=1.0, depth=1.0, height=0.8, support=STANDING, color="2F4F2F") for _ in range(6)]

# Central feature
mausoleum = Object("Mausoleum", width=3.0, depth=4.0, height=2.8, support=STANDING, color="7D7D72")

# Decorative urns
urns = [Object("Stone Urn", width=0.4, depth=0.4, height=0.6, support=STANDING, color="696969") for _ in range(4)]

# Cross monuments
crosses = [Object("Stone Cross", width=0.4, depth=0.4, height=1.8, support=STANDING, color="B8B8B8") for _ in range(3)]

entrance_gate.center.x = scene.center.x
entrance_gate.min.y = scene.min.y
entrance_gate.min.z = scene.min.z
entrance_gate.facing = Y_MAX

path.center.x = entrance_gate.center.x
path.center.y = scene.center.y
path.min.z = scene.min.z
path.facing = entrance_gate

mausoleum.center.x = scene.center.x
mausoleum.max.y = scene.max.y - 2.0
mausoleum.min.z = scene.min.z
mausoleum.facing = Y_MIN

spacing = 0.3
for i, gravestone in enumerate(gravestones_large):
    if i < 3:
        gravestone.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
        gravestone.center.y = path.min.x - spacing
    else:
        gravestone.center.x = scene.min.x + (i - 2.0) * scene.width / 4.0
        gravestone.center.y = path.max.x + spacing
    gravestone.min.z = scene.min.z
    gravestone.facing = path

for i, gravestone in enumerate(gravestones_small):
    if i < 4:
        gravestone.center.x = scene.min.x + (i + 1.5) * scene.width / 6.0
        gravestone.center.y = path.min.x - 2.0 * spacing
    else:
        gravestone.center.x = scene.min.x + (i - 2.5) * scene.width / 6.0
        gravestone.center.y = path.max.x + 2.0 * spacing
    gravestone.min.z = scene.min.z
    gravestone.facing = path

statues[0].min.x = mausoleum.min.x - spacing
statues[0].center.y = mausoleum.center.y
statues[0].min.z = scene.min.z
statues[0].facing = X_MAX

statues[1].max.x = mausoleum.max.x + spacing
statues[1].center.y = mausoleum.center.y
statues[1].min.z = scene.min.z
statues[1].facing = X_MIN

bench_spacing = 0.4
for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
    bench.min.y = path.max.y + bench_spacing
    bench.min.z = scene.min.z
    bench.facing = path

tree_param = 0.15
for i, tree in enumerate(trees):
    if i == 0:
        tree.min.x = scene.min.x + tree_param * scene.width
        tree.min.y = scene.min.y + tree_param * scene.depth
    elif i == 1:
        tree.max.x = scene.max.x - tree_param * scene.width
        tree.min.y = scene.min.y + tree_param * scene.depth
    elif i == 2:
        tree.min.x = scene.min.x + tree_param * scene.width
        tree.max.y = scene.max.y - tree_param * scene.depth
    else:
        tree.max.x = scene.max.x - tree_param * scene.width
        tree.max.y = scene.max.y - tree_param * scene.depth
    tree.min.z = scene.min.z
    tree.facing = path

bush_param = 0.2
for i, bush in enumerate(bushes):
    angle = i * 2.0 * 3.14159 / len(bushes)
    bush.center.x = scene.center.x + bush_param * scene.width * cos(angle)
    bush.center.y = scene.center.y + bush_param * scene.depth * sin(angle)
    bush.min.z = scene.min.z
    bush.facing = path

set_coordinate_frame(mausoleum)
for i, urn in enumerate(urns):
    if i < 2:
        urn.min.x = mausoleum.min.x + (i + 0.5) * mausoleum.width / 3.0
    else:
        urn.min.x = mausoleum.min.x + (i - 1.5) * mausoleum.width / 3.0
    urn.min.y = mausoleum.min.y + 0.2
    urn.min.z = scene.min.z
    urn.facing = mausoleum.facing
set_coordinate_frame(scene)

cross_param = 0.25
for i, cross in enumerate(crosses):
    cross.center.x = scene.min.x + (i + 1.0) * scene.width / 4.0
    cross.min.y = scene.min.y + cross_param * scene.depth
    cross.min.z = scene.min.z
    cross.facing = Y_MAX