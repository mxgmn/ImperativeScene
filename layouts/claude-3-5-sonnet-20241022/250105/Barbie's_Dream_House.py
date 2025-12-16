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

entrance.max.x = scene.max.x - 0.2 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.max.y = scene.max.y
    window.min.z = 0.8
    window.facing = Y_MIN

# Living Area
sofa.center.x = scene.min.x + 0.3 * scene.width
sofa.center.y = scene.min.y + 0.3 * scene.depth
sofa.min.z = scene.min.z
sofa.facing = Y_MAX

coffee_table.center.x = sofa.center.x
coffee_table.center.y = sofa.center.y + 0.8
coffee_table.min.z = scene.min.z
coffee_table.facing = sofa

tv_stand.center.x = sofa.center.x
tv_stand.max.y = scene.max.y - 0.1
tv_stand.min.z = scene.min.z
tv_stand.facing = Y_MIN

set_coordinate_frame(tv_stand)
tv.center.x = tv_stand.center.x
tv.min.y = tv_stand.min.y
tv.min.z = tv_stand.max.z + 0.1
tv.facing = tv_stand.facing
set_coordinate_frame(scene)

# Bedroom Area
bed.max.x = scene.max.x - 0.1
bed.center.y = scene.min.y + 0.35 * scene.depth
bed.min.z = scene.min.z
bed.facing = Y_MAX

wardrobe.max.x = scene.max.x - 0.1
wardrobe.max.y = scene.max.y - 0.1
wardrobe.min.z = scene.min.z
wardrobe.facing = X_MIN

vanity.center.x = bed.center.x - 1.0
vanity.center.y = bed.center.y
vanity.min.z = scene.min.z
vanity.facing = Y_MAX

set_coordinate_frame(vanity)
vanity_chair.center.x = vanity.center.x
vanity_chair.min.y = vanity.max.y + 0.1
vanity_chair.min.z = scene.min.z
vanity_chair.facing = vanity
set_coordinate_frame(scene)

# Kitchen Area
kitchen_counter.min.x = scene.min.x + 0.1
kitchen_counter.max.y = scene.max.y - 0.1
kitchen_counter.min.z = scene.min.z
kitchen_counter.facing = Y_MIN

fridge.min.x = kitchen_counter.max.x + 0.1
fridge.max.y = scene.max.y - 0.1
fridge.min.z = scene.min.z
fridge.facing = Y_MIN

dining_table.center.x = scene.min.x + 0.25 * scene.width
dining_table.center.y = scene.max.y - 0.3 * scene.depth
dining_table.min.z = scene.min.z
dining_table.facing = Y_MIN

for i, chair in enumerate(dining_chairs):
    angle = i * 1.57  # 90 degrees in radians
    radius = 0.8
    chair.center.x = dining_table.center.x + radius * cos(angle)
    chair.center.y = dining_table.center.y + radius * sin(angle)
    chair.min.z = scene.min.z
    chair.facing = dining_table

# Decorative Elements
rugs[0].center = sofa.center
rugs[0].min.z = scene.min.z
rugs[1].center = bed.center
rugs[1].min.z = scene.min.z

for i, plant in enumerate(plants):
    if i == 0:
        plant.min.x = scene.min.x + 0.1
        plant.min.y = scene.min.y + 0.1
    elif i == 1:
        plant.max.x = scene.max.x - 0.1
        plant.min.y = scene.min.y + 0.1
    else:
        plant.center = dining_table.center
        plant.min.z = dining_table.max.z
    plant.min.z = scene.min.z
    plant.facing = Y_MAX

for i, painting in enumerate(paintings):
    painting.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    painting.min.y = scene.min.y + 0.1
    painting.min.z = 1.5
    painting.facing = Y_MAX