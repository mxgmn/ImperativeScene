set_title("Garage")
set_size(width=4.5, depth=6.5, height=2.5)
set_floor_asset("Concrete Floor")
set_wall_asset("Brick Wall", interior=True)

gate = Door("Garage Gate", width=2.5, depth=0.15, height=2.2)
car = Object("Car", width=1.9, depth=4.5, height=1.4, support=STANDING, dynamic=True)
workbench = Object("Workbench", width=2.2, depth=0.4, height=0.8, support=STANDING, dynamic=False)
vise = Object("Vise", width=0.2, depth=0.3, height=0.2, support=STANDING, dynamic=True)
hammer = Object("Hammer", width=0.1, depth=0.2, height=0.05, support=STANDING, dynamic=True)
toolbox = Object("Toolbox", width=0.4, depth=0.3, height=0.5, support=STANDING, dynamic=True)
shelving_unit = Object("Shelving Unit", width=1.5, depth=0.4, height=1.8, support=STANDING, dynamic=False)
boxes = [Object("Storage Box", width=0.3, depth=0.25, height=0.2, support=STANDING, dynamic=True) for _ in range(4)]
bicycle = Object("Bicycle", width=0.4, depth=1.8, height=1.0, support=STANDING, dynamic=True)
ladder = Object("Ladder", width=0.5, depth=0.4, height=2.0, support=STANDING, dynamic=False)
tire_rack = Object("Tire Rack", width=2.4, depth=0.6, height=0.5, support=MOUNTED, dynamic=False)
tires = [Object("Tire", 0.6, 0.6, height=0.25, support=STANDING, dynamic=True) for _ in range(4)]
washer = Object("Pressure Washer", 0.6, 0.6, height=0.8, support=STANDING, dynamic=True)

gate.center.x = scene.center.x
gate.min.y = scene.min.y
gate.min.z = scene.min.z
gate.facing = Y_MAX

car.center.x = gate.center.x
car.center.y = scene.center.y
car.min.z = scene.min.z
car.facing = gate

workbench.min.x = scene.min.x
workbench.center.y = scene.center.y - 1.0
workbench.min.z = scene.min.z
workbench.facing = X_MAX

set_coordinate_frame(workbench)
vise.center.x = workbench.min.x + 0.25 * workbench.width
vise.center.y = workbench.center.y
vise.min.z = workbench.max.z
vise.facing = workbench.facing
hammer.center.x = workbench.min.x + 0.75 * workbench.width
hammer.center.y = workbench.center.y
hammer.min.z = workbench.max.z
hammer.facing = workbench.facing
set_coordinate_frame(scene)

toolbox.min.x = scene.min.x
toolbox.max.y = workbench.min.y
toolbox.min.z = scene.min.z
toolbox.facing = X_MAX

shelving_unit.center.x = scene.min.x + 0.5 * scene.width
shelving_unit.max.y = scene.max.y
shelving_unit.min.z = scene.min.z
shelving_unit.facing = Y_MIN

set_coordinate_frame(shelving_unit)
for i, box in enumerate(boxes):
    box.center.x = shelving_unit.min.x + (i+0.5) / 4.0 * shelving_unit.width
    box.center.y = shelving_unit.center.y
    box.min.z = shelving_unit.max.z
    box.facing = shelving_unit.facing
set_coordinate_frame(scene)

bicycle.max.x = scene.max.x
bicycle.center.y = scene.min.y + 0.5 * scene.depth
bicycle.min.z = scene.min.z
bicycle.facing = car.facing

ladder.max.x = scene.max.x
ladder.center.y = scene.min.y + 0.25 * scene.depth
ladder.min.z = scene.min.z
ladder.facing = X_MIN

tire_rack.min.x = scene.min.x
tire_rack.min.y = workbench.max.y + 0.5
tire_rack.min.z = 0.5
tire_rack.facing = X_MAX

set_coordinate_frame(tire_rack)
for i, tire in enumerate(tires):
    tire.center.x = tire_rack.min.x + (i+0.5) / 4.0 * tire_rack.width
    tire.center.y = tire_rack.center.y
    tire.min.z = tire_rack.max.z
    tire.facing = tire_rack.facing
set_coordinate_frame(scene)

washer.max.x = scene.max.x
washer.center.y = scene.min.y + 0.75 * scene.depth
washer.min.z = scene.min.z
washer.facing = X_MIN