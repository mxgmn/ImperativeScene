set_title("Bedroom")
set_size(width=5, depth=6, height=2.8)
set_floor_asset("Wooden Floor", color="9B7D60")
set_wall_asset("Painted Wall", interior=True, color="C7B9A8")

door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
window = Window("Window", width=1.8, depth=0.1, height=1.5, color="87CEFA")

# Main furniture
bed = Object("Double Bed", width=1.6, depth=2.0, height=0.6, support=STANDING, color="4169E1")
nightstands = [Object("Nightstand", width=0.5, depth=0.4, height=0.6, support=STANDING, color="8B4513") for _ in range(2)]
wardrobe = Object("Wardrobe", width=1.2, depth=0.6, height=2.2, support=STANDING, color="DEB887")
dresser = Object("Dresser", width=1.2, depth=0.5, height=0.8, support=STANDING, color="A0522D")

# Decor and accessories
mirror = Object("Wall Mirror", width=0.8, depth=0.05, height=1.2, support=MOUNTED, color="B8B8B8")
rug = Object("Area Rug", width=2.0, depth=1.6, height=0.02, support=STANDING, color="E6A8D7")
desk = Object("Study Desk", width=1.2, depth=0.6, height=0.75, support=STANDING, color="8B4513")
chair = Object("Desk Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="4682B4")
lamp = Object("Table Lamp", width=0.3, depth=0.3, height=0.4, support=STANDING, color="FFD700")
plants = [Object("Indoor Plant", width=0.3, depth=0.3, height=0.6, support=STANDING, color="228B22") for _ in range(2)]
paintings = [Object("Wall Art", width=0.6, depth=0.05, height=0.8, support=MOUNTED, color="FF6B6B") for _ in range(2)]