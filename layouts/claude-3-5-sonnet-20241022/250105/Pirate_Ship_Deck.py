set_title("Pirate Ship Deck")
set_size(width=8, depth=24, height=5)
set_floor_asset("Wooden Planks Floor", color="8B4513")
set_wall_asset("Ship Railing", interior=False, color="A0522D")

# Main ship features
mast = Object("Ship Mast", width=0.5, depth=0.5, height=5.0, support=STANDING, color="8B4513")
helm = Object("Ship Wheel", width=1.2, depth=0.3, height=1.2, support=STANDING, color="DEB887")
capstan = Object("Capstan", width=1.0, depth=1.0, height=1.0, support=STANDING, color="CD853F")

# Storage and cargo
barrels = [Object("Wooden Barrel", width=0.8, depth=0.8, height=1.2, support=STANDING, color="B8860B") for _ in range(6)]
crates = [Object("Wooden Crate", width=1.0, depth=1.0, height=0.8, support=STANDING, color="DAA520") for _ in range(4)]

# Ship equipment
anchor = Object("Ship Anchor", width=1.5, depth=0.4, height=2.0, support=STANDING, color="708090")
cannon_left = [Object("Ship Cannon", width=0.6, depth=1.8, height=0.8, support=STANDING, color="4A4A4A") for _ in range(3)]
cannon_right = [Object("Ship Cannon", width=0.6, depth=1.8, height=0.8, support=STANDING, color="4A4A4A") for _ in range(3)]

# Navigation equipment
map_table = Object("Navigation Table", width=1.2, depth=0.8, height=0.8, support=STANDING, color="8B4513")
compass = Object("Ship Compass", width=0.3, depth=0.3, height=0.2, support=STANDING, color="CD853F")

# Crew areas
benches = [Object("Wooden Bench", width=1.8, depth=0.4, height=0.5, support=STANDING, color="A0522D") for _ in range(2)]
rope_coils = [Object("Rope Coil", width=0.6, depth=0.6, height=0.3, support=STANDING, color="DEB887") for _ in range(3)]

# Access points
hatch = Object("Ship Hatch", width=1.0, depth=1.0, height=0.1, support=STANDING, color="8B4513")

# Central mast placement
mast.center.x = scene.center.x
mast.center.y = scene.center.y
mast.min.z = scene.min.z
mast.facing = Y_MAX

# Helm at the back of the ship
helm.center.x = scene.center.x
helm.max.y = scene.max.y - 0.5
helm.min.z = scene.min.z + 0.8
helm.facing = Y_MIN

# Capstan placement
capstan.center.x = scene.center.x
capstan.center.y = scene.center.y + 0.25 * scene.depth
capstan.min.z = scene.min.z
capstan.facing = Y_MAX

# Map table near helm
map_table.center.x = helm.center.x + 1.5
map_table.max.y = helm.max.y - 0.5
map_table.min.z = scene.min.z
map_table.facing = Y_MIN

set_coordinate_frame(map_table)
compass.center.x = map_table.center.x
compass.center.y = map_table.center.y
compass.min.z = map_table.max.z
compass.facing = map_table.facing
set_coordinate_frame(scene)

# Cannons placement
spacing = 0.25 * scene.depth
for i, (left, right) in enumerate(zip(cannon_left, cannon_right)):
    y_pos = scene.min.y + (i + 1.0) * spacing
    
    left.min.x = scene.min.x + 0.5
    left.center.y = y_pos
    left.min.z = scene.min.z
    left.facing = X_MIN
    
    right.max.x = scene.max.x - 0.5
    right.center.y = y_pos
    right.min.z = scene.min.z
    right.facing = X_MAX

# Barrels grouped near the front
barrel_spacing = 1.2
for i, barrel in enumerate(barrels):
    if i < 3:
        barrel.center.x = scene.min.x + (i + 1.0) * barrel_spacing
        barrel.center.y = scene.min.y + 0.25 * scene.depth
    else:
        barrel.center.x = scene.min.x + (i - 2.0) * barrel_spacing
        barrel.center.y = scene.min.y + 0.4 * scene.depth
    barrel.min.z = scene.min.z
    barrel.facing = Y_MAX

# Crates stacked near the middle
for i, crate in enumerate(crates):
    crate.center.x = scene.max.x - (i + 1.0) * 1.2
    crate.center.y = scene.center.y
    crate.min.z = scene.min.z
    crate.facing = Y_MAX

# Anchor placement
anchor.max.x = scene.max.x - 0.2
anchor.min.y = scene.min.y + 0.15 * scene.depth
anchor.min.z = scene.min.z
anchor.facing = X_MIN

# Benches placement
for i, bench in enumerate(benches):
    bench.center.x = scene.center.x + (1.0 if i == 0 else -1.0) * 2.0
    bench.center.y = scene.center.y - 0.2 * scene.depth
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

# Rope coils scattered around
for i, rope in enumerate(rope_coils):
    rope.center.x = scene.min.x + (i + 1.0) * 1.5
    rope.max.y = scene.max.y - 0.2 * scene.depth
    rope.min.z = scene.min.z
    rope.facing = Y_MIN

# Hatch placement
hatch.center.x = scene.center.x
hatch.center.y = scene.center.y - 0.25 * scene.depth
hatch.min.z = scene.min.z
hatch.facing = Y_MAX