set_title("Hedge Maze")
set_size(width=30, depth=30, height=3)
set_floor_asset("Grass Floor", color="4A5D32")
set_wall_asset("Stone Wall", interior=False, color="8B8B83")

entrance = Object("Stone Archway", width=2.0, depth=1.0, height=2.5, support=STANDING, color="9C9C9C")

# Main hedge sections (using larger sections instead of small pieces for better performance)
hedge_sections = [
    Object("Hedge Wall", width=8.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=12.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=15.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=10.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=6.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=14.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=9.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=11.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=7.0, depth=0.8, height=2.2, support=STANDING, color="355E3B"),
    Object("Hedge Wall", width=13.0, depth=0.8, height=2.2, support=STANDING, color="355E3B")
]

# Decorative elements
fountains = [Object("Stone Fountain", width=2.0, depth=2.0, height=1.5, support=STANDING, color="7B8B8B") for _ in range(3)]
benches = [Object("Garden Bench", width=1.2, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(4)]
statues = [Object("Garden Statue", width=0.8, depth=0.8, height=1.8, support=STANDING, color="B8860B") for _ in range(6)]
planters = [Object("Stone Planter", width=1.0, depth=1.0, height=0.6, support=STANDING, color="696969") for _ in range(8)]
topiaries = [Object("Topiary Bush", width=0.8, depth=0.8, height=1.5, support=STANDING, color="228B22") for _ in range(6)]
gazebo = Object("Garden Gazebo", width=3.0, depth=3.0, height=2.8, support=STANDING, color="DEB887")

# Dead ends decorations
urns = [Object("Garden Urn", width=0.6, depth=0.6, height=1.0, support=STANDING, color="8B7355") for _ in range(5)]
sundial = Object("Sundial", width=0.8, depth=0.8, height=1.2, support=STANDING, color="CD853F")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

# Create the main maze paths
offset = 0.25 # relative offset for positioning
hedge_sections[0].center.x = scene.min.x + offset * scene.width
hedge_sections[0].center.y = scene.min.y + 0.3 * scene.depth
hedge_sections[0].min.z = scene.min.z
hedge_sections[0].facing = Y_MAX

hedge_sections[1].center.x = scene.min.x + (1.0 - offset) * scene.width
hedge_sections[1].center.y = scene.min.y + 0.4 * scene.depth
hedge_sections[1].min.z = scene.min.z
hedge_sections[1].facing = X_MAX

hedge_sections[2].center.x = scene.min.x + 0.4 * scene.width
hedge_sections[2].center.y = scene.min.y + 0.6 * scene.depth
hedge_sections[2].min.z = scene.min.z
hedge_sections[2].facing = Y_MAX

hedge_sections[3].center.x = scene.min.x + 0.7 * scene.width
hedge_sections[3].center.y = scene.min.y + 0.7 * scene.depth
hedge_sections[3].min.z = scene.min.z
hedge_sections[3].facing = X_MIN

hedge_sections[4].center.x = scene.min.x + 0.3 * scene.width
hedge_sections[4].center.y = scene.min.y + (1.0 - offset) * scene.depth
hedge_sections[4].min.z = scene.min.z
hedge_sections[4].facing = Y_MIN

# Place decorative elements at maze intersections
fountains[0].center.x = scene.min.x + 0.25 * scene.width
fountains[0].center.y = scene.min.y + 0.25 * scene.depth
fountains[0].min.z = scene.min.z
fountains[0].facing = Y_MAX

fountains[1].center.x = scene.min.x + 0.75 * scene.width
fountains[1].center.y = scene.min.y + 0.5 * scene.depth
fountains[1].min.z = scene.min.z
fountains[1].facing = X_MAX

fountains[2].center.x = scene.min.x + 0.5 * scene.width
fountains[2].center.y = scene.min.y + 0.75 * scene.depth
fountains[2].min.z = scene.min.z
fountains[2].facing = Y_MIN

# Place benches along the paths
param = 0.2
for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    bench.center.y = scene.min.y + param * scene.depth
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

# Place statues at strategic points
param = 0.15
for i, statue in enumerate(statues):
    statue.center.x = scene.min.x + (i+1.0) / 7.0 * scene.width
    statue.center.y = scene.min.y + (1.0 - param) * scene.depth
    statue.min.z = scene.min.z
    statue.facing = Y_MIN

# Place the gazebo at the maze center
gazebo.center.x = scene.center.x
gazebo.center.y = scene.center.y
gazebo.min.z = scene.min.z
gazebo.facing = Y_MAX

# Place planters along the hedge walls
param = 0.1
for i, planter in enumerate(planters):
    planter.center.x = scene.min.x + (i+1.0) / 9.0 * scene.width
    planter.center.y = scene.min.y + param * scene.depth
    planter.min.z = scene.min.z
    planter.facing = Y_MAX

# Place topiaries at maze corners
param = 0.85
for i, topiary in enumerate(topiaries):
    topiary.center.x = scene.min.x + param * scene.width
    topiary.center.y = scene.min.y + (i+1.0) / 7.0 * scene.depth
    topiary.min.z = scene.min.z
    topiary.facing = X_MIN

# Place urns at dead ends
param = 0.9
for i, urn in enumerate(urns):
    urn.center.x = scene.min.x + (i+1.0) / 6.0 * scene.width
    urn.center.y = scene.min.y + param * scene.depth
    urn.min.z = scene.min.z
    urn.facing = Y_MIN

# Place sundial in a prominent location
sundial.center.x = scene.min.x + 0.8 * scene.width
sundial.center.y = scene.min.y + 0.2 * scene.depth
sundial.min.z = scene.min.z
sundial.facing = Y_MAX