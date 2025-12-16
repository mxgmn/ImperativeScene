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