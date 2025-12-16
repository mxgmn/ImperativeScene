set_title("Two-Car Garage")
set_size(width=6.5, depth=7.0, height=2.8)
set_floor_asset("Concrete Floor", color="8E8E8E")
set_wall_asset("Painted Wall", interior=True, color="E0DCD3")

# Two garage doors on the front
gate1 = Door("Garage Gate", width=2.8, depth=0.15, height=2.2, color="A9A9A9")
gate2 = Door("Garage Gate", width=2.8, depth=0.15, height=2.2, color="A9A9A9")
side_door = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="708090")

# Two cars
car1 = Object("SUV", width=1.9, depth=4.8, height=1.6, support=STANDING, color="4682B4")
car2 = Object("Sedan", width=1.8, depth=4.5, height=1.4, support=STANDING, color="CD5C5C")

# Storage and work areas
workbench = Object("Workbench", width=2.0, depth=0.6, height=0.9, support=STANDING, color="8B4513")
tool_cabinet = Object("Tool Cabinet", width=1.2, depth=0.5, height=1.8, support=STANDING, color="2F4F4F")
storage_shelves = [Object("Storage Shelf", width=1.8, depth=0.6, height=2.0, support=STANDING, color="696969") for _ in range(2)]

# Wall-mounted storage
wall_rack = Object("Wall Storage Rack", width=2.4, depth=0.3, height=0.6, support=MOUNTED, color="B8860B")
bike_hooks = [Object("Bike Hook", width=0.3, depth=0.2, height=0.2, support=MOUNTED, color="CD853F") for _ in range(2)]

# Equipment
lawn_mower = Object("Lawn Mower", width=0.6, depth=1.2, height=1.0, support=STANDING, color="32CD32")
garbage_bins = [Object("Garbage Bin", width=0.5, depth=0.5, height=0.9, support=STANDING, color="2E8B57") for _ in range(2)]
toolbox = Object("Large Toolbox", width=0.6, depth=0.3, height=0.4, support=STANDING, color="B22222")

# Position the garage doors
gate1.center.x = scene.min.x + 0.3 * scene.width
gate1.min.y = scene.min.y
gate1.min.z = scene.min.z
gate1.facing = Y_MAX

gate2.center.x = scene.min.x + 0.7 * scene.width
gate2.min.y = scene.min.y
gate2.min.z = scene.min.z
gate2.facing = Y_MAX

side_door.max.x = scene.max.x
side_door.center.y = scene.min.y + 0.2 * scene.depth
side_door.min.z = scene.min.z
side_door.facing = X_MIN

# Position cars
car1.center.x = gate1.center.x
car1.center.y = scene.center.y
car1.min.z = scene.min.z
car1.facing = gate1

car2.center.x = gate2.center.x
car2.center.y = scene.center.y
car2.min.z = scene.min.z
car2.facing = gate2

# Work area
workbench.min.x = scene.min.x
workbench.max.y = scene.max.y
workbench.min.z = scene.min.z
workbench.facing = Y_MIN

tool_cabinet.min.x = workbench.max.x + 0.1
tool_cabinet.max.y = scene.max.y
tool_cabinet.min.z = scene.min.z
tool_cabinet.facing = Y_MIN

# Storage shelves along the right wall
for i, shelf in enumerate(storage_shelves):
    shelf.max.x = scene.max.x
    shelf.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    shelf.min.z = scene.min.z
    shelf.facing = X_MIN

# Wall-mounted storage
wall_rack.max.x = scene.max.x - 0.1
wall_rack.center.y = scene.center.y
wall_rack.min.z = 1.8
wall_rack.facing = X_MIN

# Bike hooks
for i, hook in enumerate(bike_hooks):
    hook.min.x = scene.min.x
    hook.center.y = scene.min.y + (i+1.0) / 3.0 * scene.depth
    hook.min.z = 1.6
    hook.facing = X_MAX

# Equipment
lawn_mower.max.x = scene.max.x - 0.1
lawn_mower.min.y = scene.min.y + 0.1
lawn_mower.min.z = scene.min.z
lawn_mower.facing = X_MIN

set_coordinate_frame(workbench)
toolbox.center.x = workbench.center.x
toolbox.center.y = workbench.center.y
toolbox.min.z = workbench.max.z
toolbox.facing = workbench.facing
set_coordinate_frame(scene)

# Garbage bins
for i, bin in enumerate(garbage_bins):
    bin.max.x = scene.max.x - 0.1
    bin.center.y = scene.max.y - (i+0.5) * bin.depth
    bin.min.z = scene.min.z
    bin.facing = X_MIN