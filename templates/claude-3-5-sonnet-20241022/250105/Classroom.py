set_title("Classroom")
set_size(width=8, depth=6, height=3)
set_floor_asset("Linoleum Floor", color="B5B5A3")
set_wall_asset("Painted Wall", interior=True, color="E6E6D8")

door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")
windows = [Window("Window", width=1.2, depth=0.1, height=1.5, color="87CEEB") for _ in range(3)]

# Main furniture
teacher_desk = Object("Teacher Desk", width=1.4, depth=0.8, height=0.75, support=STANDING, color="8B4513")
teacher_chair = Object("Office Chair", width=0.6, depth=0.6, height=1.0, support=STANDING, color="4682B4")
student_desks = [Object("Student Desk", width=0.6, depth=0.4, height=0.7, support=STANDING, color="DEB887") for _ in range(15)]
student_chairs = [Object("Student Chair", width=0.4, depth=0.4, height=0.8, support=STANDING, color="4169E1") for _ in range(15)]

# Educational equipment
whiteboard = Object("Whiteboard", width=3.0, depth=0.05, height=1.2, support=MOUNTED, color="FFFFFF")
bulletin_board = Object("Bulletin Board", width=1.2, depth=0.05, height=0.9, support=MOUNTED, color="CD853F")
bookshelf = Object("Bookshelf", width=1.2, depth=0.4, height=1.8, support=STANDING, color="8B4513")
globe = Object("Globe", width=0.3, depth=0.3, height=0.45, support=STANDING, color="4682B4")
computer = Object("Desktop Computer", width=0.4, depth=0.4, height=0.4, support=STANDING, color="696969")
projector_screen = Object("Projector Screen", width=2.0, depth=0.05, height=1.5, support=MOUNTED, color="F5F5F5")
storage_cabinet = Object("Storage Cabinet", width=0.8, depth=0.4, height=1.8, support=STANDING, color="B8860B")

# Educational decorations
map = Object("World Map", width=1.5, depth=0.05, height=1.0, support=MOUNTED, color="F0E68C")
clock = Object("Wall Clock", width=0.3, depth=0.05, height=0.3, support=MOUNTED, color="B22222")