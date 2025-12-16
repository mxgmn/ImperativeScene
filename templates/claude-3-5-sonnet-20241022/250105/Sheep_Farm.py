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