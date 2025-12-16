set_title("Hair Salon")
set_size(width=8, depth=6, height=3)
set_floor_asset("Tile Floor", color="E6E6E6")
set_wall_asset("Modern Wall", interior=True, color="F0F0F0")

entrance = Door("Glass Door", width=0.9, depth=0.1, height=2.1, color="87CEEB")
window = Window("Store Window", width=3.0, depth=0.1, height=2.0, color="ADD8E6")

styling_stations = [Object("Styling Station", width=1.2, depth=0.5, height=0.8, support=STANDING, color="FF69B4") for _ in range(3)]
salon_chairs = [Object("Salon Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="FF1493") for _ in range(3)]
mirrors = [Object("Mirror", width=1.2, depth=0.05, height=1.4, support=MOUNTED, color="B0E0E6") for _ in range(3)]

reception_desk = Object("Reception Counter", width=1.8, depth=0.6, height=1.1, support=STANDING, color="9370DB")
waiting_chairs = [Object("Modern Chair", width=0.5, depth=0.5, height=0.8, support=STANDING, color="4682B4") for _ in range(3)]
product_shelves = [Object("Display Shelf", width=1.2, depth=0.3, height=1.8, support=STANDING, color="DDA0DD") for _ in range(2)]
washing_station = Object("Hair Wash Station", width=1.8, depth=0.8, height=1.0, support=STANDING, color="20B2AA")
storage_cabinet = Object("Storage Cabinet", width=1.0, depth=0.4, height=1.6, support=STANDING, color="778899")
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=0.8, support=STANDING, color="32CD32") for _ in range(2)]
magazine_rack = Object("Magazine Rack", width=0.4, depth=0.2, height=0.6, support=STANDING, color="FF8C00")