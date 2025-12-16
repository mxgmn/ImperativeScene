set_title("Cozy Italian Restaurant")
set_size(width=7, depth=4, height=3)
set_floor_asset("Terracotta Tiles Floor", color="A65E42")
set_wall_asset("Venetian Plaster Wall", interior=True, color="D1C6B5")

kitchen_door = Door("Metal Door", width=0.75, depth=0.1, height=2.0, color="B0C4DE")
entrance_door = Door("Wooden Door", width=0.85, depth=0.1, height=2.0, color="8B4513")
window = Window("Window", width=2.4, depth=0.1, height=1.5, color="87CEFA")

tables = [Object("Vintage Table", width=1.3, depth=0.8, height=0.6, support=STANDING, color="A0522D") for _ in range(2)]
chairs = [Object("Durable Chair", 0.45, 0.45, height=0.8, support=STANDING, color="2F4F4F") for _ in range(4 * len(tables))]
counter = Object("Counter", width=3.0, depth=0.4, height=1.1, support=STANDING, color="D2B48C")
stools = [Object("Bar Stool", 0.4, 0.4, height=0.75, support=STANDING, color="8B0000") for _ in range(3)]
register = Object("Cash Register", 0.3, 0.3, height=0.2, support=STANDING, color="696969")
menu = Object("Menu Board", width=0.5, depth=0.05, height=0.85, support=MOUNTED, color="556B2F")
shelf = Object("Wall-mounted Shelf", width=1.6, depth=0.4, height=0.05, support=MOUNTED, color="DEB887")
cheese_wheels = [Object("Cheese Wheel", 0.2 * scale, 0.2 * scale, height=0.15 * scale, support=STANDING, color="FFD700") for i in range(4) for scale in [1.0 + i * 0.3]]
paintings = [Object("Still Life Painting", width=0.6, depth=0.04, height=0.5, support=MOUNTED, color="BC8F8F") for _ in range(3)]
