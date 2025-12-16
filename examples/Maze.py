set_title("Mysterious Hedge Maze")
set_size(width=30, depth=30, height=3)
set_floor_asset("Grass")
set_wall_asset("Sky")

# Define hedge walls
def create_hedge(x1, y1, x2, y2):
    hedge = Object("Hedge Wall", width=abs(x2-x1), depth=abs(y2-y1), height=2.5)
    hedge.supporting_surface = GROUND
    hedge.min.x = min(x1, x2)
    hedge.min.y = min(y1, y2)
    hedge.facing = center(scene)
    return hedge

# Create maze layout
hedges = [
    # Outer walls
    create_hedge(-15, -15, 15, -15),
    create_hedge(-15, -15, -15, 15),
    create_hedge(15, -15, 15, 15),
    create_hedge(-15, 15, 15, 15),
    
    # Inner walls
    create_hedge(-10, -15, -10, 10),
    create_hedge(-5, -10, -5, 15),
    create_hedge(0, -15, 0, 10),
    create_hedge(5, -10, 5, 15),
    create_hedge(10, -15, 10, 10),
    
    create_hedge(-15, -10, -5, -10),
    create_hedge(-10, -5, 0, -5),
    create_hedge(-15, 0, -5, 0),
    create_hedge(-10, 5, 0, 5),
    create_hedge(-15, 10, -5, 10),
    
    create_hedge(0, -10, 10, -10),
    create_hedge(5, -5, 15, -5),
    create_hedge(0, 0, 10, 0),
    create_hedge(5, 5, 15, 5),
    create_hedge(0, 10, 10, 10),
]

# Entrance
entrance = Object("Stone Archway", width=2, depth=1, height=3)
entrance.supporting_surface = GROUND
entrance.center.x = 0
entrance.min.y = -15
entrance.facing = center(scene)

# Exit
exit = Object("Stone Archway", width=2, depth=1, height=3)
exit.supporting_surface = GROUND
exit.center.x = 0
exit.max.y = 15
exit.facing = center(scene)

# Fountain at the center
fountain = Object("Stone Fountain", width=3, depth=3, height=2)
fountain.supporting_surface = GROUND
fountain.center.x = 0
fountain.center.y = 0
fountain.facing = center(scene)

# Statues at dead ends
statue1 = Object("Greek Statue", width=1, depth=1, height=2)
statue1.supporting_surface = GROUND
statue1.center.x = -12.5
statue1.center.y = -12.5
statue1.facing = center(scene)

statue2 = Object("Greek Statue", width=1, depth=1, height=2)
statue2.supporting_surface = GROUND
statue2.center.x = 12.5
statue2.center.y = 12.5
statue2.facing = center(scene)

# Benches
bench1 = Object("Stone Bench", width=1.5, depth=0.5, height=0.5)
bench1.supporting_surface = GROUND
bench1.center.x = -7.5
bench1.center.y = 7.5
bench1.facing = center(scene)

bench2 = Object("Stone Bench", width=1.5, depth=0.5, height=0.5)
bench2.supporting_surface = GROUND
bench2.center.x = 7.5
bench2.center.y = -7.5
bench2.facing = center(scene)

# Decorative elements
sundial = Object("Sundial", width=0.5, depth=0.5, height=1)
sundial.supporting_surface = GROUND
sundial.center.x = 2.5
sundial.center.y = 2.5
sundial.facing = center(scene)

birdbath = Object("Bird Bath", width=0.8, depth=0.8, height=1)
birdbath.supporting_surface = GROUND
birdbath.center.x = -2.5
birdbath.center.y = -2.5
birdbath.facing = center(scene)

# Lanterns for lighting
def create_lantern(x, y):
    lantern = Object("Garden Lantern", width=0.3, depth=0.3, height=1.2)
    lantern.supporting_surface = GROUND
    lantern.center.x = x
    lantern.center.y = y
    lantern.facing = center(scene)
    return lantern

lanterns = [
    create_lantern(-12.5, 2.5),
    create_lantern(12.5, -2.5),
    create_lantern(-2.5, 12.5),
    create_lantern(2.5, -12.5),
]