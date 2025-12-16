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

main_entrance.center.x = scene.center.x
main_entrance.min.y = scene.min.y
main_entrance.min.z = scene.min.z
main_entrance.facing = Y_MAX

side_door1.min.x = scene.min.x
side_door1.center.y = scene.min.y + 0.25 * scene.depth
side_door1.min.z = scene.min.z
side_door1.facing = X_MAX

side_door2.max.x = scene.max.x
side_door2.center.y = scene.min.y + 0.25 * scene.depth
side_door2.min.z = scene.min.z
side_door2.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 1.5
    window.facing = Y_MAX

stage.center.x = scene.center.x
stage.max.y = scene.max.y
stage.min.z = scene.min.z
stage.facing = Y_MIN

set_coordinate_frame(stage)
curtain.center.x = stage.center.x
curtain.min.y = stage.min.y + 0.1
curtain.min.z = stage.max.z
curtain.facing = stage.facing

backdrop.center.x = stage.center.x
backdrop.min.y = stage.min.y + 0.5
backdrop.min.z = stage.max.z
backdrop.facing = stage.facing

grand_piano.min.x = stage.min.x + 0.2
grand_piano.center.y = stage.center.y
grand_piano.min.z = stage.max.z
grand_piano.facing = Y_MIN
set_coordinate_frame(scene)

orchestra_pit.center.x = stage.center.x
orchestra_pit.max.y = stage.min.y - 0.2
orchestra_pit.min.z = scene.min.z
orchestra_pit.facing = Y_MIN

set_coordinate_frame(orchestra_pit)
for i, stand in enumerate(music_stands):
    stand.center.x = orchestra_pit.min.x + (i+1.0) / 9.0 * orchestra_pit.width
    stand.center.y = orchestra_pit.center.y
    stand.min.z = orchestra_pit.max.z
    stand.facing = Y_MIN
set_coordinate_frame(scene)

spacing = 0.3
for i, row in enumerate(seat_rows):
    row.center.x = scene.center.x
    row.center.y = orchestra_pit.min.y - (i+1.0) * (row.depth + spacing)
    row.min.z = scene.min.z
    row.facing = stage

for i, column in enumerate(columns):
    if i < 3:
        column.min.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    else:
        column.max.x = scene.max.x - ((i-3)+1.0) / 4.0 * scene.width
    column.min.y = scene.min.y + 0.1
    column.min.z = scene.min.z
    column.facing = Y_MAX

for i, statue in enumerate(statues):
    if i < 2:
        statue.min.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    else:
        statue.max.x = scene.max.x - ((i-2)+1.0) / 3.0 * scene.width
    statue.max.y = scene.max.y - 0.2
    statue.min.z = scene.min.z
    statue.facing = Y_MIN

for i, sconce in enumerate(wall_sconces):
    if i < 4:
        sconce.min.x = scene.min.x
        sconce.center.y = scene.min.y + (i+1.0) / 5.0 * scene.depth
    else:
        sconce.max.x = scene.max.x
        sconce.center.y = scene.min.y + ((i-4)+1.0) / 5.0 * scene.depth
    sconce.min.z = 2.0
    sconce.facing = X_MAX if i < 4 else X_MIN