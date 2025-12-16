set_title("Bathroom with Bathtub")
set_size(width=3.5, depth=2.8, height=2.4)
set_floor_asset("Ceramic Tile Floor", color="E5E5E5")
set_wall_asset("Ceramic Tile Wall", interior=True, color="F0F0F0")

door = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="A0522D")
window = Window("Frosted Window", width=0.8, depth=0.1, height=1.0, color="E6F3FF")

# Main fixtures
bathtub = Object("Bathtub", width=1.7, depth=0.8, height=0.6, support=STANDING, color="FFFFFF")
toilet = Object("Toilet", width=0.4, depth=0.65, height=0.4, support=STANDING, color="FFFFFF")
sink = Object("Bathroom Sink", width=0.6, depth=0.45, height=0.15, support=STANDING, color="FFFFFF")
vanity = Object("Vanity Cabinet", width=0.6, depth=0.45, height=0.8, support=STANDING, color="87CEEB")

# Storage and accessories
mirror = Object("Wall Mirror", width=0.6, depth=0.05, height=0.8, support=MOUNTED, color="B0E0E6")
towel_rack = Object("Towel Rack", width=0.6, depth=0.1, height=0.1, support=MOUNTED, color="C0C0C0")
toilet_paper_holder = Object("Toilet Paper Holder", width=0.15, depth=0.1, height=0.15, support=MOUNTED, color="C0C0C0")
storage_cabinet = Object("Wall Cabinet", width=0.4, depth=0.25, height=0.6, support=MOUNTED, color="87CEEB")

# Decorative elements
plant = Object("Indoor Plant", width=0.3, depth=0.3, height=0.4, support=STANDING, color="228B22")
bath_mat = Object("Bath Mat", width=0.9, depth=0.6, height=0.02, support=STANDING, color="4682B4")
soap_dispenser = Object("Soap Dispenser", width=0.1, depth=0.1, height=0.2, support=STANDING, color="FF69B4")