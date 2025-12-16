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

door.max.x = scene.max.x - 0.2 * scene.width
door.min.y = scene.min.y
door.min.z = scene.min.z
door.facing = Y_MAX

window.center.x = scene.min.x + 0.5 * scene.width
window.max.y = scene.max.y
window.min.z = 1.2
window.facing = Y_MIN

bathtub.min.x = scene.min.x
bathtub.max.y = scene.max.y
bathtub.min.z = scene.min.z
bathtub.facing = X_MAX

toilet.max.x = scene.max.x
toilet.min.y = scene.min.y + 0.1
toilet.min.z = scene.min.z
toilet.facing = Y_MAX

vanity.min.x = scene.min.x
vanity.min.y = scene.min.y + 0.1
vanity.min.z = scene.min.z
vanity.facing = X_MAX

set_coordinate_frame(vanity)
sink.center.x = vanity.center.x
sink.center.y = vanity.center.y
sink.min.z = vanity.max.z
sink.facing = vanity.facing

mirror.center.x = vanity.center.x
mirror.min.y = vanity.min.y
mirror.min.z = vanity.max.z + 0.1
mirror.facing = vanity.facing

soap_dispenser.min.x = sink.min.x + 0.1
soap_dispenser.min.y = sink.min.y + 0.1
soap_dispenser.min.z = sink.max.z
soap_dispenser.facing = vanity.facing
set_coordinate_frame(scene)

set_coordinate_frame(toilet)
toilet_paper_holder.min.x = toilet.min.x - 0.2
toilet_paper_holder.center.y = toilet.center.y
toilet_paper_holder.min.z = 0.6
toilet_paper_holder.facing = X_MAX
set_coordinate_frame(scene)

storage_cabinet.max.x = scene.max.x
storage_cabinet.min.y = scene.min.y + 0.1
storage_cabinet.min.z = 1.6
storage_cabinet.facing = X_MIN

towel_rack.max.x = scene.max.x
towel_rack.center.y = scene.center.y
towel_rack.min.z = 1.2
towel_rack.facing = X_MIN

bath_mat.center.x = bathtub.center.x
bath_mat.min.y = bathtub.min.y - 0.1
bath_mat.min.z = scene.min.z
bath_mat.facing = bathtub.facing

plant.min.x = scene.min.x + 0.1
plant.min.y = scene.min.y + 0.1
plant.min.z = scene.min.z
plant.facing = X_MAX