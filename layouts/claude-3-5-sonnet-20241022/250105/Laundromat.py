set_title("Laundromat")
set_size(width=8, depth=6, height=3)
set_floor_asset("Linoleum Floor", color="9BA4B0")
set_wall_asset("Painted Wall", interior=True, color="E5E5E5")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.0, color="87CEEB")
windows = [Window("Storefront Window", width=2.0, depth=0.1, height=1.8, color="ADD8E6") for _ in range(2)]

washers = [Object("Washing Machine", width=0.65, depth=0.7, height=0.9, support=STANDING, color="4169E1") for _ in range(6)]
dryers = [Object("Clothes Dryer", width=0.65, depth=0.7, height=0.9, support=STANDING, color="20B2AA") for _ in range(6)]
folding_tables = [Object("Folding Table", width=1.2, depth=0.6, height=0.9, support=STANDING, color="F5DEB3") for _ in range(2)]
benches = [Object("Bench", width=1.2, depth=0.4, height=0.45, support=STANDING, color="CD853F") for _ in range(2)]
vending_machine = Object("Vending Machine", width=0.9, depth=0.8, height=1.8, support=STANDING, color="FF6B6B")
detergent_dispenser = Object("Detergent Dispenser", width=0.5, depth=0.3, height=0.8, support=STANDING, color="FFD700")
trash_bin = Object("Trash Bin", width=0.4, depth=0.4, height=0.6, support=STANDING, color="708090")
change_machine = Object("Change Machine", width=0.4, depth=0.3, height=0.6, support=STANDING, color="C0C0C0")
bulletin_board = Object("Bulletin Board", width=1.0, depth=0.05, height=0.8, support=MOUNTED, color="8B4513")
laundry_cart = Object("Laundry Cart", width=0.6, depth=0.8, height=0.7, support=STANDING, color="FF8C00")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

for i, washer in enumerate(washers):
    washer.min.x = scene.min.x + 0.2 + i * (washer.width + 0.1)
    washer.max.y = scene.max.y
    washer.min.z = scene.min.z
    washer.facing = Y_MIN

for i, dryer in enumerate(dryers):
    dryer.min.x = scene.min.x + 0.2 + i * (dryer.width + 0.1)
    dryer.min.y = scene.min.y + 0.8
    dryer.min.z = scene.min.z
    dryer.facing = Y_MAX

param = 0.3
for i, table in enumerate(folding_tables):
    table.center.x = scene.center.x + (i-0.5) * (table.width + param)
    table.center.y = scene.center.y
    table.min.z = scene.min.z
    table.facing = Y_MAX

for i, bench in enumerate(benches):
    bench.center.x = folding_tables[i].center.x
    bench.min.y = folding_tables[i].max.y + 0.2
    bench.min.z = scene.min.z
    bench.facing = folding_tables[i]

vending_machine.max.x = scene.max.x - 0.1
vending_machine.min.y = scene.min.y + 0.1
vending_machine.min.z = scene.min.z
vending_machine.facing = X_MIN

detergent_dispenser.max.x = scene.max.x - 0.1
detergent_dispenser.center.y = scene.center.y
detergent_dispenser.min.z = scene.min.z
detergent_dispenser.facing = X_MIN

trash_bin.max.x = scene.max.x - 0.1
trash_bin.max.y = scene.max.y - 0.1
trash_bin.min.z = scene.min.z
trash_bin.facing = X_MIN

change_machine.min.x = scene.min.x + 0.1
change_machine.min.y = scene.min.y + 0.1
change_machine.min.z = scene.min.z
change_machine.facing = X_MAX

bulletin_board.min.x = scene.min.x + 0.2
bulletin_board.center.y = scene.min.y + 0.3 * scene.depth
bulletin_board.min.z = 1.2
bulletin_board.facing = X_MAX

laundry_cart.max.x = scene.max.x - 0.2
laundry_cart.center.y = scene.center.y
laundry_cart.min.z = scene.min.z
laundry_cart.facing = X_MIN