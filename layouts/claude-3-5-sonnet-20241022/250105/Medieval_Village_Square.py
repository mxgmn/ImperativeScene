set_title("Medieval Village Square")
set_size(width=25, depth=25, height=4)
set_floor_asset("Cobblestone Floor", color="6B7275")
set_wall_asset("None", interior=False, color="000000")

# Central feature
well = Object("Stone Well", width=2.0, depth=2.0, height=1.2, support=STANDING, color="8B8378")

# Market stalls
market_stalls = [Object("Wooden Stall", width=2.0, depth=1.5, height=2.2, support=STANDING, color="8B4513") for _ in range(6)]
barrels = [Object("Wooden Barrel", width=0.8, depth=0.8, height=1.2, support=STANDING, color="DEB887") for _ in range(6)]
crates = [Object("Wooden Crate", width=0.7, depth=0.7, height=0.6, support=STANDING, color="CD853F") for _ in range(5)]

# Buildings around the square (partial facades)
buildings = [
    Object("Half-timbered House", width=5.0, depth=4.0, height=4.0, support=STANDING, color="F5DEB3"),
    Object("Stone Shop", width=4.0, depth=3.5, height=3.5, support=STANDING, color="9C9C9C"),
    Object("Tavern Building", width=6.0, depth=3.8, height=3.8, support=STANDING, color="8B7355"),
    Object("Blacksmith Shop", width=4.5, depth=3.5, height=3.2, support=STANDING, color="A0522D")
]

# Decorative elements
trees = [Object("Oak Tree", width=2.5, depth=2.5, height=3.5, support=STANDING, color="228B22") for _ in range(4)]
benches = [Object("Wooden Bench", width=1.8, depth=0.6, height=0.5, support=STANDING, color="8B5A2B") for _ in range(6)]
cart = Object("Wooden Cart", width=1.5, depth=2.5, height=1.4, support=STANDING, color="B8860B")
horse = Object("Horse", width=0.8, depth=2.0, height=1.6, support=STANDING, color="8B4513")
signposts = [Object("Wooden Sign", width=0.2, depth=0.2, height=2.5, support=STANDING, color="A0522D") for _ in range(3)]
hay_bales = [Object("Hay Bale", width=1.2, depth=0.8, height=0.8, support=STANDING, color="F4A460") for _ in range(5)]

# Blacksmith area
anvil = Object("Anvil", width=0.6, depth=0.4, height=0.8, support=STANDING, color="4F4F4F")
forge = Object("Forge", width=1.2, depth=1.2, height=1.0, support=STANDING, color="8B0000")

# Place central well
well.center.x = scene.center.x
well.center.y = scene.center.y
well.min.z = scene.min.z
well.facing = Y_MAX

# Place buildings around the square
param = 0.8
buildings[0].min.x = scene.min.x + param
buildings[0].min.y = scene.min.y + param
buildings[0].min.z = scene.min.z
buildings[0].facing = X_MAX

buildings[1].max.x = scene.max.x - param
buildings[1].min.y = scene.min.y + param
buildings[1].min.z = scene.min.z
buildings[1].facing = X_MIN

buildings[2].max.x = scene.max.x - param
buildings[2].max.y = scene.max.y - param
buildings[2].min.z = scene.min.z
buildings[2].facing = Y_MIN

buildings[3].min.x = scene.min.x + param
buildings[3].max.y = scene.max.y - param
buildings[3].min.z = scene.min.z
buildings[3].facing = Y_MIN

# Place market stalls in a semi-circle
stall_spacing = 0.25
for i, stall in enumerate(market_stalls):
    angle = (i / len(market_stalls)) * 3.14159  # semi-circle
    radius = 6.0
    stall.center.x = scene.center.x + radius * math.cos(angle)
    stall.center.y = scene.center.y + radius * math.sin(angle)
    stall.min.z = scene.min.z
    stall.facing = well

# Place barrels near market stalls
for i, barrel in enumerate(barrels):
    stall = market_stalls[i % len(market_stalls)]
    set_coordinate_frame(stall)
    barrel.min.x = stall.max.x + 0.2
    barrel.center.y = stall.center.y
    barrel.min.z = scene.min.z
    barrel.facing = stall.facing
set_coordinate_frame(scene)

# Place trees in corners
corner_offset = 3.0
for i, tree in enumerate(trees):
    if i == 0:
        tree.min.x = scene.min.x + corner_offset
        tree.min.y = scene.min.y + corner_offset
    elif i == 1:
        tree.max.x = scene.max.x - corner_offset
        tree.min.y = scene.min.y + corner_offset
    elif i == 2:
        tree.min.x = scene.min.x + corner_offset
        tree.max.y = scene.max.y - corner_offset
    else:
        tree.max.x = scene.max.x - corner_offset
        tree.max.y = scene.max.y - corner_offset
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

# Place benches around well
bench_radius = 4.0
for i, bench in enumerate(benches):
    angle = (i / len(benches)) * 6.28318  # full circle
    bench.center.x = well.center.x + bench_radius * math.cos(angle)
    bench.center.y = well.center.y + bench_radius * math.sin(angle)
    bench.min.z = scene.min.z
    bench.facing = well

# Place cart with horse
cart.min.x = scene.min.x + 8.0
cart.center.y = scene.center.y
cart.min.z = scene.min.z
cart.facing = X_MAX

set_coordinate_frame(cart)
horse.min.x = cart.max.x + 0.5
horse.center.y = cart.center.y
horse.min.z = scene.min.z
horse.facing = cart.facing
set_coordinate_frame(scene)

# Place signposts at key locations
signpost_offset = 2.0
for i, sign in enumerate(signposts):
    if i == 0:
        sign.min.x = buildings[0].max.x + signpost_offset
        sign.min.y = buildings[0].max.y + signpost_offset
    elif i == 1:
        sign.max.x = buildings[1].min.x - signpost_offset
        sign.min.y = buildings[1].max.y + signpost_offset
    else:
        sign.center.x = scene.center.x
        sign.min.y = scene.min.y + signpost_offset
    sign.min.z = scene.min.z
    sign.facing = Y_MAX

# Place blacksmith equipment near blacksmith building
set_coordinate_frame(buildings[3])
anvil.min.x = buildings[3].max.x + 1.0
anvil.min.y = buildings[3].min.y + 1.0
anvil.min.z = scene.min.z
anvil.facing = buildings[3].facing

forge.min.x = anvil.max.x + 0.5
forge.center.y = anvil.center.y
forge.min.z = scene.min.z
forge.facing = anvil.facing
set_coordinate_frame(scene)

# Place hay bales near the cart
for i, hay in enumerate(hay_bales):
    hay.min.x = cart.min.x - (i + 1.0) * 1.5
    hay.center.y = cart.center.y + (i % 2) * 1.0
    hay.min.z = scene.min.z
    hay.facing = X_MAX

# Place crates near market stalls
for i, crate in enumerate(crates):
    stall = market_stalls[i % len(market_stalls)]
    set_coordinate_frame(stall)
    crate.min.x = stall.min.x - 0.8
    crate.center.y = stall.center.y
    crate.min.z = scene.min.z
    crate.facing = stall.facing
set_coordinate_frame(scene)