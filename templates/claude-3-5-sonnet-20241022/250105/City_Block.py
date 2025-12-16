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