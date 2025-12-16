set_title("Chess Board")
set_size(width=12, depth=12, height=3)
set_floor_asset("Marble Floor", color="E8E5DE")
set_wall_asset("Wood Panel Wall", interior=True, color="8B4513")

entrance = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="A0522D")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="87CEEB") for _ in range(2)]

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