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