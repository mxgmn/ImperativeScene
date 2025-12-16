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