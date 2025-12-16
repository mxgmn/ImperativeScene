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