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

# Position main shelter
tent.center.x = scene.min.x + 0.3 * scene.width
tent.center.y = scene.min.y + 0.3 * scene.depth
tent.min.z = scene.min.z
tent.facing = Y_MAX

# Position sleeping bags inside tent
set_coordinate_frame(tent)
for i, bag in enumerate(sleeping_bags):
    bag.center.x = tent.min.x + (i+1.0) / 4.0 * tent.width
    bag.center.y = tent.center.y
    bag.min.z = tent.min.z
    bag.facing = tent.facing
set_coordinate_frame(scene)

# Setup fire pit and seating area
fire_pit.center.x = tent.center.x + 4.0
fire_pit.center.y = tent.center.y
fire_pit.min.z = scene.min.z

# Position logs around fire pit
for i, log in enumerate(logs):
    angle = i * 2.0 * 3.14159 / 3.0
    radius = 1.5
    log.center.x = fire_pit.center.x + radius * math.cos(angle)
    log.center.y = fire_pit.center.y + radius * math.sin(angle)
    log.min.z = scene.min.z
    log.facing = fire_pit

# Position water storage and power
water_tanks[0].max.x = tent.max.x + 0.5
water_tanks[0].min.y = tent.min.y
water_tanks[0].min.z = scene.min.z
water_tanks[0].facing = X_MIN

water_tanks[1].max.x = water_tanks[0].max.x
water_tanks[1].min.y = water_tanks[0].max.y + 0.2
water_tanks[1].min.z = scene.min.z
water_tanks[1].facing = X_MIN

generator.min.x = water_tanks[0].max.x + 0.5
generator.center.y = water_tanks[0].center.y
generator.min.z = scene.min.z
generator.facing = X_MAX

# Position fuel storage
for i, barrel in enumerate(fuel_barrels):
    barrel.center.x = generator.center.x
    barrel.min.y = generator.max.y + 0.2 + i * (barrel.depth + 0.2)
    barrel.min.z = scene.min.z
    barrel.facing = generator.facing

# Position vehicles
motorcycle.max.x = scene.max.x - 0.2 * scene.width
motorcycle.max.y = scene.max.y - 0.2 * scene.depth
motorcycle.min.z = scene.min.z
motorcycle.facing = Y_MIN

bicycle.min.x = motorcycle.min.x - 1.0
bicycle.center.y = motorcycle.center.y
bicycle.min.z = scene.min.z
bicycle.facing = motorcycle.facing

# Position storage area
for i, crate in enumerate(storage_crates):
    crate.min.x = scene.min.x + 0.1 * scene.width
    crate.min.y = scene.max.y - (i+1.0) * (crate.depth + 0.2)
    crate.min.z = scene.min.z
    crate.facing = Y_MIN

weapon_locker.min.x = crate.max.x + 0.5
weapon_locker.center.y = scene.max.y - 0.2 * scene.depth
weapon_locker.min.z = scene.min.z
weapon_locker.facing = X_MAX

# Position defensive structures
watchtower.max.x = scene.max.x - 0.1 * scene.width
watchtower.min.y = scene.min.y + 0.1 * scene.depth
watchtower.min.z = scene.min.z
watchtower.facing = Y_MAX

for i, sandbag in enumerate(sandbags):
    if i == 0:
        sandbag.min.x = tent.min.x - 1.0
        sandbag.center.y = tent.center.y
        sandbag.facing = X_MAX
    elif i == 1:
        sandbag.center.x = tent.center.x
        sandbag.min.y = tent.min.y - 1.0
        sandbag.facing = Y_MAX
    else:
        sandbag.max.x = tent.max.x + 1.0
        sandbag.center.y = tent.center.y
        sandbag.facing = X_MIN

# Position survival infrastructure
rain_collector.min.x = scene.min.x + 0.1 * scene.width
rain_collector.min.y = scene.min.y + 0.1 * scene.depth
rain_collector.min.z = scene.min.z
rain_collector.facing = X_MAX

garden_box.min.x = rain_collector.max.x + 0.5
garden_box.min.y = rain_collector.min.y
garden_box.min.z = scene.min.z
garden_box.facing = Y_MAX