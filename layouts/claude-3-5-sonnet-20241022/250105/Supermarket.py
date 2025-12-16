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

entrance.center.x = scene.min.x + 0.3 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

back_door.max.x = scene.max.x - 0.2 * scene.width
back_door.max.y = scene.max.y
back_door.min.z = scene.min.z
back_door.facing = Y_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

# Arrange shelves in parallel aisles
shelf_spacing = 0.25
for i, shelf in enumerate(shelves):
    shelf.center.x = scene.min.x + (i+2.0) / 8.0 * scene.width
    shelf.center.y = scene.center.y
    shelf.min.z = scene.min.z
    shelf.facing = X_MAX if i % 2 == 0 else X_MIN

# Refrigerated section along the back wall
for i, fridge in enumerate(fridges):
    fridge.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    fridge.max.y = scene.max.y
    fridge.min.z = scene.min.z
    fridge.facing = Y_MIN

# Produce section near entrance
for i, display in enumerate(produce_displays):
    display.center.x = scene.min.x + (i+2.0) / 5.0 * scene.width
    display.center.y = scene.min.y + 0.2 * scene.depth
    display.min.z = scene.min.z
    display.facing = Y_MAX

# Checkout counters near entrance
checkout_spacing = 0.2
for i, counter in enumerate(checkout_counters):
    counter.center.x = scene.max.x - (i+1.0) / 4.0 * scene.width
    counter.center.y = scene.min.y + 0.15 * scene.depth
    counter.min.z = scene.min.z
    counter.facing = Y_MAX

# Shopping cart area near entrance
cart_spacing = 0.1
for i, cart in enumerate(shopping_carts):
    cart.center.x = entrance.center.x + (i-2.0) * (cart.width + cart_spacing)
    cart.center.y = scene.min.y + 0.1 * scene.depth
    cart.min.z = scene.min.z
    cart.facing = Y_MAX

# Specialty counters
bakery_counter.min.x = scene.min.x
bakery_counter.center.y = scene.min.y + 0.7 * scene.depth
bakery_counter.min.z = scene.min.z
bakery_counter.facing = X_MAX

deli_counter.max.x = scene.max.x
deli_counter.center.y = scene.min.y + 0.7 * scene.depth
deli_counter.min.z = scene.min.z
deli_counter.facing = X_MIN

# Security mirrors in corners
for i, mirror in enumerate(security_mirrors):
    if i == 0:
        mirror.min.x = scene.min.x
        mirror.min.y = scene.min.y
    elif i == 1:
        mirror.max.x = scene.max.x
        mirror.min.y = scene.min.y
    elif i == 2:
        mirror.min.x = scene.min.x
        mirror.max.y = scene.max.y
    else:
        mirror.max.x = scene.max.x
        mirror.max.y = scene.max.y
    mirror.max.z = scene.max.z - 0.2
    mirror.facing = Y_MAX if i < 2 else Y_MIN

bulletin_board.center.x = entrance.center.x
bulletin_board.min.y = scene.min.y
bulletin_board.min.z = 1.5
bulletin_board.facing = Y_MAX