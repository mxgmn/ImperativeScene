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

entrance.max.x = scene.max.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

window.center.x = scene.min.x + 0.5 * scene.width
window.min.y = scene.min.y
window.min.z = 0.8
window.facing = Y_MAX

for i, station in enumerate(styling_stations):
    station.min.x = scene.min.x + (i+0.5) / 4.0 * scene.width
    station.max.y = scene.max.y
    station.min.z = scene.min.z
    station.facing = Y_MIN

    mirrors[i].center.x = station.center.x
    mirrors[i].min.y = station.min.y
    mirrors[i].min.z = 1.0
    mirrors[i].facing = Y_MIN

    set_coordinate_frame(station)
    salon_chairs[i].center.x = station.center.x
    salon_chairs[i].center.y = station.center.y + 0.1
    salon_chairs[i].min.z = scene.min.z
    salon_chairs[i].facing = station
    set_coordinate_frame(scene)

reception_desk.max.x = scene.max.x - 0.2
reception_desk.min.y = scene.min.y + 0.2
reception_desk.min.z = scene.min.z
reception_desk.facing = X_MIN

for i, chair in enumerate(waiting_chairs):
    chair.min.x = scene.min.x + (i+0.5) / 4.0 * scene.width
    chair.min.y = scene.min.y + 0.3
    chair.min.z = scene.min.z
    chair.facing = Y_MAX

for i, shelf in enumerate(product_shelves):
    shelf.min.x = scene.min.x + i * (shelf.width + 0.2)
    shelf.min.y = scene.min.y + 0.2
    shelf.min.z = scene.min.z
    shelf.facing = X_MAX

washing_station.min.x = scene.min.x + 0.2
washing_station.center.y = scene.center.y
washing_station.min.z = scene.min.z
washing_station.facing = X_MAX

storage_cabinet.max.x = scene.max.x - 0.2
storage_cabinet.max.y = scene.max.y - 0.2
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MIN

plants[0].min.x = scene.min.x + 0.2
plants[0].max.y = scene.max.y - 0.2
plants[0].min.z = scene.min.z
plants[0].facing = Y_MIN

plants[1].max.x = scene.max.x - 0.2
plants[1].min.y = scene.min.y + 0.2
plants[1].min.z = scene.min.z
plants[1].facing = X_MIN

magazine_rack.min.x = scene.min.x + 0.3
magazine_rack.min.y = scene.min.y + 0.3
magazine_rack.min.z = scene.min.z
magazine_rack.facing = X_MAX