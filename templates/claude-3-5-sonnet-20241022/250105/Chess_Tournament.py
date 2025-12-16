set_title("Chess Tournament Hall")
set_size(width=10, depth=12, height=3)
set_floor_asset("Marble Floor", color="E8E5DE")
set_wall_asset("Painted Wall", interior=True, color="D6D1C4")

entrance = Door("Double Door", width=1.8, depth=0.1, height=2.2, color="8B4513")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Window", width=1.5, depth=0.1, height=1.5, color="87CEEB") for _ in range(4)]

# Chess tables are wider than deep to accommodate the chess board and clock
chess_tables = [Object("Chess Table", width=0.9, depth=0.7, height=0.75, support=STANDING, color="8B4513") for _ in range(12)]
chairs = [Object("Tournament Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="A0522D") for _ in range(24)]

# Judges' area
judges_table = Object("Long Table", width=2.0, depth=0.8, height=0.75, support=STANDING, color="4B0082")
judges_chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="483D8B") for _ in range(3)]

# Display and equipment
scoreboard = Object("Digital Board", width=2.0, depth=0.1, height=1.2, support=MOUNTED, color="4682B4")
trophy_case = Object("Display Cabinet", width=1.2, depth=0.4, height=1.8, support=STANDING, color="DEB887")
clock_display = Object("Tournament Clock Display", width=1.5, depth=0.1, height=0.6, support=MOUNTED, color="FF4500")

# Spectator area
benches = [Object("Wooden Bench", width=2.0, depth=0.4, height=0.45, support=STANDING, color="CD853F") for _ in range(4)]
water_dispenser = Object("Water Dispenser", width=0.4, depth=0.4, height=1.2, support=STANDING, color="87CEEB")
trash_bin = Object("Trash Bin", width=0.3, depth=0.3, height=0.5, support=STANDING, color="708090")