set_title("Spacious Family Kitchen")
set_size(width=10, depth=8, height=3)
set_floor_asset("Tile Floor", color="B5B5B5")
set_wall_asset("Painted Wall", interior=True, color="E6E6FA")

# Doors and windows
main_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.1, color="8B4513")
patio_door = Door("Glass Door", width=1.8, depth=0.1, height=2.1, color="87CEEB")
windows = [Window("Window", width=1.2, depth=0.1, height=1.2, color="ADD8E6") for _ in range(3)]

# Seating
dining_table = Object("Large Dining Table", width=4.8, depth=1.5, height=0.75, support=STANDING, color="CD853F")
chairs = [Object("Dining Chair", width=0.45, depth=0.45, height=0.95, support=STANDING, color="B8860B") for _ in range(12)]
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.65, support=STANDING, color="B8860B") for _ in range(4)]

# Major appliances and fixtures
refrigerator = Object("Double Door Refrigerator", width=1.2, depth=0.8, height=2.0, support=STANDING, color="E0E0E0")
stove = Object("Industrial Stove", width=1.2, depth=0.7, height=0.9, support=STANDING, color="484848")
dishwasher = Object("Dishwasher", width=0.6, depth=0.6, height=0.85, support=STANDING, color="C0C0C0")
sink = Object("Double Sink", width=0.9, depth=0.6, height=0.9, support=STANDING, color="CFD7D9")

# Storage and counters
island = Object("Kitchen Island", width=2.4, depth=1.2, height=0.9, support=STANDING, color="8B4513")
cabinets = [Object("Cabinet", width=0.6, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]
wall_cabinets = [Object("Wall Cabinet", width=0.6, depth=0.3, height=0.7, support=MOUNTED, color="8B4513") for _ in range(4)]
pantry = Object("Pantry Cabinet", width=1.2, depth=0.6, height=2.0, support=STANDING, color="8B4513")

# Appliances
microwave = Object("Microwave", width=0.6, depth=0.4, height=0.4, support=STANDING, color="696969")
coffee_maker = Object("Coffee Maker", width=0.3, depth=0.25, height=0.35, support=STANDING, color="8B0000")
toaster = Object("Toaster", width=0.3, depth=0.2, height=0.2, support=STANDING, color="CD853F")

# Storage and organization
spice_rack = Object("Spice Rack", width=0.6, depth=0.1, height=0.4, support=MOUNTED, color="DEB887")
pot_rack = Object("Pot Rack", width=1.2, depth=0.3, height=0.02, support=MOUNTED, color="B8860B")