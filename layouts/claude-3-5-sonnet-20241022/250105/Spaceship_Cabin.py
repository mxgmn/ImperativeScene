set_title("Spaceship Cabin")
set_size(width=8, depth=6, height=2.5)
set_floor_asset("Metal Floor", color="2F4F4F")
set_wall_asset("Metal Panel Wall", interior=True, color="4A5459")

sliding_door = Door("Sliding Door", width=1.2, depth=0.1, height=2.0, color="4682B4")
window = Window("Spaceship Window", width=2.0, depth=0.1, height=1.0, color="87CEEB")

# Main control station
control_panel = Object("Control Panel", width=2.4, depth=0.8, height=1.0, support=STANDING, color="FF4500")
pilot_seat = Object("Pilot Chair", width=0.8, depth=0.8, height=1.2, support=STANDING, color="4169E1")
copilot_seat = Object("Copilot Chair", width=0.8, depth=0.8, height=1.2, support=STANDING, color="4169E1")

# Living quarters
bunk_beds = [Object("Bunk Bed", width=0.9, depth=2.0, height=1.8, support=STANDING, color="708090") for _ in range(2)]
lockers = [Object("Storage Locker", width=0.6, depth=0.5, height=1.8, support=STANDING, color="20B2AA") for _ in range(3)]

# Equipment
computer_screens = [Object("Monitor Screen", width=0.6, depth=0.05, height=0.4, support=MOUNTED, color="00CED1") for _ in range(4)]
life_support = Object("Life Support Unit", width=1.0, depth=0.4, height=1.6, support=STANDING, color="32CD32")
navigation_unit = Object("Navigation Unit", width=0.8, depth=0.4, height=0.6, support=STANDING, color="FFD700")
medical_station = Object("Medical Station", width=1.2, depth=0.5, height=1.4, support=STANDING, color="FF6B6B")
storage_containers = [Object("Storage Container", width=0.4, depth=0.4, height=0.4, support=STANDING, color="CD853F") for _ in range(3)]

# Wall-mounted equipment
status_displays = [Object("Status Display", width=0.8, depth=0.05, height=0.5, support=MOUNTED, color="7B68EE") for _ in range(2)]
emergency_kit = Object("Emergency Kit", width=0.5, depth=0.2, height=0.5, support=MOUNTED, color="DC143C")

sliding_door.max.x = scene.max.x
sliding_door.center.y = scene.min.y + 0.2 * scene.depth
sliding_door.min.z = scene.min.z
sliding_door.facing = X_MIN

window.center.x = scene.center.x
window.min.y = scene.min.y
window.min.z = 1.2
window.facing = Y_MAX

control_panel.center.x = window.center.x
control_panel.min.y = window.max.y + 0.3
control_panel.min.z = scene.min.z
control_panel.facing = Y_MIN

set_coordinate_frame(control_panel)
pilot_seat.center.x = control_panel.center.x - 0.5
pilot_seat.min.y = control_panel.max.y + 0.2
pilot_seat.min.z = scene.min.z
pilot_seat.facing = control_panel

copilot_seat.center.x = control_panel.center.x + 0.5
copilot_seat.min.y = control_panel.max.y + 0.2
copilot_seat.min.z = scene.min.z
copilot_seat.facing = control_panel
set_coordinate_frame(scene)

for i, bunk in enumerate(bunk_beds):
    bunk.min.x = scene.min.x + i * (bunk.width + 0.3)
    bunk.max.y = scene.max.y
    bunk.min.z = scene.min.z
    bunk.facing = Y_MIN

for i, locker in enumerate(lockers):
    locker.max.x = scene.max.x
    locker.center.y = scene.min.y + (i + 1.0) * scene.depth / 4.0
    locker.min.z = scene.min.z
    locker.facing = X_MIN

set_coordinate_frame(control_panel)
for i, screen in enumerate(computer_screens):
    screen.center.x = control_panel.min.x + (i + 1.0) * control_panel.width / 5.0
    screen.min.y = control_panel.min.y
    screen.min.z = control_panel.max.z + 0.1
    screen.facing = control_panel.facing
set_coordinate_frame(scene)

life_support.min.x = scene.min.x
life_support.min.y = scene.min.y + 0.2
life_support.min.z = scene.min.z
life_support.facing = X_MAX

navigation_unit.min.x = life_support.max.x + 0.2
navigation_unit.min.y = scene.min.y + 0.2
navigation_unit.min.z = scene.min.z
navigation_unit.facing = X_MAX

medical_station.max.x = scene.max.x
medical_station.max.y = scene.max.y
medical_station.min.z = scene.min.z
medical_station.facing = X_MIN

for i, container in enumerate(storage_containers):
    container.min.x = scene.min.x
    container.center.y = scene.min.y + (i + 1.0) * scene.depth / 4.0
    container.min.z = scene.min.z
    container.facing = X_MAX

for i, display in enumerate(status_displays):
    display.center.x = scene.min.x + (i + 1.0) * scene.width / 3.0
    display.max.y = scene.max.y
    display.min.z = 1.8
    display.facing = Y_MIN

emergency_kit.max.x = scene.max.x
emergency_kit.center.y = scene.center.y
emergency_kit.min.z = 1.5
emergency_kit.facing = X_MIN