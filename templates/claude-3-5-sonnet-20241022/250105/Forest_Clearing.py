set_title("Forest Clearing")
set_size(width=20, depth=20, height=8)
set_floor_asset("Grass Floor", color="4A5D23")
set_wall_asset("Forest Background", interior=False, color="2F4F2F")

# Main trees forming the clearing border
trees = [Object("Pine Tree", width=2.0, depth=2.0, height=7.0, support=STANDING, color="2E8B57") for _ in range(15)]
birch_trees = [Object("Birch Tree", width=1.2, depth=1.2, height=6.0, support=STANDING, color="F5DEB3") for _ in range(6)]

# Focal point - large boulder formation
boulders = [
    Object("Large Boulder", width=2.5, depth=2.0, height=1.8, support=STANDING, color="808080"),
    Object("Medium Boulder", width=1.8, depth=1.5, height=1.2, support=STANDING, color="A9A9A9"),
    Object("Small Boulder", width=1.2, depth=1.0, height=0.8, support=STANDING, color="B8B8B8")
]

# Ground details
mushrooms = [Object("Mushroom", width=0.3, depth=0.3, height=0.4, support=STANDING, color="FF8C69") for _ in range(6)]
fallen_logs = [Object("Fallen Log", width=0.8, depth=2.5, height=0.6, support=STANDING, color="8B4513") for _ in range(3)]
bushes = [Object("Bush", width=1.0, depth=1.0, height=1.2, support=STANDING, color="228B22") for _ in range(8)]

# Wildlife elements
deer = Object("Deer Statue", width=1.2, depth=1.8, height=1.5, support=STANDING, color="D2B48C")
bird_bath = Object("Bird Bath", width=0.8, depth=0.8, height=1.0, support=STANDING, color="E6E6FA")

# Mystical elements
standing_stones = [Object("Standing Stone", width=0.6, depth=0.4, height=1.8, support=STANDING, color="708090") for _ in range(3)]
altar_stone = Object("Stone Altar", width=1.2, depth=0.8, height=1.0, support=STANDING, color="B8860B")

# Ground cover
ferns = [Object("Fern", width=0.6, depth=0.6, height=0.4, support=STANDING, color="3CB371") for _ in range(8)]