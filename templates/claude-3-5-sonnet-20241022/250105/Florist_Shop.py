set_title("Florist Shop")
set_size(width=8, depth=6, height=3)
set_floor_asset("Wooden Floor", color="9B8579")
set_wall_asset("Painted Wall", interior=True, color="E6E6FA")

entrance_door = Door("Glass Door", width=1.0, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="8B4513")
window = Window("Display Window", width=3.0, depth=0.1, height=2.0, color="B0E0E6")

# Main display and storage furniture
counter = Object("Shop Counter", width=2.0, depth=0.6, height=1.0, support=STANDING, color="E9967A")
register = Object("Cash Register", width=0.3, depth=0.3, height=0.25, support=STANDING, color="708090")
display_shelves = [Object("Display Shelf", width=1.8, depth=0.4, height=1.8, support=STANDING, color="DEB887") for _ in range(3)]
window_display = Object("Display Table", width=2.8, depth=0.6, height=0.8, support=STANDING, color="B8860B")

# Plants and flowers (represented as solid objects)
potted_plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=0.8, support=STANDING, color="228B22") for _ in range(6)]
flower_buckets = [Object("Flower Bucket", width=0.3, depth=0.3, height=0.5, support=STANDING, color="FF69B4") for _ in range(8)]
large_plants = [Object("Large Plant", width=0.6, depth=0.6, height=1.6, support=STANDING, color="006400") for _ in range(2)]

# Storage and supplies
storage_cabinet = Object("Storage Cabinet", width=1.2, depth=0.5, height=1.8, support=STANDING, color="8FBC8F")
work_table = Object("Work Table", width=1.5, depth=0.8, height=0.9, support=STANDING, color="CD853F")
supply_shelf = Object("Wall Shelf", width=1.6, depth=0.3, height=0.05, support=MOUNTED, color="A0522D")
vase_display = [Object("Decorative Vase", width=0.2, depth=0.2, height=0.3, support=STANDING, color="4682B4") for _ in range(5)]