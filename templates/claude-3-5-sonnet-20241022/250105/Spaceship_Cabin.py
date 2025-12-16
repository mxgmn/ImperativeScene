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