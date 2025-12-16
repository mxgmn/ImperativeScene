set_title("Wine Cellar")
set_size(width=8, depth=12, height=2.8)
set_floor_asset("Stone Floor", color="696969")
set_wall_asset("Stone Wall", interior=True, color="8B7355")

entrance = Door("Heavy Wooden Door", width=1.0, depth=0.15, height=2.0, color="8B4513")

# Main storage elements
wine_racks = [Object("Wine Rack", width=2.0, depth=0.4, height=2.0, support=STANDING, color="A0522D") for _ in range(6)]
wine_barrels = [Object("Wine Barrel", width=0.8, depth=1.4, height=1.0, support=STANDING, color="DEB887") for _ in range(8)]

# Tasting area
tasting_table = Object("Rustic Table", width=1.6, depth=0.8, height=0.75, support=STANDING, color="A0522D")
chairs = [Object("Wooden Chair", width=0.45, depth=0.45, height=0.9, support=STANDING, color="8B4513") for _ in range(4)]

# Storage and display
vintage_cabinet = Object("Display Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="CD853F")
wine_crates = [Object("Wooden Crate", width=0.6, depth=0.4, height=0.4, support=STANDING, color="B8860B") for _ in range(3)]

# Functional elements
thermometer = Object("Wall Thermometer", width=0.15, depth=0.05, height=0.4, support=MOUNTED, color="FF4500")
humidity_meter = Object("Humidity Meter", width=0.15, depth=0.05, height=0.2, support=MOUNTED, color="4682B4")

# Decorative elements
wall_sconces = [Object("Wall Sconce", width=0.2, depth=0.25, height=0.3, support=MOUNTED, color="FFA500") for _ in range(4)]
vintage_sign = Object("Vintage Wine Sign", width=1.0, depth=0.05, height=0.6, support=MOUNTED, color="800000")