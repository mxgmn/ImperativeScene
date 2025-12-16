set_title("Gun Shop")
set_size(width=8, depth=10, height=3)
set_floor_asset("Hardwood Floor", color="8B7355")
set_wall_asset("Painted Wall", interior=True, color="E8E5DC")

entrance = Door("Security Door", width=1.0, depth=0.1, height=2.2, color="4A4A4A")
back_door = Door("Metal Door", width=0.8, depth=0.1, height=2.0, color="708090")
windows = [Window("Security Window", width=1.5, depth=0.1, height=1.5, color="87CEEB") for _ in range(2)]

display_cases = [Object("Glass Display Case", width=1.8, depth=0.6, height=1.0, support=STANDING, color="B0C4DE") for _ in range(3)]
counter = Object("Counter", width=2.5, depth=0.6, height=1.1, support=STANDING, color="8B4513")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.3, support=STANDING, color="696969")

wall_racks = [Object("Gun Rack", width=2.0, depth=0.2, height=1.5, support=MOUNTED, color="A0522D") for _ in range(4)]
ammo_shelves = [Object("Storage Shelf", width=1.2, depth=0.4, height=2.0, support=STANDING, color="8B7355") for _ in range(2)]
gun_safe = Object("Gun Safe", width=1.2, depth=0.6, height=2.0, support=STANDING, color="2F4F4F")

security_camera = Object("Security Camera", width=0.2, depth=0.2, height=0.2, support=MOUNTED, color="4682B4")
target_posters = [Object("Target Poster", width=0.6, depth=0.02, height=0.8, support=MOUNTED, color="CD5C5C") for _ in range(3)]
warning_sign = Object("Warning Sign", width=0.4, depth=0.02, height=0.3, support=MOUNTED, color="FF4500")

chairs = [Object("Office Chair", width=0.5, depth=0.5, height=1.0, support=STANDING, color="000080") for _ in range(2)]
filing_cabinet = Object("Filing Cabinet", width=0.5, depth=0.6, height=1.3, support=STANDING, color="778899")