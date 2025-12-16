set_title("Mancave")
set_size(width=8, depth=6, height=2.8)
set_floor_asset("Wood Planks Floor", color="8B4513")
set_wall_asset("Wood Panel Wall", interior=True, color="6B4423")

door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
window = Window("Small Window", width=1.2, depth=0.1, height=1.0, color="87CEEB")

# Main entertainment setup
tv = Object("Flat Screen TV", width=1.8, depth=0.1, height=1.0, support=MOUNTED, color="2F4F4F")
tv_stand = Object("TV Console", width=2.0, depth=0.5, height=0.6, support=STANDING, color="A0522D")
gaming_console = Object("Gaming Console", width=0.3, depth=0.25, height=0.1, support=STANDING, color="1E90FF")

# Seating
recliner = Object("Leather Recliner", width=1.0, depth=1.2, height=1.1, support=STANDING, color="8B0000")
couch = Object("Large Sofa", width=2.2, depth=1.0, height=0.9, support=STANDING, color="A52A2A")
bean_bag = Object("Bean Bag Chair", width=0.9, depth=0.9, height=0.5, support=STANDING, color="FF4500")

# Entertainment elements
pool_table = Object("Pool Table", width=2.8, depth=1.4, height=0.8, support=STANDING, color="006400")
dart_board = Object("Dart Board", width=0.5, depth=0.05, height=0.5, support=MOUNTED, color="CD853F")

# Storage and decor
mini_fridge = Object("Mini Fridge", width=0.6, depth=0.6, height=0.8, support=STANDING, color="708090")
bar_cabinet = Object("Bar Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
trophy_case = Object("Trophy Case", width=1.0, depth=0.3, height=1.8, support=STANDING, color="B8860B")
posters = [Object("Sports Poster", width=0.8, depth=0.02, height=1.2, support=MOUNTED, color="4169E1") for _ in range(3)]

# Additional furniture
side_table = Object("Side Table", width=0.5, depth=0.5, height=0.6, support=STANDING, color="8B4513")
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.75, support=STANDING, color="B22222") for _ in range(2)]