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