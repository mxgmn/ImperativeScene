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