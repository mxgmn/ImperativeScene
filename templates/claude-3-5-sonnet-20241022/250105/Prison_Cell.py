set_title("Prison Cell")
set_size(width=2.5, depth=3.0, height=2.5)
set_floor_asset("Concrete Floor", color="696969")
set_wall_asset("Concrete Wall", interior=True, color="808080")

cell_door = Door("Prison Door", width=0.8, depth=0.1, height=2.0, color="4A4A4A")
window = Window("Barred Window", width=0.6, depth=0.1, height=0.4, color="A9A9A9")

bed = Object("Prison Bed", width=0.8, depth=2.0, height=0.4, support=STANDING, color="8B4513")
toilet = Object("Metal Toilet", width=0.4, depth=0.5, height=0.4, support=STANDING, color="C0C0C0")
sink = Object("Metal Sink", width=0.4, depth=0.3, height=0.15, support=MOUNTED, color="B8B8B8")
shelf = Object("Metal Shelf", width=0.6, depth=0.3, height=0.05, support=MOUNTED, color="A9A9A9")
books = [Object("Book", width=0.03, depth=0.2, height=0.3, support=STANDING, color=color) for color in ["FF5733","4CAF50","2196F3","FFC107","9C27B0","E91E63"]]
vent = Object("Air Vent", width=0.3, depth=0.05, height=0.3, support=MOUNTED, color="787878")
drain = Object("Floor Drain", width=0.2, depth=0.2, height=0.02, support=STANDING, color="505050")