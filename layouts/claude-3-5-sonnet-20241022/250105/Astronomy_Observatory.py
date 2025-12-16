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

entrance.min.x = scene.min.x + 0.2 * scene.width
entrance.min.y = scene.min.y
entrance.min.z = scene.min.z
entrance.facing = Y_MAX

emergency_exit.max.x = scene.max.x
emergency_exit.max.y = scene.max.y - 0.2 * scene.depth
emergency_exit.min.z = scene.min.z
emergency_exit.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 5.0 * scene.width
    window.max.y = scene.max.y
    window.min.z = 1.0
    window.facing = Y_MIN

telescope.center.x = scene.center.x
telescope.center.y = scene.center.y
telescope.min.z = scene.min.z
telescope.facing = Y_MAX

computer_desk.min.x = scene.min.x + 0.1
computer_desk.min.y = scene.min.y + 0.2
computer_desk.min.z = scene.min.z
computer_desk.facing = X_MAX

set_coordinate_frame(computer_desk)
for i, computer in enumerate(computers):
    computer.center.x = computer_desk.min.x + (i+1.0) / 4.0 * computer_desk.width
    computer.center.y = computer_desk.center.y
    computer.min.z = computer_desk.max.z
    computer.facing = computer_desk.facing

for i, chair in enumerate(office_chairs):
    chair.center.x = computer_desk.min.x + (i+1.0) / 4.0 * computer_desk.width
    chair.min.y = computer_desk.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = computer_desk
set_coordinate_frame(scene)

control_panel.max.x = scene.max.x - 0.1
control_panel.min.y = scene.min.y + 0.2
control_panel.min.z = scene.min.z
control_panel.facing = X_MIN

equipment_rack.max.x = scene.max.x - 0.1
equipment_rack.center.y = scene.center.y
equipment_rack.min.z = scene.min.z
equipment_rack.facing = X_MIN

storage_cabinet.max.x = scene.max.x - 0.1
storage_cabinet.max.y = scene.max.y - 0.2
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MIN

for i, chart in enumerate(star_charts):
    chart.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    chart.min.y = scene.min.y
    chart.min.z = 1.5
    chart.facing = Y_MAX

workbench.min.x = scene.min.x + 0.1
workbench.max.y = scene.max.y - 0.2
workbench.min.z = scene.min.z
workbench.facing = X_MAX

set_coordinate_frame(workbench)
for i, model in enumerate(planet_models):
    model.center.x = workbench.min.x + (i+1.0) / 5.0 * workbench.width
    model.center.y = workbench.center.y
    model.min.z = workbench.max.z
    model.facing = workbench.facing
set_coordinate_frame(scene)