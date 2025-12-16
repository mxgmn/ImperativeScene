set_title("Futuristic Command Center")
set_size(width=15, depth=12, height=3.5)
set_floor_asset("Metal Floor", color="2C3E50")
set_wall_asset("Metal Panel Wall", interior=True, color="34495E")

main_door = Door("Sliding Door", width=2.0, depth=0.1, height=2.2, color="7F8C8D")
side_door = Door("Sliding Door", width=1.0, depth=0.1, height=2.2, color="7F8C8D")
window = Window("Observation Window", width=6.0, depth=0.2, height=2.0, color="85C1E9")

# Main command console
main_console = Object("Command Console", width=6.0, depth=1.2, height=1.0, support=STANDING, color="3498DB")
control_chairs = [Object("Ergonomic Chair", width=0.6, depth=0.6, height=1.2, support=STANDING, color="E74C3C") for _ in range(4)]

# Side stations
monitoring_stations = [Object("Monitoring Station", width=1.2, depth=0.8, height=1.0, support=STANDING, color="27AE60") for _ in range(3)]
side_chairs = [Object("Task Chair", width=0.5, depth=0.5, height=1.0, support=STANDING, color="C0392B") for _ in range(3)]

# Wall-mounted displays
displays = [Object("Holographic Display", width=1.8, depth=0.1, height=1.0, support=MOUNTED, color="9B59B6") for _ in range(4)]

# Central hologram projector
hologram_table = Object("Hologram Table", width=2.5, depth=2.5, height=0.9, support=STANDING, color="16A085")

# Communication equipment
comm_array = Object("Communication Array", width=1.5, depth=0.4, height=1.8, support=STANDING, color="F1C40F")

# Server racks
server_racks = [Object("Server Rack", width=0.8, depth=1.0, height=2.0, support=STANDING, color="95A5A6") for _ in range(3)]

# Status boards
status_boards = [Object("Status Board", width=1.2, depth=0.1, height=0.8, support=MOUNTED, color="E67E22") for _ in range(2)]

# Emergency equipment
emergency_station = Object("Emergency Station", width=1.0, depth=0.3, height=1.5, support=MOUNTED, color="E74C3C")

# Radar equipment
radar_console = Object("Radar Console", width=1.5, depth=0.8, height=1.2, support=STANDING, color="2980B9")

main_door.center.x = scene.center.x
main_door.min.y = scene.min.y
main_door.min.z = scene.min.z
main_door.facing = Y_MAX

side_door.max.x = scene.max.x
side_door.max.y = scene.max.y - 0.2 * scene.depth
side_door.min.z = scene.min.z
side_door.facing = X_MIN

window.center.x = scene.center.x
window.max.y = scene.max.y
window.min.z = 1.0
window.facing = Y_MIN

main_console.center.x = scene.center.x
main_console.max.y = scene.max.y - 0.2 * scene.depth
main_console.min.z = scene.min.z
main_console.facing = Y_MIN

set_coordinate_frame(main_console)
for i, chair in enumerate(control_chairs):
    chair.center.x = main_console.min.x + (i+1.0) / 5.0 * main_console.width
    chair.min.y = main_console.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = main_console
set_coordinate_frame(scene)

for i, station in enumerate(monitoring_stations):
    station.min.x = scene.min.x + 0.1
    station.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    station.min.z = scene.min.z
    station.facing = X_MAX

set_coordinate_frame(monitoring_stations[0])
for i, chair in enumerate(side_chairs):
    set_coordinate_frame(monitoring_stations[i])
    chair.center.x = monitoring_stations[i].center.x
    chair.min.y = monitoring_stations[i].max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = monitoring_stations[i]
set_coordinate_frame(scene)

for i, display in enumerate(displays):
    if i < 2:
        display.min.x = scene.min.x
        display.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
        display.facing = X_MAX
    else:
        display.max.x = scene.max.x
        display.center.y = scene.min.y + (i-1.0) / 3.0 * scene.depth
        display.facing = X_MIN
    display.min.z = 1.5

hologram_table.center.x = scene.center.x
hologram_table.center.y = scene.center.y
hologram_table.min.z = scene.min.z
hologram_table.facing = Y_MIN

comm_array.max.x = scene.max.x - 0.1
comm_array.min.y = scene.min.y + 0.1
comm_array.min.z = scene.min.z
comm_array.facing = X_MIN

for i, rack in enumerate(server_racks):
    rack.max.x = scene.max.x - 0.1
    rack.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    rack.min.z = scene.min.z
    rack.facing = X_MIN

for i, board in enumerate(status_boards):
    board.center.x = scene.min.x + (i+1.0) / 3.0 * scene.width
    board.min.y = scene.min.y + 0.1
    board.min.z = 1.8
    board.facing = Y_MAX

emergency_station.min.x = scene.min.x
emergency_station.max.y = scene.max.y - 0.1
emergency_station.min.z = 1.0
emergency_station.facing = X_MAX

radar_console.max.x = scene.max.x - 0.1
radar_console.max.y = scene.max.y - 0.1
radar_console.min.z = scene.min.z
radar_console.facing = X_MIN