set_title("Garage")
set_size(width=4.5, depth=6.5, height=2.5)
set_floor_asset("Concrete Floor", color="8E8E8E")
set_wall_asset("Brick Wall", interior=True, color="8C4F3B")

gate = Door("Garage Gate", width=2.5, depth=0.15, height=2.2, color="A9A9A9")

car = Object("Car", width=1.9, depth=4.5, height=1.4, support=STANDING, color="2E8B57")
workbench = Object("Workbench", width=2.2, depth=0.4, height=0.8, support=STANDING, color="8B4513")
vise = Object("Vise", width=0.2, depth=0.3, height=0.2, support=STANDING, color="4682B4")
hammer = Object("Hammer", width=0.1, depth=0.2, height=0.05, support=STANDING, color="CD5C5C")
toolbox = Object("Toolbox", width=0.4, depth=0.3, height=0.5, support=STANDING, color="FF4500")
shelving_unit = Object("Shelving Unit", width=1.5, depth=0.4, height=1.8, support=STANDING, color="556B2F")
boxes = [Object("Storage Box", width=0.3, depth=0.25, height=0.2, support=STANDING, color="FFD700") for _ in range(4)]
bicycle = Object("Bicycle", width=0.4, depth=1.8, height=1.0, support=STANDING, color="4169E1")
ladder = Object("Ladder", width=0.5, depth=0.4, height=2.0, support=STANDING, color="DAA520")
tire_rack = Object("Tire Rack", width=2.4, depth=0.6, height=0.5, support=MOUNTED, color="808080")
tires = [Object("Tire", 0.6, 0.6, height=0.25, support=STANDING, color="333333") for _ in range(4)]
washer = Object("Pressure Washer", 0.6, 0.6, height=0.8, support=STANDING, color="32CD32")