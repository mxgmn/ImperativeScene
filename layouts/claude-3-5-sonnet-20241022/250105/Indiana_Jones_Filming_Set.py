set_title("Indiana Jones Film Set")
set_size(width=20, depth=15, height=4)
set_floor_asset("Sandy Floor", color="C2B280")
set_wall_asset("Temple Wall", interior=True, color="8B7355")

entrance = Door("Temple Door", width=2.5, depth=0.3, height=3.0, color="CD853F")

# Main temple set pieces
altar = Object("Stone Altar", width=2.0, depth=1.2, height=1.0, support=STANDING, color="8B4513")
idol = Object("Golden Idol", width=0.3, depth=0.3, height=0.4, support=STANDING, color="FFD700")
pillars = [Object("Stone Pillar", width=1.0, depth=1.0, height=3.5, support=STANDING, color="A0522D") for _ in range(4)]
sarcophagus = Object("Stone Sarcophagus", width=1.2, depth=2.2, height=0.8, support=STANDING, color="8B7355")

# Film equipment
cameras = [Object("Movie Camera", width=0.6, depth=0.8, height=1.5, support=STANDING, color="2F4F4F") for _ in range(3)]
lights = [Object("Studio Light", width=0.5, depth=0.5, height=1.8, support=STANDING, color="FFA500") for _ in range(4)]
boom_mic = Object("Boom Microphone", width=0.2, depth=2.0, height=0.2, support=STANDING, color="708090")
director_chair = Object("Director Chair", width=0.6, depth=0.5, height=1.0, support=STANDING, color="8B4513")

# Set dressing
props = [Object("Prop Crate", width=1.0, depth=0.8, height=0.6, support=STANDING, color="DEB887") for _ in range(5)]
fake_rocks = [Object("Foam Rock", width=1.2, depth=1.0, height=0.8, support=STANDING, color="696969") for _ in range(4)]
snake_basket = Object("Wicker Basket", width=0.4, depth=0.4, height=0.3, support=STANDING, color="D2691E")
treasure_chest = Object("Wooden Chest", width=0.8, depth=0.5, height=0.4, support=STANDING, color="8B4513")

# Special effects equipment
smoke_machine = Object("Smoke Machine", width=0.5, depth=0.7, height=0.4, support=STANDING, color="4682B4")
green_screen = Object("Green Screen", width=12.0, depth=0.2, height=3.0, support=STANDING, color="32CD32")

# Safety equipment
first_aid = Object("First Aid Station", width=0.8, depth=0.4, height=1.2, support=STANDING, color="FF0000")
fire_extinguisher = Object("Fire Extinguisher", width=0.2, depth=0.2, height=0.5, support=STANDING, color="FF4500")

entrance.center.x = scene.min.x + 0.5 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

altar.center.x = scene.center.x
altar.center.y = scene.center.y
altar.min.z = scene.min.z
altar.facing = Y_MIN

set_coordinate_frame(altar)
idol.center.x = altar.center.x
idol.center.y = altar.center.y
idol.min.z = altar.max.z
idol.facing = altar.facing
set_coordinate_frame(scene)

pillar_offset = 3.0
for i, pillar in enumerate(pillars):
    if i < 2:
        pillar.center.x = altar.center.x - pillar_offset if i == 0 else altar.center.x + pillar_offset
        pillar.center.y = altar.center.y + pillar_offset
    else:
        pillar.center.x = altar.center.x - pillar_offset if i == 2 else altar.center.x + pillar_offset
        pillar.center.y = altar.center.y - pillar_offset
    pillar.min.z = scene.min.z
    pillar.facing = Y_MIN

sarcophagus.center.x = scene.center.x
sarcophagus.max.y = altar.min.y - 1.0
sarcophagus.min.z = scene.min.z
sarcophagus.facing = Y_MAX

green_screen.center.x = scene.center.x
green_screen.max.y = scene.max.y
green_screen.min.z = scene.min.z
green_screen.facing = Y_MIN

camera_positions = [(0.25, 0.3), (0.5, 0.7), (0.75, 0.3)]
for i, camera in enumerate(cameras):
    camera.center.x = scene.min.x + camera_positions[i][0] * scene.width
    camera.center.y = scene.min.y + camera_positions[i][1] * scene.depth
    camera.min.z = scene.min.z
    camera.facing = altar

light_positions = [(0.2, 0.2), (0.8, 0.2), (0.2, 0.8), (0.8, 0.8)]
for i, light in enumerate(lights):
    light.center.x = scene.min.x + light_positions[i][0] * scene.width
    light.center.y = scene.min.y + light_positions[i][1] * scene.depth
    light.min.z = scene.min.z
    light.facing = altar

boom_mic.center.x = altar.center.x
boom_mic.center.y = altar.min.y - 2.0
boom_mic.min.z = 2.5
boom_mic.facing = altar

director_chair.min.x = scene.min.x + 0.2
director_chair.min.y = scene.min.y + 0.2
director_chair.min.z = scene.min.z
director_chair.facing = altar

prop_spacing = 1.2
for i, prop in enumerate(props):
    prop.min.x = scene.max.x - 2.0
    prop.center.y = scene.min.y + (i + 1.0) * prop_spacing
    prop.min.z = scene.min.z
    prop.facing = X_MIN

for i, rock in enumerate(fake_rocks):
    rock.center.x = scene.min.x + (i + 1.0) / 5.0 * scene.width
    rock.min.y = scene.min.y + 0.5
    rock.min.z = scene.min.z
    rock.facing = Y_MAX

snake_basket.min.x = altar.min.x - 1.0
snake_basket.min.y = altar.min.y - 1.0
snake_basket.min.z = scene.min.z
snake_basket.facing = altar

treasure_chest.max.x = altar.max.x + 1.0
treasure_chest.min.y = altar.min.y - 1.0
treasure_chest.min.z = scene.min.z
treasure_chest.facing = altar

smoke_machine.min.x = scene.min.x + 1.0
smoke_machine.max.y = scene.max.y - 1.0
smoke_machine.min.z = scene.min.z
smoke_machine.facing = altar

first_aid.max.x = scene.max.x - 0.2
first_aid.min.y = scene.min.y + 0.2
first_aid.min.z = scene.min.z
first_aid.facing = X_MIN

fire_extinguisher.max.x = scene.max.x - 0.2
fire_extinguisher.max.y = scene.max.y - 0.2
fire_extinguisher.min.z = scene.min.z
fire_extinguisher.facing = X_MIN