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

gate.center.x = scene.min.x + 0.5 * scene.width
gate.min.y = scene.min.y
gate.min.z = scene.min.z
gate.facing = Y_MAX

guard_tower.max.x = scene.max.x - 0.1 * scene.width
guard_tower.min.y = scene.min.y + 0.1 * scene.depth
guard_tower.min.z = scene.min.z
guard_tower.facing = Y_MAX

for i, barrier in enumerate(barriers):
    barrier.center.x = gate.center.x + (1 if i == 0 else -1) * (gate.width/2 + barrier.width)
    barrier.min.y = scene.min.y
    barrier.min.z = scene.min.z
    barrier.facing = Y_MAX

parking_offset = 0.15
for i, jeep in enumerate(jeeps):
    jeep.center.x = scene.min.x + (i + 1.0) * parking_offset * scene.width
    jeep.center.y = scene.min.y + 0.2 * scene.depth
    jeep.min.z = scene.min.z
    jeep.facing = Y_MAX

generator.max.x = scene.max.x - 0.05 * scene.width
generator.max.y = scene.max.y - 0.05 * scene.depth
generator.min.z = scene.min.z
generator.facing = X_MIN

feeding_station.center.x = scene.min.x + 0.7 * scene.width
feeding_station.center.y = scene.min.y + 0.6 * scene.depth
feeding_station.min.z = scene.min.z
feeding_station.facing = Y_MIN

water_pond.center.x = scene.min.x + 0.3 * scene.width
water_pond.center.y = scene.min.y + 0.7 * scene.depth
water_pond.min.z = scene.min.z
water_pond.facing = Y_MAX

tree_spacing = 0.2
for i, tree in enumerate(trees):
    tree.center.x = scene.min.x + ((i % 3) + 1.0) * tree_spacing * scene.width
    tree.center.y = scene.min.y + ((i // 3) + 1.0) * tree_spacing * scene.depth
    tree.min.z = scene.min.z
    tree.facing = Y_MAX

bush_spacing = 0.15
for i, bush in enumerate(bushes):
    bush.center.x = scene.min.x + ((i % 4) + 2.0) * bush_spacing * scene.width
    bush.center.y = scene.min.y + ((i // 4) + 2.0) * bush_spacing * scene.depth
    bush.min.z = scene.min.z
    bush.facing = Y_MAX

fern_spacing = 0.1
for i, fern in enumerate(ferns):
    fern.center.x = scene.min.x + ((i % 5) + 3.0) * fern_spacing * scene.width
    fern.center.y = scene.min.y + ((i // 5) + 3.0) * fern_spacing * scene.depth
    fern.min.z = scene.min.z
    fern.facing = Y_MAX

lab_building.min.x = scene.min.x + 0.1 * scene.width
lab_building.max.y = scene.max.y - 0.1 * scene.depth
lab_building.min.z = scene.min.z
lab_building.facing = Y_MIN

storage_container.max.x = scene.max.x - 0.15 * scene.width
storage_container.center.y = scene.center.y
storage_container.min.z = scene.min.z
storage_container.facing = X_MIN

beacon_spacing = 0.25
for i, beacon in enumerate(warning_beacons):
    if i < 2:
        beacon.center.x = scene.min.x + (i + 1.0) * beacon_spacing * scene.width
    else:
        beacon.center.x = scene.max.x - (i - 1.0) * beacon_spacing * scene.width
    beacon.center.y = scene.center.y
    beacon.min.z = scene.min.z
    beacon.facing = Y_MAX

speaker_spacing = 0.2
for i, speaker in enumerate(speakers):
    speaker.center.x = scene.min.x + (i + 1.0) * speaker_spacing * scene.width
    speaker.max.y = scene.max.y
    speaker.max.z = scene.max.z - 1.0
    speaker.facing = Y_MIN

shelter.min.x = scene.min.x + 0.05 * scene.width
shelter.min.y = scene.min.y + 0.05 * scene.depth
shelter.min.z = scene.min.z
shelter.facing = X_MAX