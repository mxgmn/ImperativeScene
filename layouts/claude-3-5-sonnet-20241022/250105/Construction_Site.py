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

entrance_gate.center.x = scene.min.x + 0.3 * scene.width
entrance_gate.min.y = scene.min.y
entrance_gate.min.z = scene.min.z
entrance_gate.facing = Y_MAX

foundation.center.x = scene.center.x
foundation.center.y = scene.center.y
foundation.min.z = scene.min.z
foundation.facing = Y_MAX

scaffold.min.x = foundation.min.x
scaffold.center.y = foundation.center.y
scaffold.min.z = foundation.max.z
scaffold.facing = X_MAX

brick_pile.max.x = scene.max.x - 0.2 * scene.width
brick_pile.min.y = scene.min.y + 0.2 * scene.depth
brick_pile.min.z = scene.min.z
brick_pile.facing = X_MIN

for i, lumber in enumerate(lumber_pile):
    lumber.min.x = scene.min.x + 0.1 * scene.width
    lumber.min.y = scene.min.y + (i+1.0) * 0.15 * scene.depth
    lumber.min.z = scene.min.z
    lumber.facing = Y_MAX

crane.max.x = scene.max.x - 0.1 * scene.width
crane.max.y = scene.max.y - 0.1 * scene.depth
crane.min.z = scene.min.z
crane.facing = foundation

cement_mixer.min.x = foundation.max.x + 0.1 * scene.width
cement_mixer.center.y = foundation.center.y
cement_mixer.min.z = scene.min.z
cement_mixer.facing = foundation

for i, wheelbarrow in enumerate(wheelbarrows):
    wheelbarrow.min.x = foundation.max.x + 0.05 * scene.width
    wheelbarrow.min.y = foundation.min.y + (i+1.0) * 0.2 * foundation.depth
    wheelbarrow.min.z = scene.min.z
    wheelbarrow.facing = foundation

generator.max.x = scene.max.x - 0.05 * scene.width
generator.min.y = scene.min.y + 0.1 * scene.depth
generator.min.z = scene.min.z
generator.facing = X_MIN

office_container.min.x = scene.min.x + 0.05 * scene.width
office_container.max.y = scene.max.y - 0.1 * scene.depth
office_container.min.z = scene.min.z
office_container.facing = Y_MIN

portable_toilet.max.x = scene.max.x - 0.05 * scene.width
portable_toilet.min.y = scene.min.y + 0.05 * scene.depth
portable_toilet.min.z = scene.min.z
portable_toilet.facing = X_MIN

tool_container.max.x = scene.max.x - 0.05 * scene.width
tool_container.max.y = scene.max.y - 0.1 * scene.depth
tool_container.min.z = scene.min.z
tool_container.facing = Y_MIN

barrier_spacing = 0.15
for i, barrier in enumerate(barriers):
    if i < 3:
        barrier.center.x = foundation.min.x + (i+1.0) * foundation.width/4.0
        barrier.min.y = foundation.min.y - barrier_spacing * scene.depth
    else:
        barrier.center.x = foundation.min.x + (i-2.0) * foundation.width/4.0
        barrier.max.y = foundation.max.y + barrier_spacing * scene.depth
    barrier.min.z = scene.min.z
    barrier.facing = foundation

cone_spacing = 0.1
for i, cone in enumerate(cones):
    if i < 4:
        cone.min.x = entrance_gate.min.x + (i+1.0) * entrance_gate.width/5.0
        cone.min.y = entrance_gate.max.y + cone_spacing * scene.depth
    else:
        cone.min.x = entrance_gate.min.x + (i-3.0) * entrance_gate.width/5.0
        cone.max.y = entrance_gate.min.y - cone_spacing * scene.depth
    cone.min.z = scene.min.z
    cone.facing = entrance_gate