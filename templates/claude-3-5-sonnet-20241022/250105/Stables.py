set_title("Stables")
set_size(width=12, depth=8, height=3.5)
set_floor_asset("Dirt Floor", color="8B7355")
set_wall_asset("Wooden Plank Wall", interior=True, color="8B4513")

main_door = Door("Barn Door", width=2.4, depth=0.15, height=2.8, color="A0522D")
side_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.0, depth=0.1, height=1.0, color="87CEEB") for _ in range(4)]

# Horse stalls (main feature)
stalls = [Object("Horse Stall", width=2.0, depth=3.0, height=1.6, support=STANDING, color="DEB887") for _ in range(4)]

# Feeding and storage
hay_bales = [Object("Hay Bale", width=1.2, depth=0.6, height=0.6, support=STANDING, color="F4A460") for _ in range(6)]
feed_bins = [Object("Feed Bin", width=0.6, depth=0.4, height=0.4, support=STANDING, color="CD853F") for _ in range(4)]
water_troughs = [Object("Water Trough", width=0.8, depth=0.4, height=0.4, support=STANDING, color="4682B4") for _ in range(4)]

# Equipment storage
tack_rack = Object("Tack Rack", width=2.0, depth=0.3, height=1.8, support=MOUNTED, color="8B4513")
tool_rack = Object("Tool Rack", width=1.5, depth=0.2, height=1.0, support=MOUNTED, color="A0522D")
wheelbarrow = Object("Wheelbarrow", width=0.8, depth=1.4, height=0.6, support=STANDING, color="CD5C5C")
storage_chest = Object("Storage Chest", width=1.2, depth=0.6, height=0.8, support=STANDING, color="B8860B")

# Grooming area
grooming_station = Object("Grooming Station", width=2.0, depth=1.0, height=1.0, support=STANDING, color="DAA520")