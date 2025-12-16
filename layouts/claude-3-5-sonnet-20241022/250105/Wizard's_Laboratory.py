set_title("Wizard's Laboratory")
set_size(width=5, depth=7, height=3.5)
set_floor_asset("Stone Floor", color="4A4A4A")
set_wall_asset("Stone Wall", interior=True, color="695E53")

door = Door("Heavy Wooden Door", width=1.0, depth=0.15, height=2.2, color="8B4513")
window = Window("Arched Window", width=1.2, depth=0.2, height=1.8, color="87CEEB")

# Main furniture
workbench = Object("Alchemy Table", width=2.4, depth=0.8, height=0.9, support=STANDING, color="8B4513")
bookshelf = Object("Ornate Bookshelf", width=2.0, depth=0.4, height=2.0, support=STANDING, color="A0522D")
cabinet = Object("Potion Cabinet", width=1.6, depth=0.5, height=1.8, support=STANDING, color="4B0082")
desk = Object("Writing Desk", width=1.4, depth=0.7, height=0.8, support=STANDING, color="CD853F")
chair = Object("Wooden Chair", width=0.5, depth=0.5, height=1.0, support=STANDING, color="8B4513")

# Laboratory equipment
cauldron = Object("Cauldron", width=0.8, depth=0.8, height=0.7, support=STANDING, color="454545")
crystal_ball = Object("Crystal Ball", width=0.3, depth=0.3, height=0.3, support=STANDING, color="E6E6FA")
telescope = Object("Telescope", width=0.4, depth=1.2, height=1.5, support=STANDING, color="B8860B")

# Decorative elements
potions = [Object("Potion Bottle", width=0.15, depth=0.15, height=0.25, support=STANDING, color=color) for color in ["FF69B4", "7B68EE", "00FF7F", "FFD700"]]
books = [Object("Spell Book", width=0.3, depth=0.2, height=0.4, support=STANDING, color="800000") for _ in range(3)]
globe = Object("Magical Globe", width=0.4, depth=0.4, height=0.6, support=STANDING, color="4682B4")
skull = Object("Crystal Skull", width=0.2, depth=0.3, height=0.2, support=STANDING, color="E0FFFF")
tapestry = Object("Magical Tapestry", width=2.0, depth=0.05, height=2.0, support=MOUNTED, color="9370DB")

door.max.x = scene.max.x - 0.2 * scene.width
door.min.y = scene.min.y
door.min.z = scene.min.z
door.facing = Y_MAX

window.min.x = scene.min.x
window.center.y = scene.min.y + 0.3 * scene.depth
window.min.z = 1.0
window.facing = X_MAX

workbench.center.x = scene.center.x
workbench.max.y = scene.max.y - 0.3
workbench.min.z = scene.min.z
workbench.facing = Y_MIN

set_coordinate_frame(workbench)
cauldron.center.x = workbench.center.x
cauldron.min.y = workbench.max.y + 0.2
cauldron.min.z = scene.min.z
cauldron.facing = workbench.facing

for i, potion in enumerate(potions):
    potion.center.x = workbench.min.x + (i+1.0) / 5.0 * workbench.width
    potion.center.y = workbench.center.y
    potion.min.z = workbench.max.z
    potion.facing = workbench.facing
set_coordinate_frame(scene)

bookshelf.min.x = scene.min.x
bookshelf.center.y = scene.min.y + 0.3 * scene.depth
bookshelf.min.z = scene.min.z
bookshelf.facing = X_MAX

set_coordinate_frame(bookshelf)
for i, book in enumerate(books):
    book.center.x = bookshelf.min.x + (i+1.0) / 4.0 * bookshelf.width
    book.center.y = bookshelf.center.y
    book.min.z = bookshelf.min.z + 0.3 * bookshelf.height
    book.facing = bookshelf.facing
set_coordinate_frame(scene)

cabinet.max.x = scene.max.x
cabinet.min.y = scene.min.y + 0.1
cabinet.min.z = scene.min.z
cabinet.facing = X_MIN

desk.max.x = scene.max.x
desk.center.y = scene.min.y + 0.6 * scene.depth
desk.min.z = scene.min.z
desk.facing = X_MIN

set_coordinate_frame(desk)
chair.center.x = desk.center.x
chair.min.y = desk.max.y + 0.1
chair.min.z = scene.min.z
chair.facing = desk

crystal_ball.center.x = desk.center.x
crystal_ball.center.y = desk.center.y
crystal_ball.min.z = desk.max.z
crystal_ball.facing = desk.facing

skull.max.x = desk.max.x - 0.1
skull.min.y = desk.min.y + 0.1
skull.min.z = desk.max.z
skull.facing = desk.facing
set_coordinate_frame(scene)

telescope.min.x = scene.min.x + 0.1
telescope.min.y = scene.min.y + 0.1
telescope.min.z = scene.min.z
telescope.facing = window

globe.max.x = scene.max.x - 0.1
globe.max.y = scene.max.y - 0.1
globe.min.z = scene.min.z
globe.facing = X_MIN

tapestry.center.x = scene.center.x
tapestry.max.y = scene.max.y
tapestry.min.z = 1.2
tapestry.facing = Y_MIN