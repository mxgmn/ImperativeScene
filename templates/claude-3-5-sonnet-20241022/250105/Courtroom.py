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