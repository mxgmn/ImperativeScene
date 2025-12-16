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