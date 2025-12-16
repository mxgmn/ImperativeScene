set_title("Circus Ring")
set_size(width=15, depth=15, height=6)
set_floor_asset("Sawdust Floor", color="D2B48C")
set_wall_asset("Striped Wall", interior=True, color="F5F5DC")

entrance_door = Door("Double Door", width=2.0, depth=0.1, height=2.2, color="8B0000")
backstage_door = Door("Wooden Door", width=0.9, depth=0.1, height=2.0, color="8B4513")

# Main performance area
ring = Object("Circus Ring", width=8.0, depth=8.0, height=0.1, support=STANDING, color="FFD700")

bleachers = [Object("Bleacher Section", width=7.5, depth=1.2, height=0.8, support=STANDING, color="8B4513") for _ in range(4)]

# Performance equipment
trampoline = Object("Trampoline", width=2.0, depth=2.0, height=0.4, support=STANDING, color="4169E1")
balance_beam = Object("Balance Beam", width=0.2, depth=4.0, height=1.2, support=STANDING, color="CD853F")
pedestals = [
    Object("Performance Pedestal", width=0.6, depth=0.6, height=h, support=STANDING, color="B8860B")
    for h in [0.3, 0.6, 0.9]  # Different heights for variety
]

# Props and equipment
prop_chest = Object("Storage Chest", width=1.2, depth=0.8, height=0.9, support=STANDING, color="8B008B")
safety_mats = [
    Object("Safety Mat", width=2.0, depth=1.5, height=0.2, support=STANDING, color="4B0082")
    for _ in range(3)
]

# Decorative elements
banners = [
    Object("Decorative Banner", width=1.0, depth=0.05, height=2.0, support=MOUNTED, color=color)
    for color in ["FF0000", "FFFF00", "FF1493", "00FF00"]
]

podium = Object("Ringmaster Podium", width=0.8, depth=0.8, height=1.0, support=STANDING, color="DC143C")

# Animal equipment (suggesting presence without actual animals)
cage_cart = Object("Cage Cart", width=1.8, depth=1.2, height=1.5, support=STANDING, color="B8860B")