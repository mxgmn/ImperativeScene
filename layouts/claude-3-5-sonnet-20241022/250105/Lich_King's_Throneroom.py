set_title("Lich King's Throneroom")
set_size(width=20, depth=25, height=6)
set_floor_asset("Dark Stone Floor", color="2F4F4F")
set_wall_asset("Ice Wall", interior=True, color="A5C5D6")

entrance = Door("Massive Door", width=3.0, depth=0.3, height=4.0, color="4A4A4A")
windows = [Window("Ice Window", width=1.5, depth=0.2, height=3.0, color="E0FFFF") for _ in range(6)]

# The centerpiece
throne = Object("Ice Throne", width=3.0, depth=2.5, height=4.0, support=STANDING, color="87CEEB")

# Ceremonial objects
braziers = [Object("Ice Brazier", width=1.0, depth=1.0, height=1.5, support=STANDING, color="00BFFF") for _ in range(6)]
skull_pillars = [Object("Skull Pillar", width=1.2, depth=1.2, height=4.0, support=STANDING, color="483D8B") for _ in range(8)]
weapon_racks = [Object("Weapon Rack", width=2.0, depth=0.4, height=2.0, support=STANDING, color="4682B4") for _ in range(4)]

# Decorative elements
ice_statues = [Object("Ice Statue", width=1.5, depth=1.5, height=3.0, support=STANDING, color="B0E0E6") for _ in range(4)]
bone_piles = [Object("Bone Pile", width=1.0, depth=1.0, height=0.6, support=STANDING, color="E6E6FA") for _ in range(6)]
runestones = [Object("Runestone", width=0.8, depth=0.8, height=1.8, support=STANDING, color="9370DB") for _ in range(4)]

# Steps leading to throne
steps = Object("Stone Steps", width=5.0, depth=3.0, height=1.0, support=STANDING, color="4B0082")

# Magical elements
magic_circle = Object("Magic Circle", width=4.0, depth=4.0, height=0.1, support=STANDING, color="7B68EE")
soul_crystals = [Object("Soul Crystal", width=0.5, depth=0.5, height=1.2, support=STANDING, color="00FF7F") for _ in range(4)]

# Banners
banners = [Object("Ice Banner", width=1.0, depth=0.1, height=3.0, support=MOUNTED, color="191970") for _ in range(8)]

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

for i, window in enumerate(windows):
    if i < 3:
        window.min.x = scene.min.x
        window.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
        window.facing = X_MAX
    else:
        window.max.x = scene.max.x
        window.center.y = scene.min.y + (i-2.0) / 4.0 * scene.depth
        window.facing = X_MIN
    window.min.z = scene.max.z - 4.0

throne.center.x = scene.center.x
throne.max.y = scene.max.y - 1.0
throne.min.z = scene.min.z
throne.facing = Y_MIN

steps.center.x = throne.center.x
steps.max.y = throne.min.y
steps.min.z = scene.min.z
steps.facing = throne.facing

magic_circle.center.x = scene.center.x
magic_circle.center.y = scene.center.y
magic_circle.min.z = scene.min.z

param = 0.4
for i, crystal in enumerate(soul_crystals):
    crystal.center.x = magic_circle.center.x + (1.0 if i % 2 == 0 else -1.0) * param * magic_circle.width
    crystal.center.y = magic_circle.center.y + (1.0 if i < 2 else -1.0) * param * magic_circle.depth
    crystal.min.z = magic_circle.max.z
    crystal.facing = Y_MIN

param = 0.25
for i, brazier in enumerate(braziers):
    if i < 3:
        brazier.min.x = scene.min.x + param * scene.width
        brazier.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    else:
        brazier.max.x = scene.max.x - param * scene.width
        brazier.center.y = scene.min.y + (i-2.0) / 4.0 * scene.depth
    brazier.min.z = scene.min.z

for i, pillar in enumerate(skull_pillars):
    if i < 4:
        pillar.min.x = scene.min.x + (i+1.0) / 5.0 * scene.width
        pillar.max.y = scene.max.y - param * scene.depth
    else:
        pillar.min.x = scene.min.x + (i-3.0) / 5.0 * scene.width
        pillar.min.y = scene.min.y + param * scene.depth
    pillar.min.z = scene.min.z

for i, rack in enumerate(weapon_racks):
    if i < 2:
        rack.min.x = scene.min.x
        rack.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
        rack.facing = X_MAX
    else:
        rack.max.x = scene.max.x
        rack.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
        rack.facing = X_MIN
    rack.min.z = scene.min.z

for i, statue in enumerate(ice_statues):
    statue.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    statue.max.y = scene.max.y - 2.0
    statue.min.z = scene.min.z
    statue.facing = Y_MIN

for i, pile in enumerate(bone_piles):
    pile.center.x = scene.min.x + (i+1.0) / 7.0 * scene.width
    pile.min.y = scene.min.y + param * scene.depth
    pile.min.z = scene.min.z

for i, stone in enumerate(runestones):
    stone.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    stone.min.y = scene.min.y + 2.0 * param * scene.depth
    stone.min.z = scene.min.z
    stone.facing = Y_MAX

for i, banner in enumerate(banners):
    if i < 4:
        banner.min.x = scene.min.x
        banner.center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
        banner.facing = X_MAX
    else:
        banner.max.x = scene.max.x
        banner.center.y = scene.min.y + (i-3.0) / 5.0 * scene.depth
        banner.facing = X_MIN
    banner.min.z = scene.max.z - 3.5