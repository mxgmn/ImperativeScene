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