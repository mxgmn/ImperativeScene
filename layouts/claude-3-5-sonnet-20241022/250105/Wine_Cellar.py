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

entrance.max.x = scene.max.x
entrance.max.y = scene.max.y - 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

# Place wine racks along the walls
rack_spacing = 0.4
for i in range(3):
    # Left wall racks
    wine_racks[i].min.x = scene.min.x
    wine_racks[i].center.y = scene.min.y + (i+1.0) * scene.depth / 4.0
    wine_racks[i].min.z = scene.min.z
    wine_racks[i].facing = X_MAX
    
    # Right wall racks
    wine_racks[i+3].max.x = scene.max.x
    wine_racks[i+3].center.y = scene.min.y + (i+1.0) * scene.depth / 4.0
    wine_racks[i+3].min.z = scene.min.z
    wine_racks[i+3].facing = X_MIN

# Place wine barrels in two rows
barrel_spacing = 0.3
for i in range(8):
    row = i // 4
    col = i % 4
    wine_barrels[i].center.x = scene.center.x + (col-1.5) * (wine_barrels[i].width + barrel_spacing)
    wine_barrels[i].max.y = scene.max.y - row * (wine_barrels[i].depth + barrel_spacing)
    wine_barrels[i].min.z = scene.min.z
    wine_barrels[i].facing = Y_MIN

# Tasting area in the center
tasting_table.center.x = scene.center.x
tasting_table.center.y = scene.min.y + 0.3 * scene.depth
tasting_table.min.z = scene.min.z
tasting_table.facing = Y_MAX

# Place chairs around the tasting table
set_coordinate_frame(tasting_table)
for i, chair in enumerate(chairs):
    if i < 2:
        chair.center.x = tasting_table.min.x + (i+0.5) * tasting_table.width/2.0
        chair.max.y = tasting_table.min.y - 0.1
    else:
        chair.center.x = tasting_table.min.x + (i-1.5) * tasting_table.width/2.0
        chair.min.y = tasting_table.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = tasting_table
set_coordinate_frame(scene)

# Display cabinet and crates
vintage_cabinet.min.x = scene.min.x
vintage_cabinet.min.y = scene.min.y + 0.1
vintage_cabinet.min.z = scene.min.z
vintage_cabinet.facing = X_MAX

for i, crate in enumerate(wine_crates):
    crate.min.x = vintage_cabinet.max.x + 0.2
    crate.min.y = scene.min.y + 0.1
    crate.min.z = i * crate.height
    crate.facing = X_MAX

# Monitoring equipment
thermometer.max.x = scene.max.x
thermometer.center.y = scene.center.y - 1.0
thermometer.min.z = 1.2
thermometer.facing = X_MIN

humidity_meter.max.x = scene.max.x
humidity_meter.center.y = scene.center.y + 1.0
humidity_meter.min.z = 1.2
humidity_meter.facing = X_MIN

# Wall sconces for lighting
sconce_height = 1.5
for i, sconce in enumerate(wall_sconces):
    if i < 2:
        sconce.min.x = scene.min.x
        sconce.center.y = scene.min.y + (i+1.0) * scene.depth / 3.0
    else:
        sconce.max.x = scene.max.x
        sconce.center.y = scene.min.y + (i-1.0) * scene.depth / 3.0
    sconce.min.z = sconce_height
    sconce.facing = X_MAX if i < 2 else X_MIN

# Vintage sign
vintage_sign.center.x = scene.center.x
vintage_sign.min.y = scene.min.y
vintage_sign.min.z = 1.8
vintage_sign.facing = Y_MAX