set_title("Courtroom")
set_size(width=12, depth=15, height=4)
set_floor_asset("Hardwood Floor", color="8B4513")
set_wall_asset("Wood Panel Wall", interior=True, color="966F33")

main_door = Door("Double Door", width=1.8, depth=0.1, height=2.2, color="8B4513")
side_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.5, depth=0.1, height=2.0, color="87CEEB") for _ in range(3)]

# Main court furniture
judges_bench = Object("Judge Bench", width=4.0, depth=1.2, height=0.3, support=STANDING, color="8B4513")
judges_chair = Object("Leather Chair", width=0.8, depth=0.8, height=1.2, support=STANDING, color="800000")
witness_stand = Object("Witness Stand", width=1.5, depth=1.2, height=0.2, support=STANDING, color="A0522D")
witness_chair = Object("Wooden Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="8B4513")

# Lawyer tables
prosecution_table = Object("Table", width=2.0, depth=0.8, height=0.75, support=STANDING, color="A0522D")
defense_table = Object("Table", width=2.0, depth=0.8, height=0.75, support=STANDING, color="A0522D")
lawyer_chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="800000") for _ in range(4)]

# Jury section
jury_box = Object("Jury Box", width=4.0, depth=2.0, height=0.5, support=STANDING, color="8B4513")
jury_chairs = [Object("Wooden Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="8B4513") for _ in range(12)]

# Gallery
gallery_benches = [Object("Wooden Bench", width=3.0, depth=0.6, height=0.9, support=STANDING, color="A0522D") for _ in range(6)]

# Decorative elements
flag = Object("American Flag", width=1.2, depth=0.1, height=2.0, support=MOUNTED, color="B22222")
seal = Object("Court Seal", width=1.5, depth=0.1, height=1.5, support=MOUNTED, color="FFD700")
railing = Object("Wooden Railing", width=6.0, depth=0.1, height=0.9, support=STANDING, color="8B4513")

main_door.center.x = scene.center.x
main_door.min.y = scene.min.y
main_door.min.z = scene.min.z
main_door.facing = Y_MAX

side_door.max.x = scene.max.x
side_door.max.y = scene.max.y - 0.2 * scene.depth
side_door.min.z = scene.min.z
side_door.facing = X_MIN

for i, window in enumerate(windows):
    window.min.x = scene.min.x
    window.center.y = scene.min.y + (i+1.0) / 4.0 * scene.depth
    window.min.z = 1.0
    window.facing = X_MAX

judges_bench.center.x = scene.center.x
judges_bench.max.y = scene.max.y - 0.1 * scene.depth
judges_bench.min.z = 0.5
judges_bench.facing = Y_MIN

set_coordinate_frame(judges_bench)
judges_chair.center.x = judges_bench.center.x
judges_chair.center.y = judges_bench.center.y
judges_chair.min.z = judges_bench.max.z
judges_chair.facing = judges_bench.facing
set_coordinate_frame(scene)

witness_stand.max.x = judges_bench.min.x - 0.5
witness_stand.max.y = judges_bench.max.y - 0.5
witness_stand.min.z = 0.3
witness_stand.facing = Y_MIN

set_coordinate_frame(witness_stand)
witness_chair.center = witness_stand.center
witness_chair.min.z = witness_stand.max.z
witness_chair.facing = witness_stand.facing
set_coordinate_frame(scene)

prosecution_table.min.x = scene.min.x + 0.2 * scene.width
prosecution_table.center.y = scene.center.y
prosecution_table.min.z = scene.min.z
prosecution_table.facing = judges_bench

defense_table.max.x = scene.max.x - 0.2 * scene.width
defense_table.center.y = scene.center.y
defense_table.min.z = scene.min.z
defense_table.facing = judges_bench

for i, chair in enumerate(lawyer_chairs):
    if i < 2:
        table = prosecution_table
        set_coordinate_frame(table)
        chair.center.x = table.min.x + (i+0.5) * table.width/2.0
    else:
        table = defense_table
        set_coordinate_frame(table)
        chair.center.x = table.min.x + ((i-2)+0.5) * table.width/2.0
    chair.min.y = table.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = judges_bench
set_coordinate_frame(scene)

jury_box.max.x = scene.max.x - 0.1 * scene.width
jury_box.max.y = judges_bench.max.y
jury_box.min.z = 0.3
jury_box.facing = X_MIN

set_coordinate_frame(jury_box)
for i, chair in enumerate(jury_chairs):
    row = i // 6
    col = i % 6
    chair.center.x = jury_box.min.x + (col+0.5) / 6.0 * jury_box.width
    chair.center.y = jury_box.min.y + (row+0.5) / 2.0 * jury_box.depth
    chair.min.z = jury_box.max.z
    chair.facing = jury_box.facing
set_coordinate_frame(scene)

for i, bench in enumerate(gallery_benches):
    row = i // 3
    col = i % 3
    bench.center.x = scene.min.x + (col+1.0) / 4.0 * scene.width
    bench.center.y = scene.min.y + (row+1.0) / 3.0 * scene.depth/2.0
    bench.min.z = scene.min.z
    bench.facing = judges_bench

flag.min.x = scene.min.x
flag.max.y = scene.max.y - 0.1 * scene.depth
flag.min.z = 1.5
flag.facing = X_MAX

seal.center.x = scene.center.x
seal.max.y = scene.max.y
seal.min.z = 2.0
seal.facing = Y_MIN

railing.center.x = scene.center.x
railing.center.y = scene.center.y
railing.min.z = scene.min.z
railing.facing = Y_MIN