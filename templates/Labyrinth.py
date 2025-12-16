set_title("Labyrinth")
set_size(width=11+4, depth=11+4, height=3) # The main labyrinth will be 11x11, plus a border of 2 meters from every side
set_floor_asset("Stone Tile Floor", color="8A8774")
set_wall_asset("Hedge Wall", interior=False, color="57724F")

# The main objects in a labyrinth are walls, we will initalize them with special care
layout = [
    [1,1,1,1,1,0,1,1,1,1,1],
    [0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0],
    [1,0,1,1,1,1,1,0,1,1,1],
    [0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,1,1]
]

num_walls = sum(sum(row) for row in layout)
walls = [Object("Stone Wall", width=1.0, depth=1.0, height=2.0, support=STANDING, color="708090") for _ in range(num_walls)]

# Decorative and atmospheric elements
statues = [Object("Stone Statue", width=0.8, depth=0.8, height=2.0, support=STANDING, color="B8860B") for _ in range(4)]
pedestals = [Object("Stone Pedestal", width=0.6, depth=0.6, height=0.8, support=STANDING, color="DEB887") for _ in range(4)]

# Central feature
altar = Object("Stone Altar", width=1.0, depth=1.0, height=1.5, support=STANDING, color="DAA520")