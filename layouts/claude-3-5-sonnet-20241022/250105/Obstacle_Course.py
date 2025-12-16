set_title("Obstacle Course")
set_size(width=25, depth=15, height=3)
set_floor_asset("Rubber Floor", color="2F4F4F")
set_wall_asset("Metal Panel Wall", interior=True, color="708090")

entrance = Door("Metal Door", width=1.0, depth=0.1, height=2.0, color="4682B4")
exit_door = Door("Metal Door", width=1.0, depth=0.1, height=2.0, color="4682B4")

# Main obstacles, arranged in sequence
climbing_wall = Object("Climbing Wall", width=3.0, depth=0.3, height=2.5, support=STANDING, color="E67E22")
platforms = [Object("Platform", width=1.0, depth=1.0, height=h, support=STANDING, color="3498DB") for h in [0.3, 0.6, 0.9, 0.6, 0.3]]
balance_beam = Object("Balance Beam", width=0.2, depth=4.0, height=0.5, support=STANDING, color="E74C3C")
hurdles = [Object("Hurdle", width=1.2, depth=0.1, height=0.8, support=STANDING, color="F1C40F") for _ in range(4)]
monkey_bars = Object("Monkey Bars Frame", width=1.5, depth=4.0, height=2.2, support=STANDING, color="9B59B6")
foam_pit = Object("Foam Pit Container", width=2.5, depth=2.5, height=0.8, support=STANDING, color="2ECC71")
ramps = [Object("Ramp", width=1.5, depth=2.0, height=1.0, support=STANDING, color="E67E22") for _ in range(2)]
stepping_posts = [Object("Stepping Post", width=0.4, depth=0.4, height=h, support=STANDING, color="95A5A6") for h in [0.3, 0.4, 0.5, 0.4, 0.3]]
cargo_net = Object("Cargo Net Frame", width=2.0, depth=0.2, height=2.0, support=STANDING, color="27AE60")
finish_platform = Object("Platform", width=2.0, depth=2.0, height=0.3, support=STANDING, color="C0392B")

# Safety equipment
mats = [Object("Safety Mat", width=2.0, depth=1.5, height=0.1, support=STANDING, color="34495E") for _ in range(6)]
railings = [Object("Safety Railing", width=0.1, depth=2.0, height=1.0, support=STANDING, color="BDC3C7") for _ in range(8)]

entrance.min.x = scene.min.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MAX

exit_door.max.x = scene.max.x
exit_door.center.y = scene.max.y - 0.2 * scene.depth
exit_door.min.z = scene.min.z
exit_door.facing = X_MIN

# Create a winding path through the course
path_param = 0.15  # Parameter for spacing from walls

climbing_wall.min.x = scene.min.x + path_param * scene.width
climbing_wall.center.y = scene.min.y + 0.3 * scene.depth
climbing_wall.min.z = scene.min.z
climbing_wall.facing = X_MAX

spacing = 0.1 * scene.width
for i, platform in enumerate(platforms):
    platform.center.x = climbing_wall.max.x + (i + 1.0) * spacing
    platform.center.y = scene.min.y + 0.3 * scene.depth
    platform.min.z = scene.min.z
    platform.facing = Y_MAX

balance_beam.center.x = platforms[-1].max.x + spacing
balance_beam.center.y = scene.min.y + 0.5 * scene.depth
balance_beam.min.z = scene.min.z
balance_beam.facing = Y_MAX

hurdle_spacing = 0.8
for i, hurdle in enumerate(hurdles):
    hurdle.center.x = balance_beam.max.x + spacing
    hurdle.center.y = scene.center.y + (i - 1.5) * hurdle_spacing
    hurdle.min.z = scene.min.z
    hurdle.facing = X_MAX

monkey_bars.center.x = hurdles[0].max.x + 2.0 * spacing
monkey_bars.center.y = scene.center.y
monkey_bars.min.z = scene.min.z
monkey_bars.facing = Y_MAX

foam_pit.center.x = monkey_bars.max.x + 2.0 * spacing
foam_pit.center.y = scene.center.y
foam_pit.min.z = scene.min.z
foam_pit.facing = Y_MAX

ramp_spacing = 2.0 * spacing
for i, ramp in enumerate(ramps):
    ramp.center.x = foam_pit.max.x + (i + 1.0) * ramp_spacing
    ramp.center.y = scene.center.y + (1.0 if i == 0 else -1.0) * spacing
    ramp.min.z = scene.min.z
    ramp.facing = Y_MAX if i == 0 else Y_MIN

post_spacing = 0.8
for i, post in enumerate(stepping_posts):
    post.center.x = ramps[-1].max.x + 2.0 * spacing
    post.center.y = scene.center.y + (i - 2.0) * post_spacing
    post.min.z = scene.min.z
    post.facing = Y_MAX

cargo_net.center.x = stepping_posts[-1].max.x + 2.0 * spacing
cargo_net.center.y = scene.center.y
cargo_net.min.z = scene.min.z
cargo_net.facing = X_MAX

finish_platform.center.x = scene.max.x - path_param * scene.width
finish_platform.center.y = scene.max.y - 0.3 * scene.depth
finish_platform.min.z = scene.min.z
finish_platform.facing = Y_MIN

# Place safety mats under key obstacles
mat_positions = [
    (climbing_wall, 0.0),
    (platforms[2], 0.0),
    (monkey_bars, 0.0),
    (foam_pit, 0.0),
    (ramps[0], 0.0),
    (cargo_net, 0.0)
]

for i, (obstacle, offset) in enumerate(mat_positions):
    mats[i].center.x = obstacle.center.x
    mats[i].center.y = obstacle.center.y + offset
    mats[i].min.z = scene.min.z
    mats[i].facing = obstacle.facing

# Place railings along elevated sections
railing_positions = [
    (platforms[2], 0.5),
    (balance_beam, 0.5),
    (monkey_bars, 1.0),
    (ramps[0], 0.5),
    (ramps[1], 0.5),
    (stepping_posts[2], 0.5),
    (cargo_net, 0.5),
    (finish_platform, 0.5)
]

for i, (obstacle, offset) in enumerate(railing_positions):
    railings[i].center.x = obstacle.center.x
    railings[i].center.y = obstacle.center.y + offset
    railings[i].min.z = scene.min.z
    railings[i].facing = obstacle.facing