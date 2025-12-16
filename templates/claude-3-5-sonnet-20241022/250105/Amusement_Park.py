set_title("Amusement Park Section")
set_size(width=25, depth=25, height=15)
set_floor_asset("Concrete Tiles Floor", color="9B9B9B")
set_wall_asset("Park Fence", interior=False, color="4A4A4A")

entrance_gate = Door("Decorative Gate", width=3.0, depth=0.3, height=3.5, color="4169E1")

# Main attraction - a carousel
carousel_base = Object("Carousel Platform", width=8.0, depth=8.0, height=0.5, support=STANDING, color="FFD700")
carousel_center = Object("Carousel Column", width=1.0, depth=1.0, height=4.0, support=STANDING, color="B22222")
carousel_horses = [Object("Carousel Horse", width=0.8, depth=1.5, height=1.5, support=STANDING, color="FF69B4") for _ in range(8)]

# Food and refreshments
food_stands = [
    Object("Hot Dog Stand", width=2.5, depth=1.5, height=2.2, support=STANDING, color="FF4500"),
    Object("Ice Cream Cart", width=1.8, depth=1.2, height=1.8, support=STANDING, color="87CEEB"),
    Object("Popcorn Stand", width=2.0, depth=1.5, height=2.0, support=STANDING, color="FFFF00")
]

# Seating and rest areas
benches = [Object("Park Bench", width=1.5, depth=0.6, height=0.9, support=STANDING, color="8B4513") for _ in range(6)]
trash_bins = [Object("Trash Bin", width=0.4, depth=0.4, height=0.8, support=STANDING, color="228B22") for _ in range(4)]

# Decorative elements
planters = [Object("Large Planter", width=1.2, depth=1.2, height=0.6, support=STANDING, color="CD853F") for _ in range(4)]
trees = [Object("Decorative Tree", width=2.0, depth=2.0, height=4.0, support=STANDING, color="228B22") for _ in range(3)]
lamp_posts = [Object("Lamp Post", width=0.3, depth=0.3, height=3.0, support=STANDING, color="FFA500") for _ in range(6)]

# Game booths
game_booths = [
    Object("Ring Toss Booth", width=3.0, depth=2.0, height=2.5, support=STANDING, color="9370DB"),
    Object("Balloon Pop Booth", width=3.0, depth=2.0, height=2.5, support=STANDING, color="FF6347")
]

# Ticket booth
ticket_booth = Object("Ticket Booth", width=2.0, depth=2.0, height=2.5, support=STANDING, color="4682B4")