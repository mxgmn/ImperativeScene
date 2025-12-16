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