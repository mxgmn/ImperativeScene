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