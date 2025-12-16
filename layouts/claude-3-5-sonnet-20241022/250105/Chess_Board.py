set_title("Chess Board")
set_size(width=12, depth=12, height=3)
set_floor_asset("Marble Floor", color="E8E5DE")
set_wall_asset("Wood Panel Wall", interior=True, color="8B4513")

entrance = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="A0522D")
windows = [Object("Window", width=1.8, depth=0.1, height=1.5, support=MOUNTED, color="87CEEB") for _ in range(2)]

# The main chess board platform
platform = Object("Platform", width=8.0, depth=8.0, height=0.2, support=STANDING, color="DEB887")

# White pieces
white_pawns = [Object("Chess Pawn", width=0.6, depth=0.6, height=0.8, support=STANDING, color="FFFFFF") for _ in range(8)]
white_rooks = [Object("Chess Rook", width=0.7, depth=0.7, height=1.0, support=STANDING, color="FFFFFF") for _ in range(2)]
white_knights = [Object("Chess Knight", width=0.7, depth=0.7, height=1.0, support=STANDING, color="FFFFFF") for _ in range(2)]
white_bishops = [Object("Chess Bishop", width=0.7, depth=0.7, height=1.2, support=STANDING, color="FFFFFF") for _ in range(2)]
white_queen = Object("Chess Queen", width=0.8, depth=0.8, height=1.4, support=STANDING, color="FFFFFF")
white_king = Object("Chess King", width=0.8, depth=0.8, height=1.5, support=STANDING, color="FFFFFF")

# Black pieces
black_pawns = [Object("Chess Pawn", width=0.6, depth=0.6, height=0.8, support=STANDING, color="404040") for _ in range(8)]
black_rooks = [Object("Chess Rook", width=0.7, depth=0.7, height=1.0, support=STANDING, color="404040") for _ in range(2)]
black_knights = [Object("Chess Knight", width=0.7, depth=0.7, height=1.0, support=STANDING, color="404040") for _ in range(2)]
black_bishops = [Object("Chess Bishop", width=0.7, depth=0.7, height=1.2, support=STANDING, color="404040") for _ in range(2)]
black_queen = Object("Chess Queen", width=0.8, depth=0.8, height=1.4, support=STANDING, color="404040")
black_king = Object("Chess King", width=0.8, depth=0.8, height=1.5, support=STANDING, color="404040")

# Furniture around the board
benches = [Object("Wooden Bench", width=2.0, depth=0.5, height=0.5, support=STANDING, color="8B4513") for _ in range(2)]
clock = Object("Chess Clock", width=0.3, depth=0.2, height=0.15, support=STANDING, color="CD853F")
scoreboard = Object("Score Board", width=1.0, depth=0.1, height=0.8, support=MOUNTED, color="A0522D")

entrance.max.x = scene.max.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 1.0
    window.facing = Y_MAX

platform.center.x = scene.center.x
platform.center.y = scene.center.y
platform.min.z = scene.min.z
platform.facing = Y_MAX

square_size = platform.width / 8.0

set_coordinate_frame(platform)
# Place white pieces
for i, pawn in enumerate(white_pawns):
    pawn.center.x = platform.min.x + (i+0.5) * square_size
    pawn.center.y = platform.min.y + 1.5 * square_size
    pawn.min.z = platform.max.z
    pawn.facing = Y_MAX

for i, rook in enumerate(white_rooks):
    rook.center.x = platform.min.x + (0.5 if i == 0 else 7.5) * square_size
    rook.center.y = platform.min.y + 0.5 * square_size
    rook.min.z = platform.max.z
    rook.facing = Y_MAX

for i, knight in enumerate(white_knights):
    knight.center.x = platform.min.x + (1.5 if i == 0 else 6.5) * square_size
    knight.center.y = platform.min.y + 0.5 * square_size
    knight.min.z = platform.max.z
    knight.facing = Y_MAX

for i, bishop in enumerate(white_bishops):
    bishop.center.x = platform.min.x + (2.5 if i == 0 else 5.5) * square_size
    bishop.center.y = platform.min.y + 0.5 * square_size
    bishop.min.z = platform.max.z
    bishop.facing = Y_MAX

white_queen.center.x = platform.min.x + 3.5 * square_size
white_queen.center.y = platform.min.y + 0.5 * square_size
white_queen.min.z = platform.max.z
white_queen.facing = Y_MAX

white_king.center.x = platform.min.x + 4.5 * square_size
white_king.center.y = platform.min.y + 0.5 * square_size
white_king.min.z = platform.max.z
white_king.facing = Y_MAX

# Place black pieces
for i, pawn in enumerate(black_pawns):
    pawn.center.x = platform.min.x + (i+0.5) * square_size
    pawn.center.y = platform.min.y + 6.5 * square_size
    pawn.min.z = platform.max.z
    pawn.facing = Y_MIN

for i, rook in enumerate(black_rooks):
    rook.center.x = platform.min.x + (0.5 if i == 0 else 7.5) * square_size
    rook.center.y = platform.min.y + 7.5 * square_size
    rook.min.z = platform.max.z
    rook.facing = Y_MIN

for i, knight in enumerate(black_knights):
    knight.center.x = platform.min.x + (1.5 if i == 0 else 6.5) * square_size
    knight.center.y = platform.min.y + 7.5 * square_size
    knight.min.z = platform.max.z
    knight.facing = Y_MIN

for i, bishop in enumerate(black_bishops):
    bishop.center.x = platform.min.x + (2.5 if i == 0 else 5.5) * square_size
    bishop.center.y = platform.min.y + 7.5 * square_size
    bishop.min.z = platform.max.z
    bishop.facing = Y_MIN

black_queen.center.x = platform.min.x + 3.5 * square_size
black_queen.center.y = platform.min.y + 7.5 * square_size
black_queen.min.z = platform.max.z
black_queen.facing = Y_MIN

black_king.center.x = platform.min.x + 4.5 * square_size
black_king.center.y = platform.min.y + 7.5 * square_size
black_king.min.z = platform.max.z
black_king.facing = Y_MIN

set_coordinate_frame(scene)

# Place furniture
benches[0].center.x = platform.center.x
benches[0].min.y = platform.min.y - 1.0
benches[0].min.z = scene.min.z
benches[0].facing = Y_MAX

benches[1].center.x = platform.center.x
benches[1].max.y = platform.max.y + 1.0
benches[1].min.z = scene.min.z
benches[1].facing = Y_MIN

clock.center.x = platform.max.x + 1.0
clock.center.y = platform.center.y
clock.min.z = platform.max.z
clock.facing = X_MIN

scoreboard.max.x = scene.max.x
scoreboard.center.y = scene.center.y
scoreboard.min.z = 1.5
scoreboard.facing = X_MIN