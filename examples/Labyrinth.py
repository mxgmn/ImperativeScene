set_title("Mysterious Labyrinth")
set_size(width=30, depth=30, height=3)
set_floor_asset("Stone Floor")
set_wall_asset("Stone Wall", interior=False)

# Define the labyrinth layout: 0 represents a path, 1 represents a wall
layout = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0],
    [1,0,1,1,1,0,1,0,1,0],
    [1,0,0,0,1,0,1,0,1,0],
    [0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [1,0,1,1,1,0,1,0,1,1],
    [1,0,0,0,0,0,1,0,0,0],
    [1,1,1,0,1,1,1,0,1,0],
    [1,0,0,0,0,0,0,0,1,0]
]

# Function to create wall segments
def create_wall(x, y, width, depth):
    wall = Object("Stone Wall Segment", width, depth, height=3, support=STANDING, dynamic=False)
    wall.min.x = x
    wall.min.y = y
    wall.min.z = scene.min.z
    wall.facing = center(scene)
    return wall

# Create the labyrinth walls
cell_size = 3  # Each cell is 3x3 meters
for i in range(10):
    for j in range(10):
        if layout[i][j] == 1:
            x = -15 + j * cell_size
            y = -15 + i * cell_size
            create_wall(x, y, cell_size, cell_size)

exits = [Door("Stone Arch", width=2, depth=0.5, height=2.5) for _ in range(2)]
statue = Object("Ancient Statue", width=1.5, depth=1.5, height=2.5, support=STANDING, dynamic=False)

for i, exit in enumerate(exits):
    if i % 2 == 0:
        exit.min.x = scene.min.x
        exit.facing = X_MAX
    else:
        exit.max.x = scene.max.x
        exit.facing = X_MIN
exit.center.y = scene.center.y
exit.min.z = scene.min.z

statue.center.x = scene.center.x
statue.center.y = scene.center.x
statue.min.z = scene.min.z
statue.facing = entrance