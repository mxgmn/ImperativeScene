set_title("City Block")
set_size(width=30, depth=30, height=20)
set_floor_asset("Asphalt Road", color="454545")
set_wall_asset("Building Wall", interior=False, color="A0A0A0")

# Main buildings (just facades, as we're creating a small section of a city)
buildings = [
    Object("Office Building", width=12, depth=8, height=20, support=STANDING, color="708090"),
    Object("Apartment Building", width=10, depth=8, height=16, support=STANDING, color="CD853F"),
    Object("Corner Store", width=8, depth=6, height=4, support=STANDING, color="B8860B"),
    Object("Coffee Shop", width=6, depth=6, height=4, support=STANDING, color="8B4513")
]

# Street furniture
benches = [Object("Park Bench", width=1.5, depth=0.6, height=0.5, support=STANDING, color="8B4513") for _ in range(4)]
trash_bins = [Object("Trash Bin", width=0.5, depth=0.5, height=1.0, support=STANDING, color="2F4F4F") for _ in range(3)]
street_lamps = [Object("Street Lamp", width=0.3, depth=0.3, height=3.0, support=STANDING, color="FFD700") for _ in range(6)]

# Vehicles
parked_cars = [Object("Car", width=1.8, depth=4.2, height=1.5, support=STANDING, color=color) for color in ["FF4500", "4682B4", "2E8B57"]]
delivery_truck = Object("Delivery Truck", width=2.2, depth=6.0, height=2.8, support=STANDING, color="B8860B")

# Vegetation
trees = [Object("Street Tree", width=2.5, depth=2.5, height=4.0, support=STANDING, color="228B22") for _ in range(6)]
planters = [Object("Planter Box", width=1.0, depth=1.0, height=0.6, support=STANDING, color="8B4513") for _ in range(4)]

# Store elements
store_signs = [Object("Store Sign", width=2.0, depth=0.2, height=1.0, support=MOUNTED, color="4169E1") for _ in range(3)]
awning = Object("Shop Awning", width=3.0, depth=1.0, height=0.5, support=MOUNTED, color="DC143C")

# Bus stop
bus_shelter = Object("Bus Shelter", width=3.0, depth=1.5, height=2.2, support=STANDING, color="87CEEB")
bus_stop_sign = Object("Bus Stop Sign", width=0.2, depth=0.2, height=2.5, support=STANDING, color="FF6347")

# Fire hydrants
hydrants = [Object("Fire Hydrant", width=0.3, depth=0.3, height=0.8, support=STANDING, color="FF0000") for _ in range(2)]

# Place main buildings
buildings[0].min.x = scene.min.x  # Office building
buildings[0].max.y = scene.max.y
buildings[0].min.z = scene.min.z
buildings[0].facing = Y_MIN

buildings[1].max.x = scene.max.x  # Apartment building
buildings[1].max.y = scene.max.y
buildings[1].min.z = scene.min.z
buildings[1].facing = Y_MIN

buildings[2].min.x = scene.min.x  # Corner store
buildings[2].min.y = scene.min.y
buildings[2].min.z = scene.min.z
buildings[2].facing = Y_MAX

buildings[3].max.x = scene.max.x  # Coffee shop
buildings[3].min.y = scene.min.y
buildings[3].min.z = scene.min.z
buildings[3].facing = Y_MAX

# Place street furniture
spacing = 0.2 * scene.width
for i, bench in enumerate(benches):
    bench.center.x = scene.min.x + (i+1.0) * spacing
    bench.center.y = scene.center.y
    bench.min.z = scene.min.z
    bench.facing = Y_MAX

for i, bin in enumerate(trash_bins):
    bin.center.x = scene.min.x + (i+1.5) * spacing
    bin.min.y = scene.min.y + 0.1 * scene.depth
    bin.min.z = scene.min.z
    bin.facing = Y_MAX

lamp_spacing = 0.15 * scene.width
for i, lamp in enumerate(street_lamps):
    if i < 3:
        lamp.center.x = scene.min.x + (i+1.0) * lamp_spacing
        lamp.min.y = scene.min.y + 0.1 * scene.depth
    else:
        lamp.center.x = scene.max.x - (i-2.0) * lamp_spacing
        lamp.max.y = scene.max.y - 0.1 * scene.depth
    lamp.min.z = scene.min.z
    lamp.facing = Y_MAX

# Place vehicles
car_spacing = 0.15 * scene.width
for i, car in enumerate(parked_cars):
    car.center.x = scene.min.x + (i+1.0) * car_spacing
    car.center.y = scene.center.y
    car.min.z = scene.min.z
    car.facing = Y_MAX

delivery_truck.max.x = scene.max.x - 0.1 * scene.width
delivery_truck.min.y = scene.min.y + 0.2 * scene.depth
delivery_truck.min.z = scene.min.z
delivery_truck.facing = Y_MAX

# Place vegetation
tree_spacing = 0.15 * scene.width
for i, tree in enumerate(trees):
    if i < 3:
        tree.center.x = scene.min.x + (i+1.0) * tree_spacing
        tree.min.y = scene.min.y + 0.15 * scene.depth
    else:
        tree.center.x = scene.max.x - (i-2.0) * tree_spacing
        tree.max.y = scene.max.y - 0.15 * scene.depth
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

planter_spacing = 0.2 * scene.width
for i, planter in enumerate(planters):
    planter.center.x = scene.min.x + (i+1.0) * planter_spacing
    planter.center.y = scene.center.y
    planter.min.z = scene.min.z
    planter.facing = Y_MAX

# Place store elements
for i, sign in enumerate(store_signs):
    sign.center.x = buildings[2].min.x + (i+1.0) * (buildings[2].width/4.0)
    sign.min.y = buildings[2].min.y
    sign.min.z = buildings[2].height * 0.75
    sign.facing = Y_MAX

awning.center.x = buildings[3].center.x
awning.min.y = buildings[3].min.y
awning.min.z = buildings[3].height * 0.6
awning.facing = Y_MAX

# Place bus stop
bus_shelter.center.x = scene.center.x
bus_shelter.min.y = scene.min.y + 0.1 * scene.depth
bus_shelter.min.z = scene.min.z
bus_shelter.facing = Y_MAX

bus_stop_sign.min.x = bus_shelter.max.x + 0.5
bus_stop_sign.center.y = bus_shelter.center.y
bus_stop_sign.min.z = scene.min.z
bus_stop_sign.facing = Y_MAX

# Place hydrants
hydrants[0].min.x = scene.min.x + 0.1 * scene.width
hydrants[0].min.y = scene.min.y + 0.1 * scene.depth
hydrants[0].min.z = scene.min.z
hydrants[0].facing = Y_MAX

hydrants[1].max.x = scene.max.x - 0.1 * scene.width
hydrants[1].max.y = scene.max.y - 0.1 * scene.depth
hydrants[1].min.z = scene.min.z
hydrants[1].facing = Y_MIN