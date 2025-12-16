set_title("Depths of Hell")
set_size(width=25, depth=25, height=5)
set_floor_asset("Volcanic Rock Floor", color="1A0F0F")
set_wall_asset("Obsidian Wall", interior=True, color="2A1F1F")

# Main features
throne = Object("Demon Throne", width=3.0, depth=2.5, height=4.0, support=STANDING, color="8B0000")
altar = Object("Sacrificial Altar", width=2.0, depth=1.2, height=1.0, support=STANDING, color="4A0404")
braziers = [Object("Brazier", width=0.8, depth=0.8, height=1.2, support=STANDING, color="FF4500") for _ in range(6)]

# Architecture
pillars = [Object("Hell Pillar", width=1.2, depth=1.2, height=5.0, support=STANDING, color="3B1111") for _ in range(8)]
skull_piles = [Object("Skull Pile", width=1.5, depth=1.5, height=0.8, support=STANDING, color="E5D3B3") for _ in range(4)]
bone_gates = [Object("Bone Gate", width=2.0, depth=0.3, height=3.0, support=STANDING, color="D3D3D3") for _ in range(2)]

# Decorative elements
statues = [Object("Demon Statue", width=1.0, depth=1.0, height=2.5, support=STANDING, color="8B0000") for _ in range(4)]
weapon_racks = [Object("Weapon Rack", width=2.0, depth=0.4, height=2.0, support=STANDING, color="B8860B") for _ in range(3)]
chains = [Object("Chain Post", width=0.3, depth=0.3, height=1.5, support=STANDING, color="CD853F") for _ in range(6)]

# Special features
portal = Object("Hell Portal", width=3.0, depth=0.5, height=4.0, support=STANDING, color="FF1493")
cauldron = Object("Soul Cauldron", width=1.5, depth=1.5, height=1.2, support=STANDING, color="9400D3")
torture_rack = Object("Torture Rack", width=2.0, depth=1.0, height=0.8, support=STANDING, color="8B4513")

# Wall decorations
wall_torches = [Object("Wall Torch", width=0.3, depth=0.2, height=0.8, support=MOUNTED, color="FFA500") for _ in range(12)]
skull_plaques = [Object("Skull Plaque", width=0.5, depth=0.2, height=0.6, support=MOUNTED, color="F5DEB3") for _ in range(8)]

# Central throne and altar setup
throne.center.x = scene.center.x
throne.max.y = scene.max.y - 0.1 * scene.depth
throne.min.z = scene.min.z
throne.facing = Y_MIN

altar.center.x = scene.center.x
altar.center.y = scene.center.y
altar.min.z = scene.min.z
altar.facing = throne

# Braziers in hexagonal pattern around throne
angle_step = 60.0
radius = 0.2 * scene.width
for i, brazier in enumerate(braziers):
    angle = i * angle_step
    brazier.center.x = throne.center.x + radius * math.cos(math.radians(angle))
    brazier.center.y = throne.center.y + radius * math.sin(math.radians(angle))
    brazier.min.z = scene.min.z
    brazier.facing = throne

# Pillars in octagonal pattern
angle_step = 45.0
radius = 0.35 * scene.width
for i, pillar in enumerate(pillars):
    angle = i * angle_step
    pillar.center.x = scene.center.x + radius * math.cos(math.radians(angle))
    pillar.center.y = scene.center.y + radius * math.sin(math.radians(angle))
    pillar.min.z = scene.min.z
    pillar.facing = throne

# Skull piles in corners
corner_offset = 0.15 * scene.width
for i, pile in enumerate(skull_piles):
    pile.center.x = scene.min.x + corner_offset if i < 2 else scene.max.x - corner_offset
    pile.center.y = scene.min.y + corner_offset if i % 2 == 0 else scene.max.y - corner_offset
    pile.min.z = scene.min.z
    pile.facing = throne

# Gates on opposite sides
bone_gates[0].center.x = scene.center.x
bone_gates[0].min.y = scene.min.y
bone_gates[0].min.z = scene.min.z
bone_gates[0].facing = Y_MAX

bone_gates[1].center.x = scene.center.x
bone_gates[1].max.y = scene.max.y
bone_gates[1].min.z = scene.min.z
bone_gates[1].facing = Y_MIN

# Statues near pillars
statue_radius = 0.25 * scene.width
for i, statue in enumerate(statues):
    angle = i * 90.0
    statue.center.x = scene.center.x + statue_radius * math.cos(math.radians(angle))
    statue.center.y = scene.center.y + statue_radius * math.sin(math.radians(angle))
    statue.min.z = scene.min.z
    statue.facing = throne

# Weapon racks along walls
spacing = 0.25 * scene.width
for i, rack in enumerate(weapon_racks):
    rack.min.x = scene.min.x + (i + 1.0) * spacing
    rack.min.y = scene.min.y + 0.1 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = Y_MAX

# Chain posts in semi-circle
chain_radius = 0.3 * scene.width
for i, chain in enumerate(chains):
    angle = i * 36.0
    chain.center.x = throne.center.x + chain_radius * math.cos(math.radians(angle))
    chain.center.y = throne.center.y + chain_radius * math.sin(math.radians(angle))
    chain.min.z = scene.min.z
    chain.facing = throne

# Special features placement
portal.max.x = scene.max.x - 0.1 * scene.width
portal.center.y = scene.center.y
portal.min.z = scene.min.z
portal.facing = X_MIN

cauldron.min.x = scene.min.x + 0.1 * scene.width
cauldron.center.y = scene.center.y
cauldron.min.z = scene.min.z
cauldron.facing = X_MAX

torture_rack.min.x = scene.min.x + 0.15 * scene.width
torture_rack.min.y = scene.min.y + 0.15 * scene.depth
torture_rack.min.z = scene.min.z
torture_rack.facing = X_MAX

# Wall decorations
for i, torch in enumerate(wall_torches):
    if i < 6:
        torch.center.x = scene.min.x + (i + 1.0) / 7.0 * scene.width
        torch.min.y = scene.min.y
    else:
        torch.center.x = scene.min.x + (i - 5.0) / 7.0 * scene.width
        torch.max.y = scene.max.y
    torch.min.z = 1.5
    torch.facing = Y_MAX if i < 6 else Y_MIN

for i, plaque in enumerate(skull_plaques):
    if i < 4:
        plaque.min.x = scene.min.x
        plaque.center.y = scene.min.y + (i + 1.0) / 5.0 * scene.depth
        plaque.facing = X_MAX
    else:
        plaque.max.x = scene.max.x
        plaque.center.y = scene.min.y + (i - 3.0) / 5.0 * scene.depth
        plaque.facing = X_MIN
    plaque.min.z = 1.8