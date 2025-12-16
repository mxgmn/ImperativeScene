set_title("Opera House Chamber")
set_size(width=15, depth=20, height=6)
set_floor_asset("Marble Floor", color="E8E0D5")
set_wall_asset("Ornate Wall", interior=True, color="D4C7B8")

main_entrance = Door("Grand Double Door", width=2.4, depth=0.15, height=3.0, color="8B4513")
side_door1 = Door("Wooden Door", width=0.9, depth=0.1, height=2.2, color="8B4513")
side_door2 = Door("Wooden Door", width=0.9, depth=0.1, height=2.2, color="8B4513")
windows = [Window("Arched Window", width=1.2, depth=0.3, height=2.5, color="87CEEB") for _ in range(4)]

# Main performance area
stage = Object("Stage Platform", width=12.0, depth=6.0, height=0.8, support=STANDING, color="8B4513")
curtain = Object("Stage Curtain", width=12.0, depth=0.3, height=5.0, support=STANDING, color="8B0000")
backdrop = Object("Painted Backdrop", width=11.0, depth=0.1, height=4.5, support=STANDING, color="4682B4")

# Seating
seat_rows = [Object("Theater Seats Row", width=10.0, depth=0.8, height=0.9, support=STANDING, color="800020") for _ in range(8)]

# Orchestra pit
orchestra_pit = Object("Orchestra Pit", width=8.0, depth=2.5, height=0.4, support=STANDING, color="4A4A4A")
music_stands = [Object("Music Stand", width=0.4, depth=0.3, height=1.2, support=STANDING, color="CD853F") for _ in range(8)]

# Decorative elements
columns = [Object("Ornate Column", width=0.8, depth=0.8, height=5.5, support=STANDING, color="F5DEB3") for _ in range(6)]
statues = [Object("Classical Statue", width=0.7, depth=0.7, height=2.0, support=STANDING, color="DCDCDC") for _ in range(4)]
wall_sconces = [Object("Wall Sconce", width=0.3, depth=0.2, height=0.4, support=MOUNTED, color="FFD700") for _ in range(8)]

# Props
grand_piano = Object("Grand Piano", width=2.0, depth=1.5, height=1.0, support=STANDING, color="000000")