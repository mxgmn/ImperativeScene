set_title("Greenhouse")
set_size(width=8, depth=12, height=3.5)
set_floor_asset("Stone Tile Floor", color="8B8682")
set_wall_asset("Glass Wall", interior=True, color="B5D1D7")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="ADD8E6")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.0, color="B0E0E6") for _ in range(6)]

# Main planting areas
planter_boxes = [Object("Planter Box", width=1.8, depth=0.8, height=0.6, support=STANDING, color="8B4513") for _ in range(6)]

# Plants of various sizes
large_plants = [Object("Indoor Plant", width=0.8, depth=0.8, height=2.0, support=STANDING, color="228B22") for _ in range(4)]
medium_plants = [Object("Potted Plant", width=0.5, depth=0.5, height=1.2, support=STANDING, color="32CD32") for _ in range(6)]
small_plants = [Object("Small Plant", width=0.3, depth=0.3, height=0.6, support=STANDING, color="90EE90") for _ in range(12)]

# Furniture and equipment
potting_bench = Object("Potting Bench", width=2.0, depth=0.6, height=0.9, support=STANDING, color="8B7355")
storage_cabinet = Object("Storage Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
watering_station = Object("Sink", width=0.8, depth=0.6, height=0.9, support=STANDING, color="B8B8B8")
tool_rack = Object("Tool Rack", width=1.0, depth=0.1, height=1.2, support=MOUNTED, color="CD853F")
shelf_unit = Object("Wire Shelf Unit", width=1.8, depth=0.4, height=1.8, support=STANDING, color="808080")

# Decorative elements
wind_chime = Object("Wind Chime", width=0.2, depth=0.2, height=0.4, support=MOUNTED, color="E6E6FA")
garden_gnome = Object("Garden Gnome", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FF6347")