set_title("Astronomy Observatory")
set_size(width=10, depth=10, height=4)
set_floor_asset("Concrete Floor", color="4A4A4A")
set_wall_asset("Metal Panel Wall", interior=True, color="2F4F4F")

entrance = Door("Metal Door", width=1.0, depth=0.1, height=2.0, color="708090")
emergency_exit = Door("Metal Door", width=0.8, depth=0.1, height=2.0, color="708090")
windows = [Window("Observatory Window", width=1.5, depth=0.1, height=1.2, color="4682B4") for _ in range(4)]

telescope = Object("Large Telescope", width=2.0, depth=4.0, height=3.0, support=STANDING, color="4169E1")
computer_desk = Object("Computer Desk", width=2.4, depth=0.8, height=0.75, support=STANDING, color="8B4513")
computers = [Object("Computer Monitor", width=0.5, depth=0.2, height=0.3, support=STANDING, color="1E90FF") for _ in range(3)]
office_chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="483D8B") for _ in range(3)]

control_panel = Object("Control Panel", width=2.5, depth=0.6, height=1.0, support=STANDING, color="20B2AA")
equipment_rack = Object("Equipment Rack", width=1.0, depth=0.8, height=2.0, support=STANDING, color="CD853F")
storage_cabinet = Object("Storage Cabinet", width=1.2, depth=0.6, height=1.8, support=STANDING, color="B8860B")

star_charts = [Object("Star Chart", width=1.2, depth=0.05, height=0.9, support=MOUNTED, color="4682B4") for _ in range(3)]
planet_models = [Object("Planet Model", width=0.3, depth=0.3, height=0.3, support=STANDING, color="FF4500") for _ in range(4)]
workbench = Object("Workbench", width=2.0, depth=0.8, height=0.9, support=STANDING, color="8B4513")