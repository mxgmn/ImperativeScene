set_title("Graveyard")
set_size(width=15, depth=15, height=3)
set_floor_asset("Grass Floor", color="3B4D2D")
set_wall_asset("Stone Wall", interior=False, color="6B7275")

entrance_gate = Door("Iron Gate", width=2.0, depth=0.15, height=2.5, color="4A4A4A")

# Main path through the graveyard
path = Object("Gravel Path", width=2.0, depth=12.0, height=0.05, support=STANDING, color="9B9B9B")

# Gravestones of various sizes
gravestones_large = [Object("Large Gravestone", width=0.8, depth=0.3, height=1.5, support=STANDING, color="8B8B83") for _ in range(6)]
gravestones_small = [Object("Small Gravestone", width=0.5, depth=0.2, height=0.8, support=STANDING, color="A39F93") for _ in range(8)]

# Decorative elements
statues = [Object("Angel Statue", width=0.8, depth=0.8, height=2.0, support=STANDING, color="E6E6E6") for _ in range(2)]
benches = [Object("Stone Bench", width=1.2, depth=0.4, height=0.5, support=STANDING, color="8B8378") for _ in range(3)]

# Vegetation
trees = [Object("Dead Tree", width=1.5, depth=1.5, height=3.0, support=STANDING, color="4A3728") for _ in range(4)]
bushes = [Object("Bush", width=1.0, depth=1.0, height=0.8, support=STANDING, color="2F4F2F") for _ in range(6)]

# Central feature
mausoleum = Object("Mausoleum", width=3.0, depth=4.0, height=2.8, support=STANDING, color="7D7D72")

# Decorative urns
urns = [Object("Stone Urn", width=0.4, depth=0.4, height=0.6, support=STANDING, color="696969") for _ in range(4)]

# Cross monuments
crosses = [Object("Stone Cross", width=0.4, depth=0.4, height=1.8, support=STANDING, color="B8B8B8") for _ in range(3)]