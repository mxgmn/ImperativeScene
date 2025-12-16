set_title("Supermarket")
set_size(width=15, depth=20, height=3.5)
set_floor_asset("Linoleum Floor", color="D3D3D3")
set_wall_asset("Commercial Wall", interior=True, color="E8E8E8")

entrance = Door("Sliding Glass Door", width=2.0, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Metal Door", width=1.0, depth=0.1, height=2.0, color="A9A9A9")
windows = [Window("Store Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(3)]

# Main shelving units (grocery aisles)
shelves = [Object("Grocery Shelf", width=1.0, depth=4.0, height=2.0, support=STANDING, color="696969") for _ in range(6)]

# Refrigerated sections
fridges = [Object("Display Fridge", width=1.0, depth=3.0, height=2.0, support=STANDING, color="B0C4DE") for _ in range(4)]

# Produce section
produce_displays = [Object("Produce Display", width=1.5, depth=1.5, height=0.9, support=STANDING, color="32CD32") for _ in range(3)]

# Checkout area
checkout_counters = [Object("Checkout Counter", width=2.5, depth=0.8, height=1.0, support=STANDING, color="4682B4") for _ in range(3)]

# Shopping cart area
shopping_carts = [Object("Shopping Cart", width=0.6, depth=0.8, height=0.9, support=STANDING, color="B8860B") for _ in range(6)]

# Bakery section
bakery_counter = Object("Bakery Display", width=2.0, depth=0.8, height=1.2, support=STANDING, color="DEB887")

# Deli counter
deli_counter = Object("Deli Counter", width=2.5, depth=0.8, height=1.2, support=STANDING, color="8FBC8F")

# Security
security_mirrors = [Object("Security Mirror", width=0.5, depth=0.5, height=0.5, support=MOUNTED, color="C0C0C0") for _ in range(4)]

# Notice board
bulletin_board = Object("Bulletin Board", width=1.2, depth=0.1, height=0.8, support=MOUNTED, color="CD853F")