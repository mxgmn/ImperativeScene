set_title("Restaurant")
set_size(width=12, depth=8, height=3)
set_floor_asset("Hardwood Floor", color="8B7355")
set_wall_asset("Painted Wall", interior=True, color="E8DCC4")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
kitchen_door = Door("Swing Door", width=0.9, depth=0.1, height=2.0, color="B8B8B8")
windows = [Window("Window", width=1.5, depth=0.1, height=1.5, color="ADD8E6") for _ in range(3)]

# Main dining area furniture
tables_4 = [Object("Dining Table", width=1.0, depth=1.0, height=0.75, support=STANDING, color="8B4513") for _ in range(4)]
tables_2 = [Object("Small Table", width=0.8, depth=0.8, height=0.75, support=STANDING, color="8B4513") for _ in range(3)]
chairs = [Object("Dining Chair", width=0.45, depth=0.45, height=0.9, support=STANDING, color="CD853F") for _ in range(22)]

# Service area
host_station = Object("Host Station", width=1.2, depth=0.6, height=1.1, support=STANDING, color="DEB887")
service_counter = Object("Service Counter", width=2.5, depth=0.6, height=1.1, support=STANDING, color="8B7355")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.3, support=STANDING, color="4A4A4A")

# Decor
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(3)]
wall_art = [Object("Framed Art", width=0.8, depth=0.05, height=0.6, support=MOUNTED, color="B8860B") for _ in range(4)]
menu_board = Object("Menu Board", width=1.0, depth=0.05, height=0.8, support=MOUNTED, color="8B4513")

# Storage and service items
storage_cabinet = Object("Storage Cabinet", width=1.8, depth=0.4, height=1.8, support=STANDING, color="A0522D")
water_station = Object("Water Station", width=0.8, depth=0.4, height=1.2, support=STANDING, color="4682B4")