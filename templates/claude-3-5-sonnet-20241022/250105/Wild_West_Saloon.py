set_title("Wild West Saloon")
set_size(width=12, depth=8, height=3)
set_floor_asset("Wooden Planks Floor", color="8B4513")
set_wall_asset("Wooden Wall", interior=True, color="A0522D")

entrance = Door("Saloon Double Door", width=1.6, depth=0.1, height=2.0, color="CD853F")
back_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.2, depth=0.1, height=1.2, color="F4A460") for _ in range(3)]

# Main bar setup
bar_counter = Object("Bar Counter", width=5.0, depth=0.6, height=1.1, support=STANDING, color="DEB887")
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.8, support=STANDING, color="B8860B") for _ in range(6)]
bar_shelf = Object("Bar Back Shelf", width=4.8, depth=0.3, height=2.0, support=STANDING, color="8B4513")
barrels = [Object("Wooden Barrel", width=0.5, depth=0.5, height=0.8, support=STANDING, color="DAA520") for _ in range(4)]

# Seating areas
tables = [Object("Round Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="CD853F") for _ in range(4)]
chairs = [Object("Wooden Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="D2691E") for _ in range(16)]

# Gaming area
poker_table = Object("Poker Table", width=1.2, depth=1.2, height=0.75, support=STANDING, color="006400")
poker_chairs = [Object("Wooden Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]

# Decorative elements
piano = Object("Upright Piano", width=1.4, depth=0.6, height=1.3, support=STANDING, color="800000")
wanted_posters = [Object("Wanted Poster", width=0.3, depth=0.02, height=0.4, support=MOUNTED, color="F5DEB3") for _ in range(3)]
deer_head = Object("Mounted Deer Head", width=0.8, depth=0.4, height=0.9, support=MOUNTED, color="B8860B")