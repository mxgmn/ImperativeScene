set_title("Casino Floor Section")
set_size(width=15, depth=12, height=3)
set_floor_asset("Patterned Carpet", color="371F54")
set_wall_asset("Decorative Wall", interior=True, color="2B1B3B")

entrance = Door("Glass Double Door", width=2.0, depth=0.1, height=2.2, color="4682B4")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="8B0000")

# Main gambling tables and slots
slot_machines = [Object("Slot Machine", width=0.8, depth=0.6, height=1.8, support=STANDING, color="FFD700") for _ in range(8)]
blackjack_tables = [Object("Card Table", width=1.5, depth=0.8, height=0.9, support=STANDING, color="006400") for _ in range(3)]
roulette_table = Object("Roulette Table", width=2.2, depth=1.2, height=0.9, support=STANDING, color="8B0000")
poker_table = Object("Poker Table", width=2.0, depth=1.0, height=0.9, support=STANDING, color="000080")

# Bar area
bar_counter = Object("Bar Counter", width=3.5, depth=0.6, height=1.1, support=STANDING, color="B8860B")
drink_shelf = Object("Glass Shelf", width=3.0, depth=0.3, height=0.05, support=MOUNTED, color="4682B4")

# Seating
gaming_chairs = [Object("Gaming Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="4B0082") for _ in range(12)]
bar_stools = [Object("Bar Stool", width=0.4, depth=0.4, height=0.8, support=STANDING, color="8B008B") for _ in range(6)]

# Decorative elements
columns = [Object("Decorative Column", width=0.6, depth=0.6, height=3.0, support=STANDING, color="DEB887") for _ in range(4)]
plants = [Object("Indoor Palm", width=0.8, depth=0.8, height=2.0, support=STANDING, color="228B22") for _ in range(3)]
wall_lights = [Object("Wall Sconce", width=0.2, depth=0.2, height=0.4, support=MOUNTED, color="FFA500") for _ in range(6)]

# Security
security_desk = Object("Security Desk", width=1.8, depth=0.8, height=1.1, support=STANDING, color="A0522D")
camera_posts = [Object("Security Camera", width=0.2, depth=0.3, height=0.2, support=MOUNTED, color="696969") for _ in range(4)]

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

# Arrange slot machines in two rows
for i, slot in enumerate(slot_machines):
    if i < 4:
        slot.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
        slot.min.y = scene.min.y + 0.2 * scene.depth
    else:
        slot.center.x = scene.min.x + (i-3.0) / 5.0 * scene.width
        slot.min.y = scene.min.y + 0.4 * scene.depth
    slot.min.z = scene.min.z
    slot.facing = Y_MAX

# Gaming tables arrangement
spacing = 0.3
for i, table in enumerate(blackjack_tables):
    table.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    table.center.y = scene.center.y
    table.min.z = scene.min.z
    table.facing = Y_MIN

roulette_table.center.x = scene.min.x + 0.7 * scene.width
roulette_table.center.y = scene.min.y + 0.7 * scene.depth
roulette_table.min.z = scene.min.z
roulette_table.facing = Y_MIN

poker_table.center.x = scene.min.x + 0.3 * scene.width
poker_table.center.y = scene.min.y + 0.7 * scene.depth
poker_table.min.z = scene.min.z
poker_table.facing = Y_MIN

# Bar area
bar_counter.max.x = scene.max.x - 0.1
bar_counter.max.y = scene.max.y
bar_counter.min.z = scene.min.z
bar_counter.facing = Y_MIN

drink_shelf.center.x = bar_counter.center.x
drink_shelf.max.y = scene.max.y
drink_shelf.min.z = 1.5
drink_shelf.facing = Y_MIN

# Arrange chairs around tables
chair_offset = 0.2
for i, chair in enumerate(gaming_chairs):
    if i < 6:  # Blackjack table chairs
        table_index = i // 2
        table = blackjack_tables[table_index]
        set_coordinate_frame(table)
        chair.center.x = table.center.x + (0.4 if i % 2 == 0 else -0.4)
        chair.min.y = table.max.y + chair_offset
        chair.min.z = scene.min.z
        chair.facing = table
    else:  # Poker table chairs
        set_coordinate_frame(poker_table)
        angle = (i-6) * (360.0/6.0)
        chair.center.x = poker_table.center.x + 0.8 * math.cos(math.radians(angle))
        chair.center.y = poker_table.center.y + 0.8 * math.sin(math.radians(angle))
        chair.min.z = scene.min.z
        chair.facing = poker_table
set_coordinate_frame(scene)

# Bar stools
set_coordinate_frame(bar_counter)
for i, stool in enumerate(bar_stools):
    stool.center.x = bar_counter.min.x + (i+1.0) / 7.0 * bar_counter.width
    stool.min.y = bar_counter.max.y + chair_offset
    stool.min.z = scene.min.z
    stool.facing = bar_counter
set_coordinate_frame(scene)

# Decorative elements
for i, column in enumerate(columns):
    if i < 2:
        column.min.x = scene.min.x
        column.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    else:
        column.max.x = scene.max.x
        column.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
    column.min.z = scene.min.z
    column.facing = Y_MAX

for i, plant in enumerate(plants):
    plant.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    plant.max.y = scene.max.y - 0.1
    plant.min.z = scene.min.z
    plant.facing = Y_MIN

for i, light in enumerate(wall_lights):
    if i < 3:
        light.min.x = scene.min.x
        light.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    else:
        light.max.x = scene.max.x
        light.center.y = scene.min.y + (i-2.0) / 4.0 * scene.depth
    light.min.z = 2.0
    light.facing = X_MAX if i < 3 else X_MIN

# Security
security_desk.min.x = scene.min.x + 0.1
security_desk.min.y = scene.min.y + 0.1
security_desk.min.z = scene.min.z
security_desk.facing = X_MAX

for i, camera in enumerate(camera_posts):
    if i < 2:
        camera.min.x = scene.min.x
        camera.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    else:
        camera.max.x = scene.max.x
        camera.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
    camera.min.z = 2.5
    camera.facing = X_MAX if i < 2 else X_MIN