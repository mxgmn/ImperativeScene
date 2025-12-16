set_title("Jurassic Park Compound")
set_size(width=30, depth=30, height=6)
set_floor_asset("Dirt Ground", color="8B7355")
set_wall_asset("Electric Fence", interior=False, color="707070")

# Main entrance and security
gate = Door("Security Gate", width=6.0, depth=0.3, height=4.0, color="CD853F")
guard_tower = Object("Watch Tower", width=3.0, depth=3.0, height=6.0, support=STANDING, color="8B4513")
barriers = [Object("Security Barrier", width=0.3, depth=2.0, height=1.0, support=STANDING, color="FF4500") for _ in range(2)]

# Vehicles and equipment
jeeps = [Object("Off-road Vehicle", width=2.0, depth=4.5, height=1.8, support=STANDING, color="FFD700") for _ in range(3)]
generator = Object("Power Generator", width=2.5, depth=2.5, height=2.0, support=STANDING, color="4682B4")

# Enclosure features
feeding_station = Object("Feeding Station", width=3.0, depth=2.0, height=2.5, support=STANDING, color="8FBC8F")
water_pond = Object("Water Feature", width=4.0, depth=3.0, height=0.5, support=STANDING, color="4F94CD")

# Flora
trees = [Object("Tropical Tree", width=2.0, depth=2.0, height=5.0, support=STANDING, color="228B22") for _ in range(6)]
bushes = [Object("Dense Bush", width=1.5, depth=1.5, height=1.0, support=STANDING, color="32CD32") for _ in range(8)]
ferns = [Object("Large Fern", width=1.0, depth=1.0, height=0.8, support=STANDING, color="90EE90") for _ in range(10)]

# Research facilities
lab_building = Object("Research Building", width=8.0, depth=6.0, height=4.0, support=STANDING, color="B8860B")
storage_container = Object("Storage Container", width=6.0, depth=2.5, height=2.5, support=STANDING, color="CD853F")

# Warning systems
warning_beacons = [Object("Warning Beacon", width=0.5, depth=0.5, height=2.0, support=STANDING, color="FF0000") for _ in range(4)]
speakers = [Object("Speaker System", width=0.4, depth=0.4, height=0.6, support=MOUNTED, color="696969") for _ in range(6)]

# Emergency equipment
shelter = Object("Emergency Shelter", width=4.0, depth=3.0, height=2.5, support=STANDING, color="A0522D")