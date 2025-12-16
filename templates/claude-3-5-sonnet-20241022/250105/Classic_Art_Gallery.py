set_title("Classic Art Gallery")
set_size(width=15, depth=12, height=3.5)
set_floor_asset("Marble Floor", color="E8E6E1")
set_wall_asset("Smooth Wall", interior=True, color="F5F5F5")

entrance = Door("Glass Door", width=1.8, depth=0.1, height=2.2, color="87CEEB")
emergency_exit = Door("Metal Door", width=0.9, depth=0.1, height=2.0, color="CD853F")
windows = [Window("Large Window", width=2.0, depth=0.1, height=2.0, color="ADD8E6") for _ in range(3)]

# Main artwork displays
paintings = [
    Object("Large Painting", width=2.0, depth=0.1, height=1.5, support=MOUNTED, color="B22222"),
    Object("Large Painting", width=1.8, depth=0.1, height=1.4, support=MOUNTED, color="4B0082"),
    Object("Large Painting", width=2.0, depth=0.1, height=1.5, support=MOUNTED, color="84B222"),
    Object("Large Painting", width=1.8, depth=0.1, height=1.4, support=MOUNTED, color="005782"),
    Object("Medium Painting", width=1.5, depth=0.1, height=1.2, support=MOUNTED, color="006400"),
    Object("Medium Painting", width=1.4, depth=0.1, height=1.1, support=MOUNTED, color="CD853F"),
    Object("Small Painting", width=1.0, depth=0.1, height=0.8, support=MOUNTED, color="4682B4"),
    Object("Small Painting", width=0.9, depth=0.1, height=0.7, support=MOUNTED, color="DAA520")
]

# Sculptures and pedestals
pedestals = [Object("Display Pedestal", width=0.6, depth=0.6, height=1.0, support=STANDING, color="D3D3D3") for _ in range(4)]
sculptures = [
    Object("Classical Sculpture", width=0.4, depth=0.4, height=0.8, support=STANDING, color="F0F8FF"),
    Object("Modern Sculpture", width=0.5, depth=0.5, height=1.2, support=STANDING, color="FFD700"),
    Object("Abstract Sculpture", width=0.6, depth=0.6, height=0.9, support=STANDING, color="FF4500"),
    Object("Bronze Statue", width=0.4, depth=0.4, height=1.0, support=STANDING, color="CD853F")
]

# Furniture and amenities
benches = [Object("Gallery Bench", width=1.2, depth=0.4, height=0.45, support=STANDING, color="8B4513") for _ in range(3)]
information_desk = Object("Reception Desk", width=2.0, depth=0.8, height=1.0, support=STANDING, color="A0522D")
brochure_stand = Object("Brochure Stand", width=0.4, depth=0.3, height=1.2, support=STANDING, color="4682B4")
plants = [Object("Indoor Plant", width=0.6, depth=0.6, height=1.2, support=STANDING, color="228B22") for _ in range(4)]