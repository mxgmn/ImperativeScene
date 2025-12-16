set_title("Ancient Temple")
set_size(width=16, depth=20, height=6)
set_floor_asset("Stone Block Floor", color="857C70")
set_wall_asset("Sandstone Wall", interior=True, color="B8A88A")

entrance = Door("Stone Door", width=2.0, depth=0.3, height=3.0, color="8B7355")
windows = [Window("Stone Window", width=1.0, depth=0.3, height=1.5, color="A0522D") for _ in range(6)]

# Columns (two rows of 4 columns each)
columns = [Object("Stone Column", width=1.0, depth=1.0, height=5.0, support=STANDING, color="DEB887") for _ in range(8)]

# Statues
statues = [Object("Guardian Statue", width=1.2, depth=1.2, height=2.5, support=STANDING, color="B8860B") for _ in range(4)]

# Braziers for lighting
braziers = [Object("Brazier", width=0.6, depth=0.6, height=1.2, support=STANDING, color="FF4500") for _ in range(6)]

# Decorative elements
offering_tables = [Object("Stone Table", width=1.0, depth=0.6, height=0.8, support=STANDING, color="8B4513") for _ in range(4)]
urns = [Object("Ancient Urn", width=0.4, depth=0.4, height=0.8, support=STANDING, color="DAA520") for _ in range(6)]

# Wall decorations
hieroglyphs = [Object("Hieroglyph Panel", width=2.0, depth=0.1, height=1.5, support=MOUNTED, color="CD853F") for _ in range(8)]
relief = Object("Wall Relief", width=4.0, depth=0.1, height=2.0, support=MOUNTED, color="D2B48C")

# Ceremonial objects
sarcophagus = Object("Sarcophagus", width=1.0, depth=2.2, height=0.8, support=STANDING, color="FFD700")
throne = Object("Stone Throne", width=1.5, depth=1.2, height=2.0, support=STANDING, color="CD853F")

# Altar
altar = Object("Stone Altar", width=3.0, depth=1.5, height=1.2, support=STANDING, color="CD853F")

entrance.center.x = scene.center.x
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

# Place windows along side walls
for i, window in enumerate(windows):
    if i < 3:
        window.min.x = scene.min.x
        window.center.y = scene.min.y + (i+1.0) * scene.depth / 4.0
        window.facing = X_MAX
    else:
        window.max.x = scene.max.x
        window.center.y = scene.min.y + (i-2.0) * scene.depth / 4.0
        window.facing = X_MIN
    window.min.z = 2.0

# Place columns in two rows
spacing = 0.2
for i, column in enumerate(columns):
    row = i // 4
    col = i % 4
    column.center.x = scene.min.x + (col + 1.0) * scene.width / 5.0
    if row == 0:
        column.center.y = scene.min.y + scene.depth / 3.0
    else:
        column.center.y = scene.min.y + 2.0 * scene.depth / 3.0
    column.min.z = scene.min.z
    column.facing = Y_MAX

# Place statues in corners
corner_offset = 0.15 * scene.width
for i, statue in enumerate(statues):
    if i == 0:
        statue.min.x = scene.min.x + corner_offset
        statue.min.y = scene.min.y + corner_offset
        statue.facing = Y_MAX
    elif i == 1:
        statue.max.x = scene.max.x - corner_offset
        statue.min.y = scene.min.y + corner_offset
        statue.facing = Y_MAX
    elif i == 2:
        statue.min.x = scene.min.x + corner_offset
        statue.max.y = scene.max.y - corner_offset
        statue.facing = Y_MIN
    else:
        statue.max.x = scene.max.x - corner_offset
        statue.max.y = scene.max.y - corner_offset
        statue.facing = Y_MIN
    statue.min.z = scene.min.z

# Place braziers along walls
for i, brazier in enumerate(braziers):
    if i < 3:
        brazier.min.x = scene.min.x + 0.1
        brazier.center.y = scene.min.y + (i+1.0) * scene.depth / 4.0
    else:
        brazier.max.x = scene.max.x - 0.1
        brazier.center.y = scene.min.y + (i-2.0) * scene.depth / 4.0
    brazier.min.z = scene.min.z
    brazier.facing = Y_MAX

# Place offering tables between columns
for i, table in enumerate(offering_tables):
    table.center.x = columns[i*2].center.x
    table.center.y = columns[i*2].center.y - 1.0
    table.min.z = scene.min.z
    table.facing = Y_MAX

# Place urns on offering tables
for i, urn in enumerate(urns):
    table_index = i // 2
    set_coordinate_frame(offering_tables[table_index])
    urn.center.x = offering_tables[table_index].min.x + (0.25 if i % 2 == 0 else 0.75) * offering_tables[table_index].width
    urn.center.y = offering_tables[table_index].center.y
    urn.min.z = offering_tables[table_index].max.z
    urn.facing = offering_tables[table_index].facing
set_coordinate_frame(scene)

# Place hieroglyphs on walls
for i, hieroglyph in enumerate(hieroglyphs):
    if i < 4:
        hieroglyph.min.x = scene.min.x
        hieroglyph.center.y = scene.min.y + (i+1.0) * scene.depth / 5.0
        hieroglyph.facing = X_MAX
    else:
        hieroglyph.max.x = scene.max.x
        hieroglyph.center.y = scene.min.y + (i-3.0) * scene.depth / 5.0
        hieroglyph.facing = X_MIN
    hieroglyph.min.z = 1.5

# Place central relief
relief.center.x = scene.center.x
relief.max.y = scene.max.y
relief.min.z = 2.0
relief.facing = Y_MIN

# Place ceremonial objects
altar.center.x = scene.center.x
altar.max.y = scene.max.y - 0.2 * scene.depth
altar.min.z = scene.min.z
altar.facing = Y_MIN

sarcophagus.center.x = scene.center.x
sarcophagus.center.y = altar.center.y - 1.0
sarcophagus.min.z = scene.min.z
sarcophagus.facing = Y_MAX

throne.center.x = scene.center.x
throne.max.y = scene.max.y - 0.1 * scene.depth
throne.min.z = scene.min.z
throne.facing = Y_MIN