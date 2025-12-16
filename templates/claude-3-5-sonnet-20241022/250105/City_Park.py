set_title("City Park")
set_size(width=25, depth=25, height=4)
set_floor_asset("Grass Floor", color="4F7942")
set_wall_asset("Iron Fence", interior=False, color="2F4F4F")

entrance_gate = Door("Iron Gate", width=3.0, depth=0.2, height=2.5, color="4A4A4A")

# Main pathway
path = Object("Stone Path", width=3.0, depth=25.0, height=0.1, support=STANDING, color="9B8B7D")
crossing_path = Object("Stone Path", width=15.0, depth=3.0, height=0.1, support=STANDING, color="9B8B7D")

# Seating areas
benches = [Object("Park Bench", width=1.8, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]

# Greenery
trees = [Object("Maple Tree", width=3.0, depth=3.0, height=4.0, support=STANDING, color="228B22") for _ in range(8)]
bushes = [Object("Flowering Bush", width=1.2, depth=1.2, height=1.0, support=STANDING, color="32CD32") for _ in range(12)]

# Central feature
fountain = Object("Fountain", width=4.0, depth=4.0, height=2.0, support=STANDING, color="87CEEB")

# Recreation
playground = Object("Playground Set", width=6.0, depth=6.0, height=3.0, support=STANDING, color="FFA500")
sandbox = Object("Sandbox", width=3.0, depth=3.0, height=0.3, support=STANDING, color="F4A460")

# Amenities
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.8, support=STANDING, color="2E8B57") for _ in range(4)]
bike_rack = Object("Bike Rack", width=2.0, depth=0.3, height=0.8, support=STANDING, color="CD853F")

# Information
info_board = Object("Information Board", width=1.5, depth=0.1, height=1.8, support=STANDING, color="8B4513")