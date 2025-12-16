set_title("Theater")
set_size(width=10, depth=12, height=4)
set_floor_asset("Carpet Floor", color="462B37")
set_wall_asset("Fabric Panels Wall", interior=True, color="5E434B")

main_entrance = Door("Entrance Double Door", width=2.0, depth=0.1, height=2.0, color="800000")
backdoor = Door("Wooden Door", width=0.8, depth=0.1, height=2.0, color="D2691E")

stage = Object("Theater Stage", width=8, depth=4, height=0.5, support=STANDING, color="4B0082")
piano = Object("Upright Piano", width=1.5, depth=0.6, height=1.2, support=STANDING, color="FF4500")
decoration = Object("Theatrical Decoration of a Victorian Mansion", width=stage.width, depth=0.2, height = scene.height - stage.height, support=STANDING, color="8B0000")
seats = [Object("Seat", width=0.5, depth=0.4, height=0.8, support=STANDING, color="B22222") for _ in range(5 * 8)]
spotlights = [Object("Spotlight", 0.2, 0.2, 0.2, support=MOUNTED, color="FFFACD") for _ in range(4)]
plants = [Object("Potted Plant", 0.3, 0.3, height=0.5, support=STANDING, color="32CD32") for _ in range(2)]