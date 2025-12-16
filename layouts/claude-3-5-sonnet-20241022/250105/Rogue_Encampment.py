set_title("Rogue Encampment")
set_size(width=25, depth=20, height=3)
set_floor_asset("Dirt Ground", color="8B7355")
set_wall_asset("Wooden Palisade", interior=False, color="8B4513")

# Main structures
tents = [Object("Large Tent", width=3.0, depth=4.0, height=2.5, support=STANDING, color="8B4513") for _ in range(3)]
small_tents = [Object("Small Tent", width=2.0, depth=2.5, height=1.8, support=STANDING, color="CD853F") for _ in range(4)]

# Campsite elements
campfires = [Object("Campfire", width=1.0, depth=1.0, height=0.3, support=STANDING, color="FF4500") for _ in range(2)]
logs = [Object("Log Bench", width=1.8, depth=0.4, height=0.5, support=STANDING, color="8B7355") for _ in range(6)]

# Military/Defense elements
watchtower = Object("Wooden Tower", width=2.5, depth=2.5, height=3.0, support=STANDING, color="A0522D")
barricades = [Object("Wooden Barricade", width=2.0, depth=0.3, height=1.2, support=STANDING, color="DEB887") for _ in range(4)]
weapon_rack = Object("Weapon Rack", width=2.0, depth=0.4, height=1.8, support=STANDING, color="A0522D")

# Storage and supplies
supply_crates = [Object("Wooden Crate", width=1.0, depth=1.0, height=1.0, support=STANDING, color="DEB887") for _ in range(6)]
barrel = Object("Barrel", width=0.8, depth=0.8, height=1.2, support=STANDING, color="8B4513")
cart = Object("Wooden Cart", width=1.5, depth=2.5, height=1.2, support=STANDING, color="CD853F")

# Training area
training_dummy = Object("Training Dummy", width=0.8, depth=0.8, height=1.8, support=STANDING, color="DAA520")
archery_target = Object("Archery Target", width=1.0, depth=0.3, height=1.5, support=STANDING, color="B8860B")

# Misc decorative elements
banners = [Object("Tattered Banner", width=0.8, depth=0.1, height=2.0, support=MOUNTED, color="8B0000") for _ in range(3)]
torches = [Object("Torch Holder", width=0.2, depth=0.2, height=0.4, support=MOUNTED, color="FFA500") for _ in range(6)]

# Place main tents in a semi-circle formation
for i, tent in enumerate(tents):
    angle = 0.2 + i * 0.3
    tent.center.x = scene.center.x + 0.35 * scene.width * math.cos(angle)
    tent.center.y = scene.center.y + 0.35 * scene.depth * math.sin(angle)
    tent.min.z = scene.min.z
    tent.facing = Y_MIN

# Place smaller tents around the perimeter
for i, tent in enumerate(small_tents):
    angle = 0.8 + i * 0.4
    tent.center.x = scene.center.x + 0.25 * scene.width * math.cos(angle)
    tent.center.y = scene.center.y + 0.25 * scene.depth * math.sin(angle)
    tent.min.z = scene.min.z
    tent.facing = Y_MIN

# Place campfires with surrounding logs
for i, campfire in enumerate(campfires):
    campfire.center.x = scene.center.x + (0.15 if i == 0 else -0.15) * scene.width
    campfire.center.y = scene.center.y
    campfire.min.z = scene.min.z
    
    # Place logs around each campfire
    for j in range(3):
        log = logs[i*3 + j]
        angle = j * 2.0 * math.pi / 3.0
        offset = 0.8
        log.center.x = campfire.center.x + offset * math.cos(angle)
        log.center.y = campfire.center.y + offset * math.sin(angle)
        log.min.z = scene.min.z
        log.facing = campfire

# Place watchtower near entrance
watchtower.min.x = scene.min.x + 0.1 * scene.width
watchtower.min.y = scene.min.y + 0.1 * scene.depth
watchtower.min.z = scene.min.z
watchtower.facing = Y_MAX

# Place barricades strategically
for i, barricade in enumerate(barricades):
    if i < 2:
        barricade.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
        barricade.min.y = scene.min.y + 0.1 * scene.depth
    else:
        barricade.center.x = scene.min.x + ((i-1)+1.0) / 3.0 * scene.width
        barricade.max.y = scene.max.y - 0.1 * scene.depth
    barricade.min.z = scene.min.z
    barricade.facing = Y_MAX if i < 2 else Y_MIN

# Place weapon rack near training area
weapon_rack.max.x = scene.max.x - 0.1 * scene.width
weapon_rack.center.y = scene.center.y
weapon_rack.min.z = scene.min.z
weapon_rack.facing = X_MIN

# Group supply crates together
param = 0.8
for i, crate in enumerate(supply_crates):
    crate.center.x = scene.max.x - 0.15 * scene.width + (i % 2) * param
    crate.center.y = scene.min.y + 0.2 * scene.depth + (i // 2) * param
    crate.min.z = scene.min.z
    crate.facing = X_MIN

# Place barrel and cart near supplies
barrel.center.x = supply_crates[0].center.x - param
barrel.center.y = supply_crates[0].center.y
barrel.min.z = scene.min.z
barrel.facing = X_MAX

cart.center.x = barrel.center.x - param
cart.center.y = barrel.center.y
cart.min.z = scene.min.z
cart.facing = X_MAX

# Set up training area
training_dummy.max.x = scene.max.x - 0.15 * scene.width
training_dummy.max.y = scene.max.y - 0.15 * scene.depth
training_dummy.min.z = scene.min.z
training_dummy.facing = X_MIN

archery_target.max.x = training_dummy.max.x
archery_target.center.y = training_dummy.center.y - 2.0
archery_target.min.z = scene.min.z
archery_target.facing = X_MIN

# Place decorative elements
for i, banner in enumerate(banners):
    banner.center.x = scene.center.x + (i-1.0) * 0.2 * scene.width
    banner.max.y = scene.max.y - 0.05 * scene.depth
    banner.min.z = 0.5
    banner.facing = Y_MIN

for i, torch in enumerate(torches):
    if i < 3:
        torch.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
        torch.min.y = scene.min.y
    else:
        torch.center.x = scene.min.x + (i-2.0) / 4.0 * scene.width
        torch.max.y = scene.max.y
    torch.min.z = 1.5
    torch.facing = Y_MAX if i < 3 else Y_MIN