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

door.max.x = scene.max.x
door.center.y = scene.min.y + 0.2 * scene.depth
door.min.z = scene.min.z
door.facing = X_MIN

for i, window in enumerate(windows):
    window.center.x = scene.min.x + (i+1.0) / 4.0 * scene.width
    window.min.y = scene.min.y
    window.min.z = 1.0
    window.facing = Y_MAX

teacher_desk.center.x = scene.min.x + 0.25 * scene.width
teacher_desk.max.y = scene.max.y - 0.5
teacher_desk.min.z = scene.min.z
teacher_desk.facing = Y_MIN

set_coordinate_frame(teacher_desk)
teacher_chair.center.x = teacher_desk.center.x
teacher_chair.min.y = teacher_desk.max.y + 0.1
teacher_chair.min.z = scene.min.z
teacher_chair.facing = teacher_desk
set_coordinate_frame(scene)

for i, (desk, chair) in enumerate(zip(student_desks, student_chairs)):
    row = i // 3
    col = i % 3
    desk.center.x = scene.min.x + (col+1.0) / 4.0 * scene.width
    desk.center.y = scene.min.y + (row+1.0) / 6.0 * scene.depth
    desk.min.z = scene.min.z
    desk.facing = Y_MIN
    
    set_coordinate_frame(desk)
    chair.center.x = desk.center.x
    chair.min.y = desk.max.y + 0.1
    chair.min.z = scene.min.z
    chair.facing = desk
    set_coordinate_frame(scene)

whiteboard.center.x = scene.min.x + 0.5 * scene.width
whiteboard.max.y = scene.max.y
whiteboard.min.z = 1.0
whiteboard.facing = Y_MIN

bulletin_board.max.x = scene.max.x - 0.2
bulletin_board.max.y = scene.max.y
bulletin_board.min.z = 1.2
bulletin_board.facing = Y_MIN

bookshelf.min.x = scene.min.x
bookshelf.min.y = scene.min.y + 0.2
bookshelf.min.z = scene.min.z
bookshelf.facing = X_MAX

set_coordinate_frame(teacher_desk)
globe.min.x = teacher_desk.min.x + 0.1
globe.min.y = teacher_desk.min.y + 0.1
globe.min.z = teacher_desk.max.z
globe.facing = teacher_desk.facing
computer.max.x = teacher_desk.max.x - 0.1
computer.center.y = teacher_desk.center.y
computer.min.z = teacher_desk.max.z
computer.facing = teacher_desk.facing
set_coordinate_frame(scene)

projector_screen.center.x = scene.min.x + 0.5 * scene.width
projector_screen.max.y = scene.max.y
projector_screen.min.z = whiteboard.max.z + 0.1
projector_screen.facing = Y_MIN

storage_cabinet.max.x = scene.max.x
storage_cabinet.min.y = scene.min.y + 0.2
storage_cabinet.min.z = scene.min.z
storage_cabinet.facing = X_MIN

map.min.x = scene.min.x
map.max.y = scene.max.y
map.min.z = 1.2
map.facing = X_MAX

clock.max.x = scene.max.x - 0.2
clock.center.y = scene.min.y + 0.5 * scene.depth
clock.min.z = 2.0
clock.facing = X_MIN