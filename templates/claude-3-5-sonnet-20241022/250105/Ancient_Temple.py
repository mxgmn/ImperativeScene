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