set_title("Electronics Shop")
set_size(width=8, depth=10, height=3)
set_floor_asset("Vinyl Floor", color="9BA0A8")
set_wall_asset("Painted Wall", interior=True, color="E6E6E8")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
back_door = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="708090")
windows = [Window("Display Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(2)]

# Main display shelves along walls
wall_shelves = [Object("Display Shelf", width=2.0, depth=0.4, height=2.0, support=STANDING, color="F5F5F5") for _ in range(4)]

# Central display islands
display_islands = [Object("Display Table", width=1.2, depth=0.8, height=0.9, support=STANDING, color="E0E0E0") for _ in range(2)]

# Counter area
counter = Object("Sales Counter", width=2.0, depth=0.6, height=1.0, support=STANDING, color="4682B4")
register = Object("Cash Register", width=0.4, depth=0.3, height=0.2, support=STANDING, color="1E90FF")

# Display items (representing groups of products)
laptops = [Object("Laptop", width=0.4, depth=0.3, height=0.02, support=STANDING, color="AAAAAA") for _ in range(6)]
smartphones = [Object("Smartphone", width=0.05, depth=0.1, height=0.01, support=STANDING, color="FF4500") for _ in range(8)]
tv_displays = [Object("Television", width=1.2, depth=0.1, height=0.7, support=MOUNTED, color="000080") for _ in range(2)]
gaming_console = Object("Gaming Console", width=0.15, depth=0.4, height=0.5, support=STANDING, color="32CD32")
security_camera = Object("Security Camera", width=0.1, depth=0.1, height=0.1, support=MOUNTED, color="4B0082")

# Storage and workspace
repair_desk = Object("Repair Desk", width=1.4, depth=0.7, height=0.8, support=STANDING, color="8B4513")
tool_cabinet = Object("Tool Cabinet", width=1.0, depth=0.5, height=1.8, support=STANDING, color="2F4F4F")