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

# Place the main towers
towers[0].min.x = scene.min.x
towers[0].center.y = scene.center.y
towers[0].min.z = scene.min.z
towers[0].facing = Y_MIN

towers[1].max.x = scene.max.x
towers[1].center.y = scene.center.y
towers[1].min.z = scene.min.z
towers[1].facing = Y_MIN

# Place the gate between towers
gate.center.x = scene.center.x
gate.center.y = scene.center.y
gate.min.z = scene.min.z
gate.facing = Y_MIN

# Place barricades in front of the gate
spacing = 0.25
for i, barricade in enumerate(barricades):
    barricade.center.x = scene.center.x + (i-1.5) * (barricade.width + spacing)
    barricade.center.y = scene.min.y + 0.3 * scene.depth
    barricade.min.z = scene.min.z
    barricade.facing = Y_MAX

# Place braziers near towers
set_coordinate_frame(towers[0])
braziers[0].min.x = towers[0].max.x + 0.5
braziers[0].min.y = towers[0].min.y + 0.5
braziers[0].min.z = scene.min.z
braziers[0].facing = Y_MIN

braziers[1].min.x = towers[0].max.x + 0.5
braziers[1].max.y = towers[0].max.y - 0.5
braziers[1].min.z = scene.min.z
braziers[1].facing = Y_MIN

set_coordinate_frame(towers[1])
braziers[2].max.x = towers[1].min.x - 0.5
braziers[2].min.y = towers[1].min.y + 0.5
braziers[2].min.z = scene.min.z
braziers[2].facing = Y_MIN

braziers[3].max.x = towers[1].min.x - 0.5
braziers[3].max.y = towers[1].max.y - 0.5
braziers[3].min.z = scene.min.z
braziers[3].facing = Y_MIN
set_coordinate_frame(scene)

# Place banners on towers
set_coordinate_frame(towers[0])
banners[0].center.x = towers[0].center.x
banners[0].min.y = towers[0].min.y
banners[0].min.z = 4.0
banners[0].facing = Y_MAX

set_coordinate_frame(towers[1])
banners[1].center.x = towers[1].center.x
banners[1].min.y = towers[1].min.y
banners[1].min.z = 4.0
banners[1].facing = Y_MAX
set_coordinate_frame(scene)

# Place stone blocks along the walls
block_spacing = 0.3
for i, block in enumerate(stone_blocks[:3]):
    block.min.x = towers[0].max.x + (i+1.0) * (block.width + block_spacing)
    block.min.y = scene.min.y + 0.15 * scene.depth
    block.min.z = scene.min.z
    block.facing = Y_MAX

for i, block in enumerate(stone_blocks[3:]):
    block.max.x = towers[1].min.x - (i+1.0) * (block.width + block_spacing)
    block.min.y = scene.min.y + 0.15 * scene.depth
    block.min.z = scene.min.z
    block.facing = Y_MAX

# Place spikes in defensive positions
spike_spacing = 0.4
for i, spike in enumerate(spikes[:4]):
    spike.center.x = scene.center.x + (i-1.5) * (spike.width + spike_spacing)
    spike.min.y = scene.min.y + 0.2 * scene.depth
    spike.min.z = scene.min.z
    spike.facing = Y_MAX

for i, spike in enumerate(spikes[4:]):
    spike.center.x = scene.center.x + (i-1.5) * (spike.width + spike_spacing)
    spike.min.y = scene.min.y + 0.25 * scene.depth
    spike.min.z = scene.min.z
    spike.facing = Y_MAX

# Place racks inside towers
set_coordinate_frame(towers[0])
racks[0].center.x = towers[0].center.x
racks[0].min.y = towers[0].min.y + 0.2
racks[0].min.z = scene.min.z
racks[0].facing = Y_MIN

set_coordinate_frame(towers[1])
racks[1].center.x = towers[1].center.x
racks[1].min.y = towers[1].min.y + 0.2
racks[1].min.z = scene.min.z
racks[1].facing = Y_MIN
set_coordinate_frame(scene)