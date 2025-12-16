set_title("Modern Open-Plan Office")
set_size(width=15, depth=12, height=3)
set_floor_asset("Commercial Carpet Floor", color="7B8B8E")
set_wall_asset("Modern Wall", interior=True, color="E5E5E5")

entrance = Door("Glass Door", width=1.2, depth=0.1, height=2.2, color="87CEEB")
windows = [Window("Window Panel", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(4)]

# Main work areas
desks = [Object("Office Desk", width=1.4, depth=0.8, height=0.75, support=STANDING, color="F5F5F5") for _ in range(8)]
chairs = [Object("Office Chair", width=0.6, depth=0.6, height=1.1, support=STANDING, color="4682B4") for _ in range(8)]
computers = [Object("Computer Monitor", width=0.6, depth=0.2, height=0.4, support=STANDING, color="2F4F4F") for _ in range(8)]

# Collaborative area
meeting_table = Object("Conference Table", width=2.4, depth=1.2, height=0.75, support=STANDING, color="B8860B")
meeting_chairs = [Object("Meeting Chair", width=0.5, depth=0.5, height=0.9, support=STANDING, color="4682B4") for _ in range(6)]

# Storage and organization
filing_cabinets = [Object("Filing Cabinet", width=0.5, depth=0.6, height=1.3, support=STANDING, color="708090") for _ in range(3)]
bookshelf = Object("Bookshelf", width=1.8, depth=0.4, height=1.8, support=STANDING, color="8B4513")

# Break area
kitchenette = Object("Kitchen Counter", width=2.0, depth=0.6, height=0.9, support=STANDING, color="DCDCDC")
water_cooler = Object("Water Dispenser", width=0.4, depth=0.4, height=1.2, support=STANDING, color="87CEEB")
coffee_machine = Object("Coffee Machine", width=0.4, depth=0.3, height=0.35, support=STANDING, color="CD853F")

# Plants for better atmosphere
plants = [Object("Indoor Plant", width=0.4, depth=0.4, height=1.2, support=STANDING, color="228B22") for _ in range(4)]

# Presentation area
whiteboard = Object("Whiteboard", width=2.0, depth=0.05, height=1.2, support=MOUNTED, color="FFFFFF")