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