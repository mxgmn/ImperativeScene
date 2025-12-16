set_title("Maze")
set_size(width=16.0, depth=16.0, height=3.0)
set_floor_asset("Grass Floor", color="5F7947")
set_wall_asset("Hedge Wall", interior=False, color="4F6640")

wall_endpoints = [
    (6, 6, 6, -4),
    (6, -6, -6, -6),
    (-6, -6, -6, 6),
    (-4, 6, 6, 6),
    (4, 2, 4, -4),
    (4, -4, -2, -4),
    (-4, -4, -4, 4),
    (-4, 4, 4, 4),
    (2, 2, 2, -2),
    (0, -2, -2, -2),
    (-2, -2, -2, 0),
    (-2, 2, 2, 2),
]

hedge_walls = []
for x1, y1, x2, y2 in wall_endpoints:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    hedge_walls.append(Object("Hedge Wall", width=max(dx,dy), depth=0.5, height=2.0, support=STANDING, color="4E7D4E"))