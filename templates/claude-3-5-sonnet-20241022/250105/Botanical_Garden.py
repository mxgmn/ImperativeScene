set_title("Botanical Garden")
set_size(width=15, depth=15, height=4)
set_floor_asset("Stone Path", color="9B8E83")
set_wall_asset("Glass Wall", interior=True, color="A3C1D1")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.5, color="87CEEB") for _ in range(6)]

# Main features
large_planters = [Object("Large Planter", width=2.0, depth=2.0, height=0.6, support=STANDING, color="8B4513") for _ in range(4)]
medium_planters = [Object("Medium Planter", width=1.2, depth=1.2, height=0.5, support=STANDING, color="A0522D") for _ in range(6)]
small_planters = [Object("Small Planter", width=0.8, depth=0.8, height=0.4, support=STANDING, color="8B4513") for _ in range(8)]

# Plants (using the planters as bases)
palm_trees = [Object("Palm Tree", width=1.8, depth=1.8, height=3.5, support=STANDING, color="228B22") for _ in range(2)]
ferns = [Object("Large Fern", width=1.0, depth=1.0, height=1.2, support=STANDING, color="32CD32") for _ in range(4)]
bamboo = [Object("Bamboo Plant", width=0.6, depth=0.6, height=2.5, support=STANDING, color="90EE90") for _ in range(6)]
orchids = [Object("Orchid Plant", width=0.4, depth=0.4, height=0.6, support=STANDING, color="FF69B4") for _ in range(8)]

# Furniture and decorative elements
benches = [Object("Garden Bench", width=1.5, depth=0.6, height=0.9, support=STANDING, color="8B7355") for _ in range(4)]
fountain = Object("Stone Fountain", width=2.0, depth=2.0, height=1.5, support=STANDING, color="B8860B")
information_boards = [Object("Information Board", width=0.8, depth=0.1, height=1.2, support=MOUNTED, color="DEB887") for _ in range(3)]
stone_path = [Object("Decorative Stone", width=0.4, depth=0.4, height=0.05, support=STANDING, color="808080") for _ in range(12)]

# Maintenance area
tool_cabinet = Object("Tool Cabinet", width=1.2, depth=0.6, height=1.8, support=STANDING, color="556B2F")
watering_station = Object("Watering Station", width=0.8, depth=0.6, height=1.0, support=STANDING, color="4682B4")