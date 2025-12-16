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