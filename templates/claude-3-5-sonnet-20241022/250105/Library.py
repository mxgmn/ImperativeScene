set_title("Library")
set_size(width=15, depth=12, height=3.5)
set_floor_asset("Hardwood Floor", color="8B4513")
set_wall_asset("Painted Wall", interior=True, color="E8DCC4")

entrance = Door("Double Door", width=1.6, depth=0.1, height=2.2, color="8B4513")
windows = [Window("Window", width=1.8, depth=0.1, height=1.5, color="87CEEB") for _ in range(3)]

# Main bookshelves along the walls
wall_bookshelves = [Object("Tall Bookshelf", width=1.8, depth=0.4, height=2.8, support=STANDING, color="8B4513") for _ in range(8)]

# Island bookshelves in the middle
island_bookshelves = [Object("Double-sided Bookshelf", width=2.4, depth=0.8, height=1.8, support=STANDING, color="A0522D") for _ in range(3)]

# Reading areas
reading_tables = [Object("Reading Table", width=1.2, depth=0.8, height=0.75, support=STANDING, color="DEB887") for _ in range(3)]
chairs = [Object("Library Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="8B008B") for _ in range(12)]

# Librarian's area
desk = Object("Librarian Desk", width=1.8, depth=0.8, height=0.75, support=STANDING, color="CD853F")
office_chair = Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="4B0082")
computer = Object("Desktop Computer", width=0.5, depth=0.4, height=0.4, support=STANDING, color="708090")

# Reading nook
armchairs = [Object("Armchair", width=0.9, depth=0.9, height=1.0, support=STANDING, color="483D8B") for _ in range(2)]
side_table = Object("Side Table", width=0.5, depth=0.5, height=0.6, support=STANDING, color="B8860B")
reading_lamp = Object("Table Lamp", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FFD700")

# Book return cart
cart = Object("Book Cart", width=0.9, depth=0.6, height=1.0, support=STANDING, color="4682B4")

# Decorative elements
globe = Object("Globe", width=0.4, depth=0.4, height=0.6, support=STANDING, color="32CD32")
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(3)]