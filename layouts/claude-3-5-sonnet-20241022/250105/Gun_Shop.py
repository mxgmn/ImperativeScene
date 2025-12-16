set_title("Gun Shop")
set_size(width=8, depth=10, height=3)
set_floor_asset("Hardwood Floor", color="8B7355")
set_wall_asset("Painted Wall", interior=True, color="E8E5DC")

entrance = Door("Security Door", width=1.0, depth=0.1, height=2.2, color="4A4A4A")
back_door = Door("Metal Door", width=0.8, depth=0.1, height=2.0, color="708090")
windows = [Window("Security Window", width=1.5, depth=0.1, height=1.5, color="87CEEB") for _ in range(2)]

display_cases = [Object("Glass Display Case", width=1.8, depth=0.6, height=1.0, support=STANDING, color="B0C4DE") for _ in range(3)]
counter = Object("Counter", width=2.5, depth=0.6, height=1.1, support=STANDING, color="8B4513")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.3, support=STANDING, color="696969")

wall_racks = [Object("Gun Rack", width=2.0, depth=0.2, height=1.5, support=MOUNTED, color="A0522D") for _ in range(4)]
ammo_shelves = [Object("Storage Shelf", width=1.2, depth=0.4, height=2.0, support=STANDING, color="8B7355") for _ in range(2)]
gun_safe = Object("Gun Safe", width=1.2, depth=0.6, height=2.0, support=STANDING, color="2F4F4F")

security_camera = Object("Security Camera", width=0.2, depth=0.2, height=0.2, support=MOUNTED, color="4682B4")
target_posters = [Object("Target Poster", width=0.6, depth=0.02, height=0.8, support=MOUNTED, color="CD5C5C") for _ in range(3)]
warning_sign = Object("Warning Sign", width=0.4, depth=0.02, height=0.3, support=MOUNTED, color="FF4500")

chairs = [Object("Office Chair", width=0.5, depth=0.5, height=1.0, support=STANDING, color="000080") for _ in range(2)]
filing_cabinet = Object("Filing Cabinet", width=0.5, depth=0.6, height=1.3, support=STANDING, color="778899")

entrance.max.x = scene.max.x
entrance.center.y = scene.min.y + 0.2 * scene.depth
entrance.min.z = scene.min.z
entrance.facing = X_MIN

back_door.min.x = scene.min.x + 0.2 * scene.width
back_door.max.y = scene.max.y
back_door.min.z = scene.min.z
back_door.facing = Y_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 0.8
    window.facing = Y_MAX

for i, case in enumerate(display_cases):
    case.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    case.center.y = scene.center.y
    case.min.z = scene.min.z
    case.facing = Y_MAX

counter.max.x = scene.max.x - 0.2
counter.max.y = scene.max.y - 0.2
counter.min.z = scene.min.z
counter.facing = Y_MIN

set_coordinate_frame(counter)
register.center.x = counter.min.x + 0.25 * counter.width
register.center.y = counter.center.y
register.min.z = counter.max.z
register.facing = counter.facing
set_coordinate_frame(scene)

for i, rack in enumerate(wall_racks):
    if i < 2:
        rack.min.x = scene.min.x
        rack.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
        rack.facing = X_MAX
    else:
        rack.max.x = scene.max.x
        rack.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
        rack.facing = X_MIN
    rack.min.z = 1.0

for i, shelf in enumerate(ammo_shelves):
    shelf.min.x = scene.min.x + 0.2
    shelf.center.y = scene.max.y - (i+1.0) / 3.0 * scene.depth
    shelf.min.z = scene.min.z
    shelf.facing = X_MAX

gun_safe.min.x = scene.min.x + 0.2
gun_safe.max.y = scene.max.y - 0.2
gun_safe.min.z = scene.min.z
gun_safe.facing = X_MAX

security_camera.max.x = scene.max.x - 0.2
security_camera.min.y = scene.min.y + 0.2
security_camera.max.z = scene.max.z
security_camera.facing = Y_MAX

for i, poster in enumerate(target_posters):
    poster.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    poster.max.y = scene.max.y
    poster.min.z = 1.5
    poster.facing = Y_MIN

warning_sign.max.x = entrance.max.x
warning_sign.center.y = entrance.center.y
warning_sign.min.z = 1.8
warning_sign.facing = X_MIN

set_coordinate_frame(counter)
for i, chair in enumerate(chairs):
    chair.center.x = counter.min.x + (i+1.0) / 3.0 * counter.width
    chair.min.y = counter.min.y - 0.2
    chair.min.z = scene.min.z
    chair.facing = counter
set_coordinate_frame(scene)

filing_cabinet.max.x = counter.max.x
filing_cabinet.min.y = counter.min.y
filing_cabinet.min.z = scene.min.z
filing_cabinet.facing = X_MIN