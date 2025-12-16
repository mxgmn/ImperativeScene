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

cell_door.max.x = scene.max.x
cell_door.center.y = scene.min.y + 0.2 * scene.depth
cell_door.min.z = scene.min.z
cell_door.facing = X_MIN

window.center.x = scene.min.x + 0.5 * scene.width
window.min.y = scene.min.y
window.min.z = 2.0
window.facing = Y_MAX

bed.min.x = scene.min.x + 0.1
bed.center.y = scene.center.y
bed.min.z = scene.min.z
bed.facing = X_MAX

toilet.max.x = scene.max.x - 0.1
toilet.max.y = scene.max.y - 0.1
toilet.min.z = scene.min.z
toilet.facing = X_MIN

sink.max.x = scene.max.x - 0.1
sink.max.y = scene.max.y - toilet.depth - 0.2
sink.min.z = 0.8
sink.facing = X_MIN

shelf.min.x = scene.min.x + 0.1
shelf.max.y = scene.max.y - 0.1
shelf.min.z = 1.5
shelf.facing = X_MAX

set_coordinate_frame(shelf)
book_spacing = 0.1
for i, book in enumerate(books):
    book.min.x = shelf.min.x + i * book_spacing
    book.center.y = shelf.center.y
    book.min.z = shelf.max.z
    book.facing = Y_MIN
set_coordinate_frame(scene)

vent.max.x = scene.max.x - 0.1
vent.center.y = scene.min.y + 0.3 * scene.depth
vent.min.z = 2.0
vent.facing = X_MIN

drain.center.x = scene.center.x
drain.center.y = scene.center.y
drain.min.z = scene.min.z
drain.facing = Y_MAX