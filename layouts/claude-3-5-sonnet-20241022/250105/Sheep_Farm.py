set_title("Sheep Farm")
set_size(width=25, depth=20, height=3)
set_floor_asset("Grass Ground", color="567D46")
set_wall_asset("Wooden Fence", interior=False, color="8B4513")

barn = Object("Wooden Barn", width=6.0, depth=8.0, height=3.0, support=STANDING, color="CD853F")

# Main features
water_trough = Object("Water Trough", width=2.0, depth=0.8, height=0.4, support=STANDING, color="5F9EA0")
hay_feeder = Object("Hay Feeder", width=2.5, depth=1.0, height=1.2, support=STANDING, color="DAA520")
sheep_shelter = Object("Wooden Shelter", width=4.0, depth=3.0, height=2.0, support=STANDING, color="A0522D")

# Equipment and storage
hay_bales = [Object("Hay Bale", width=1.2, depth=1.2, height=1.0, support=STANDING, color="F4A460") for _ in range(6)]
tractors = [Object("Tractor", width=2.0, depth=4.0, height=2.0, support=STANDING, color="FF4500")]
wheelbarrow = Object("Wheelbarrow", width=0.8, depth=1.5, height=0.6, support=STANDING, color="8B0000")

# Animals (represented as objects for gameplay purposes)
sheep = [Object("Sheep", width=0.8, depth=1.2, height=1.0, support=STANDING, color="F5F5F5") for _ in range(8)]
ram = Object("Ram", width=1.0, depth=1.4, height=1.2, support=STANDING, color="E6E6E6")

# Storage and equipment
tool_shed = Object("Tool Shed", width=3.0, depth=2.0, height=2.2, support=STANDING, color="8B7355")
feed_bin = Object("Feed Storage Bin", width=1.5, depth=1.5, height=1.8, support=STANDING, color="BDB76B")

# Decorative elements
windmill = Object("Windmill", width=2.0, depth=2.0, height=3.0, support=STANDING, color="D2B48C")
trees = [Object("Apple Tree", width=3.0, depth=3.0, height=3.0, support=STANDING, color="228B22") for _ in range(3)]

barn.center.x = scene.min.x + 0.3 * scene.width
barn.center.y = scene.min.y + 0.3 * scene.depth
barn.min.z = scene.min.z
barn.facing = Y_MAX

water_trough.center.x = scene.center.x
water_trough.center.y = scene.center.y
water_trough.min.z = scene.min.z
water_trough.facing = X_MAX

hay_feeder.center.x = water_trough.center.x + 2.0
hay_feeder.center.y = water_trough.center.y
hay_feeder.min.z = scene.min.z
hay_feeder.facing = X_MAX

sheep_shelter.max.x = scene.max.x - 0.1 * scene.width
sheep_shelter.center.y = scene.center.y
sheep_shelter.min.z = scene.min.z
sheep_shelter.facing = X_MIN

param = 1.5
for i, hay_bale in enumerate(hay_bales):
    hay_bale.center.x = barn.max.x + param
    hay_bale.center.y = barn.min.y + (i+0.5) * param
    hay_bale.min.z = scene.min.z
    hay_bale.facing = X_MAX

tractors[0].min.x = scene.min.x + 0.1 * scene.width
tractors[0].min.y = scene.min.y + 0.1 * scene.depth
tractors[0].min.z = scene.min.z
tractors[0].facing = Y_MAX

wheelbarrow.min.x = barn.max.x + 0.1
wheelbarrow.min.y = barn.max.y + 0.1
wheelbarrow.min.z = scene.min.z
wheelbarrow.facing = X_MAX

param = 2.0
for i, sheep_obj in enumerate(sheep):
    sheep_obj.center.x = scene.center.x + (i % 4 - 1.5) * param
    sheep_obj.center.y = scene.center.y + (i // 4 - 1.0) * param
    sheep_obj.min.z = scene.min.z
    sheep_obj.facing = Y_MAX

ram.center.x = sheep[0].center.x - param
ram.center.y = sheep[0].center.y
ram.min.z = scene.min.z
ram.facing = sheep[0]

tool_shed.min.x = scene.min.x + 0.05 * scene.width
tool_shed.max.y = scene.max.y - 0.05 * scene.depth
tool_shed.min.z = scene.min.z
tool_shed.facing = X_MAX

feed_bin.min.x = tool_shed.max.x + 0.1
feed_bin.max.y = scene.max.y - 0.05 * scene.depth
feed_bin.min.z = scene.min.z
feed_bin.facing = X_MAX

windmill.max.x = scene.max.x - 0.05 * scene.width
windmill.min.y = scene.min.y + 0.05 * scene.depth
windmill.min.z = scene.min.z
windmill.facing = X_MIN

param = 0.25
for i, tree in enumerate(trees):
    tree.center.x = scene.min.x + (i+1.0) * param * scene.width
    tree.min.y = scene.min.y + 0.05 * scene.depth
    tree.min.z = scene.min.z
    tree.facing = Y_MAX