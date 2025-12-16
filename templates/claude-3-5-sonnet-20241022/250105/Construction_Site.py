set_title("Construction Site")
set_size(width=15, depth=20, height=4)
set_floor_asset("Dirt Ground", color="8B7355")
set_wall_asset("Construction Fence", interior=False, color="CD853F")

entrance_gate = Door("Construction Gate", width=3.0, depth=0.1, height=2.2, color="B8860B")

# Main construction elements
foundation = Object("Concrete Foundation", width=8.0, depth=10.0, height=0.3, support=STANDING, color="A0A0A0")
scaffold = Object("Scaffolding", width=6.0, depth=1.0, height=3.5, support=STANDING, color="4682B4")
brick_pile = Object("Brick Stack", width=2.0, depth=1.5, height=1.2, support=STANDING, color="CD5C5C")
lumber_pile = [Object("Lumber Stack", width=3.0, depth=0.8, height=0.6, support=STANDING, color="DEB887") for _ in range(2)]

# Equipment
crane = Object("Mobile Crane", width=2.5, depth=4.0, height=3.5, support=STANDING, color="FFD700")
cement_mixer = Object("Cement Mixer", width=1.2, depth=1.8, height=1.5, support=STANDING, color="FF4500")
wheelbarrows = [Object("Wheelbarrow", width=0.8, depth=1.4, height=0.6, support=STANDING, color="1E90FF") for _ in range(2)]
generator = Object("Generator", width=1.0, depth=1.5, height=1.2, support=STANDING, color="4169E1")

# Site facilities
office_container = Object("Site Office Container", width=2.4, depth=6.0, height=2.4, support=STANDING, color="87CEEB")
portable_toilet = Object("Portable Toilet", width=1.2, depth=1.2, height=2.2, support=STANDING, color="6B8E23")
tool_container = Object("Storage Container", width=2.4, depth=6.0, height=2.4, support=STANDING, color="CD853F")

# Safety equipment
barriers = [Object("Safety Barrier", width=2.0, depth=0.2, height=1.0, support=STANDING, color="FF6B6B") for _ in range(6)]
cones = [Object("Traffic Cone", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FFA500") for _ in range(8)]