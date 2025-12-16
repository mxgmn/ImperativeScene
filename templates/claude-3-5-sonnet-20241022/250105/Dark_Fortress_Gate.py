set_title("Dark Fortress Gate")
set_size(width=18, depth=15, height=8)
set_floor_asset("Stone Block Floor", color="2F4F4F")
set_wall_asset("Dark Stone Wall", interior=False, color="1C1C1C")

# Main architectural elements
towers = [Object("Stone Tower", width=4.0, depth=4.0, height=8.0, support=STANDING, color="2B2B2B") for _ in range(2)]
gate = Object("Portcullis", width=4.0, depth=0.3, height=5.0, support=STANDING, color="4A4A4A")
barricades = [Object("Medieval Barricade", width=1.5, depth=0.6, height=1.0, support=STANDING, color="84240C") for _ in range(4)]

# Decorative elements
braziers = [Object("Brazier", width=0.8, depth=0.8, height=1.2, support=STANDING, color="FF4500") for _ in range(4)]
banners = [Object("Banner", width=1.0, depth=0.1, height=2.0, support=STANDING, color="8B0000") for _ in range(2)]

# Ground elements
stone_blocks = [Object("Stone Block", width=1.0, depth=1.0, height=0.8, support=STANDING, color="4F4F4F") for _ in range(6)]
spikes = [Object("Iron Spike", width=0.2, depth=0.2, height=0.8, support=STANDING, color="363636") for _ in range(8)]

# Guard elements
racks = [
    Object("Weapon Rack", width=2.0, depth=0.4, height=1.8, support=STANDING, color="8B4513"),
    Object("Armor Rack", width=2.0, depth=0.4, height=1.8, support=STANDING, color="8B4513")
]