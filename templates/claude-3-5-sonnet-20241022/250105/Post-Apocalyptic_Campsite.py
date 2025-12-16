set_title("Post-Apocalyptic Campsite")
set_size(width=15, depth=15, height=3)
set_floor_asset("Dirt Ground", color="8B7355")
set_wall_asset("Chain Link Fence", interior=False, color="708090")

# Main shelter and living area
tent = Object("Military Tent", width=3.0, depth=4.0, height=2.2, support=STANDING, color="4B5320")
sleeping_bags = [Object("Sleeping Bag", width=0.7, depth=1.8, height=0.2, support=STANDING, color="556B2F") for _ in range(3)]

# Fire pit and seating
fire_pit = Object("Fire Pit", width=1.0, depth=1.0, height=0.3, support=STANDING, color="FF4500")
logs = [Object("Log Bench", width=1.5, depth=0.4, height=0.45, support=STANDING, color="8B4513") for _ in range(3)]

# Survival equipment
water_tanks = [Object("Water Tank", width=0.8, depth=0.8, height=1.2, support=STANDING, color="4682B4") for _ in range(2)]
generator = Object("Generator", width=0.7, depth=0.9, height=0.6, support=STANDING, color="CD853F")
fuel_barrels = [Object("Fuel Barrel", width=0.6, depth=0.6, height=0.9, support=STANDING, color="B22222") for _ in range(2)]

# Transportation
motorcycle = Object("Motorcycle", width=0.8, depth=2.0, height=1.2, support=STANDING, color="2F4F4F")
bicycle = Object("Bicycle", width=0.4, depth=1.8, height=1.0, support=STANDING, color="8B8878")

# Storage and supplies
storage_crates = [Object("Metal Crate", width=1.0, depth=0.8, height=0.6, support=STANDING, color="A0522D") for _ in range(4)]
weapon_locker = Object("Gun Locker", width=1.2, depth=0.5, height=1.8, support=STANDING, color="696969")

# Defensive measures
sandbags = [Object("Sandbag Wall", width=1.5, depth=0.5, height=0.8, support=STANDING, color="BDB76B") for _ in range(3)]
watchtower = Object("Watchtower", width=2.0, depth=2.0, height=3.0, support=STANDING, color="8B7355")

# Survival essentials
rain_collector = Object("Rain Collector", width=1.2, depth=1.2, height=0.8, support=STANDING, color="87CEEB")
garden_box = Object("Garden Box", width=2.0, depth=1.0, height=0.4, support=STANDING, color="6B8E23")