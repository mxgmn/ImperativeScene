set_title("Circus Ring")
set_size(width=15, depth=15, height=6)
set_floor_asset("Sawdust Floor", color="D2B48C")
set_wall_asset("Striped Wall", interior=True, color="F5F5DC")

entrance_door = Door("Double Door", width=2.0, depth=0.1, height=2.2, color="8B0000")
backstage_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")

# Main performance area
ring = Object("Circus Ring", width=8.0, depth=8.0, height=0.1, support=STANDING, color="FFD700")

bleachers = [Object("Bleacher Section", width=7.5, depth=1.2, height=0.8, support=STANDING, color="8B4513") for _ in range(4)]

# Performance equipment
trampoline = Object("Trampoline", width=2.0, depth=2.0, height=0.4, support=STANDING, color="4169E1")
balance_beam = Object("Balance Beam", width=0.2, depth=4.0, height=1.2, support=STANDING, color="CD853F")
pedestals = [
    Object("Performance Pedestal", width=0.6, depth=0.6, height=h, support=STANDING, color="B8860B")
    for h in [0.3, 0.6, 0.9]  # Different heights for variety
]

# Props and equipment
prop_chest = Object("Storage Chest", width=1.2, depth=0.8, height=0.9, support=STANDING, color="8B008B")
safety_mats = [
    Object("Safety Mat", width=2.0, depth=1.5, height=0.2, support=STANDING, color="4B0082")
    for _ in range(3)
]

# Decorative elements
banners = [
    Object("Decorative Banner", width=1.0, depth=0.05, height=2.0, support=MOUNTED, color=color)
    for color in ["FF0000", "FFFF00", "FF1493", "00FF00"]
]

podium = Object("Ringmaster Podium", width=0.8, depth=0.8, height=1.0, support=STANDING, color="DC143C")

# Animal equipment (suggesting presence without actual animals)
cage_cart = Object("Cage Cart", width=1.8, depth=1.2, height=1.5, support=STANDING, color="B8860B")

entrance_door.center.x = scene.min.x + 0.5 * scene.width
entrance_door.min.y = scene.min.y
entrance_door.min.z = scene.min.z
entrance_door.facing = Y_MAX

backstage_door.max.x = scene.max.x
backstage_door.max.y = scene.max.y - 0.2 * scene.depth
backstage_door.min.z = scene.min.z
backstage_door.facing = X_MIN

ring.center.x = scene.center.x
ring.center.y = scene.center.y
ring.min.z = scene.min.z
ring.facing = Y_MAX

# Place bleachers around the ring
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # top, bottom, right, left
for i, bleacher in enumerate(bleachers):
    dx, dy = directions[i]
    bleacher.center.x = ring.center.x + dx * (ring.width/2 + bleacher.depth/2)
    bleacher.center.y = ring.center.y + dy * (ring.depth/2 + bleacher.depth/2)
    bleacher.min.z = scene.min.z
    bleacher.facing = Y_MAX if dy == 1 else (Y_MIN if dy == -1 else (X_MAX if dx == 1 else X_MIN))

trampoline.center.x = ring.center.x - 0.25 * ring.width
trampoline.center.y = ring.center.y + 0.25 * ring.depth
trampoline.min.z = ring.max.z
trampoline.facing = Y_MAX

balance_beam.center.x = ring.center.x + 0.25 * ring.width
balance_beam.center.y = ring.center.y - 0.25 * ring.depth
balance_beam.min.z = ring.max.z
balance_beam.facing = X_MAX

# Arrange pedestals in an arc
param = 0.2
for i, pedestal in enumerate(pedestals):
    angle = (i - 1.0) * param
    pedestal.center.x = ring.center.x + ring.width * 0.25 * angle
    pedestal.center.y = ring.center.y + ring.depth * 0.25
    pedestal.min.z = ring.max.z
    pedestal.facing = Y_MIN

prop_chest.max.x = scene.max.x - 0.1
prop_chest.min.y = scene.min.y + 0.1
prop_chest.min.z = scene.min.z
prop_chest.facing = X_MIN

# Place safety mats near performance equipment
set_coordinate_frame(trampoline)
safety_mats[0].center.x = trampoline.center.x
safety_mats[0].min.y = trampoline.max.y + 0.1
safety_mats[0].min.z = scene.min.z
safety_mats[0].facing = trampoline.facing
set_coordinate_frame(scene)

set_coordinate_frame(balance_beam)
safety_mats[1].min.x = balance_beam.max.x + 0.1
safety_mats[1].center.y = balance_beam.center.y
safety_mats[1].min.z = scene.min.z
safety_mats[1].facing = balance_beam.facing
set_coordinate_frame(scene)

safety_mats[2].center.x = ring.center.x
safety_mats[2].min.y = ring.min.y + 0.1
safety_mats[2].min.z = scene.min.z
safety_mats[2].facing = Y_MAX

# Hang banners around the ring
for i, banner in enumerate(banners):
    banner.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    banner.max.y = scene.max.y
    banner.min.z = 3.0
    banner.facing = Y_MIN

podium.center.x = ring.center.x
podium.min.y = ring.min.y - 0.5
podium.min.z = ring.max.z
podium.facing = Y_MAX

cage_cart.min.x = scene.min.x + 0.1
cage_cart.max.y = scene.max.y - 0.1
cage_cart.min.z = scene.min.z
cage_cart.facing = X_MAX