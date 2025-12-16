set_title("Barbie's Dream House")
set_size(width=12, depth=8, height=3)
set_floor_asset("Wooden Floor", color="FFE4E1")  # Light pink wood
set_wall_asset("Wallpaper Wall", interior=True, color="FFB6C1")  # Pink wallpaper

entrance = Door("Modern Door", width=1.0, depth=0.1, height=2.2, color="FF69B4")
windows = [Window("Large Window", width=1.5, depth=0.1, height=1.8, color="87CEEB") for _ in range(3)]

# Living Area
sofa = Object("Modern Sofa", width=2.2, depth=0.9, height=0.9, support=STANDING, color="FF1493")  # Deep pink
coffee_table = Object("Glass Table", width=1.2, depth=0.6, height=0.45, support=STANDING, color="E0FFFF")  # Light cyan
tv = Object("Flat Screen TV", width=1.6, depth=0.1, height=0.9, support=MOUNTED, color="FF69B4")
tv_stand = Object("TV Stand", width=1.8, depth=0.4, height=0.5, support=STANDING, color="DDA0DD")

# Bedroom Area
bed = Object("Princess Bed", width=2.0, depth=2.4, height=0.6, support=STANDING, color="FF69B4")
wardrobe = Object("Walk-in Closet", width=2.4, depth=0.6, height=2.2, support=STANDING, color="FFB6C1")
vanity = Object("Makeup Vanity", width=1.2, depth=0.5, height=0.75, support=STANDING, color="FFC0CB")
vanity_chair = Object("Vanity Chair", width=0.4, depth=0.4, height=0.5, support=STANDING, color="FF69B4")

# Kitchen Area
kitchen_counter = Object("Modern Counter", width=2.5, depth=0.6, height=0.9, support=STANDING, color="FFE4E1")
fridge = Object("Retro Fridge", width=0.8, depth=0.7, height=1.8, support=STANDING, color="FF69B4")
dining_table = Object("Round Table", width=1.2, depth=1.2, height=0.75, support=STANDING, color="FFC0CB")
dining_chairs = [Object("Dining Chair", width=0.4, depth=0.4, height=0.9, support=STANDING, color="FF69B4") for _ in range(4)]

# Decorative Elements
rugs = [Object("Round Rug", width=1.8, depth=1.8, height=0.02, support=STANDING, color="FF1493") for _ in range(2)]
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=1.2, support=STANDING, color="98FB98") for _ in range(3)]
paintings = [Object("Fashion Poster", width=0.6, depth=0.05, height=0.8, support=MOUNTED, color="FF69B4") for _ in range(3)]