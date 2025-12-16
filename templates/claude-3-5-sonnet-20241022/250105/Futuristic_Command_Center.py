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