"""
Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

"""

import os
import time

from optimizer.helper import delete_all_files, remove_comments
from optimizer.Vec import ideal_size
from optimizer.Optimizer import Optimizer
from optimizer.Scene import Scene
from optimizer.Stat import Stat
from optimizer.LLM import LLM
from optimizer.Settings import Settings, MODE, FILENAMES
from optimizer.prompts import scheme_system, scheme_incontexts, layout_system, layout_incontexts, single_chain_system, single_chain_incontexts, coord_system, coord_incontexts
from optimizer.logger import info

OUTPUT_FOLDER = "output"

QUERIES = ["Amusement Park", "Ancient Temple", "Arcade Center", "Astronomy Observatory", "Barbie's Dream House", "Bathroom with a Bathtub", "Botanical Garden", "Bouldering Gym", "Casino", "Cat Cafe with Catwalks", "Chess Board", "Chess Tournament Hall", "Circus", "City Block", "City Park", "Classic Art Gallery", "Classroom", "Cloudborne Pantheon", "College Gym", "Competitive FPS Level", "Construction Site", "Courtroom", "Dark Fortress Gate", "Data Center", "Depths of Hell", "Electronics Shop", "Factory Floor", "Florist Shop", "Forest Clearing", "Futuristic Command Center", "Garage for 2 Cars", "Graveyard", "Greenhouse", "Gun Shop", "Hair Salon", "Hedge Maze", "History Museum Hall", "Ice City", "Indiana Jones Filming Set", "Jurassic Park", "Kindergarten", "Laundromat", "Library", "Lich King's Throneroom", "Living Room", "Mancave", "Medieval Village Square", "Modern Open-Plan Office", "Obstacle Course", "Opera", "Parking Lot", "Pirate Ship Deck", "Post-Apocalyptic Campsite", "Prison Cell", "Race Track Section", "Railway Station Platform", "Restaurant", "Rogue Encampment", "Sheep Farm", "Skyward Kingdom", "Spaceship Cabin", "Spacious Kitchen for a Family of 12", "Stables", "Stonehenge", "Supermarket", "Treetop House", "Vegan Cafe", "Wild West Saloon", "Wine Cellar", "Wizard's Laboratory"]

#QUERIES = ["3D Mario Level", "Large Commercial Warehouse", "Amusement Park", "Ancient Temple", "Astronomy Observatory", "Barbie's House", "Bathroom with a Bathtub", "Bedroom", "Botanical Garden", "Bouldering Gym without a Bouldering Cave", "Casino", "Cat Cafe with Catwalks", "Chess Board", "Chess Tournament", "Circus", "City Block", "Classic Art Gallery", "Classroom", "Construction Site", "Dark Fortress Gate", "Depths of Hell", "Electronics Shop", "Florist Shop", "Forest Clearing", "Futuristic Command Center", "Garage for 2 Cars", "Go Board", "Graveyard", "Greenhouse", "Grocery Store", "Gun Shop", "Hair Salon", "Hedge Maze", "History Museum Hall", "Indiana Jones Filming Set", "Jurassic Park", "Kindergarten", "Lair of Fire Elementals", "Laundromat", "Library", "Lich King's Throneroom", "Mancave", "Minotaur's Labyrinth", "Modern Open-Plan Office", "Opera", "City Park", "Parking Lot", "Pirate Ship Deck", "Post-Apocalyptic Campsite", "Prison Cell", "Quake Level", "Race Track Section", "Railway Station", "Restaurant", "Rogue Encampment", "Roguelike Dungeon", "Sheep Farm", "Spaceship Cabin", "Kitchen for a Family of 12", "Stables", "Stonehenge", "Supermarket", "Tower with a Spiral Staircase", "Treetop House", "Vegan Cafe", "Medieval Village Neighborhood", "Wild West Saloon", "Wine Cellar", "Wizard's Laboratory", "Zoo Enclosure"]

#QUERIES = ["village", "two towers", "harry potter", "stonehenge", "go board", "chess board", "chess tournament", "classroom", "opera", "supermarket", "grocery store", "3d mario level", "roguelike dungeon", "labyrinth", "maze", "tower with a spiral staircase", "race track section", "parking", "park", "hair salon", "quake level", "bedroom", "office", "small korean restaurant", "wizard's laboratory", "garage for 2 cars", "bathroom with a bathtub", "mancave", "kindergarten", "classic art gallery", "modern art gallery", "spaceship cabin", "electronics shop", "futuristic command center", "library", "vegan cafe", "indiana jones filming set", "post-apocalyptic campsite", "forest", "circus", "laundromat", "sheep farm", "city", "casino", "graveyard", "pirate ship deck", "lich king's throneroom", "ancient temple", "lair of fire elementals", "dungeon", "astronomy observatory", "history museum", "natural history museum", "amusement park", "fortress gate", "d2 rogue encampment", "gun shop", "depths of hell", "barbie's house", "prison cell", "gym", "wine cellar", "florist shop", "greenhouse", "jurassic park", "tavern", "treetop house", "cat cafe with catwalks", "bouldering gym without a bouldering cave", "amazon warehouse", "botanical garden", "zoo", "stables", "fortress of angband"]

#QUERIES = ["cthulhu village", "movie theater", "clinical laboratory", "medieval castle study", "steampunk workshop", "underwater research facility", "solarpunk rooftop garden", "moon base", "mars base", "cyberpunk armory", "dwarven forge", "colonists' hideout from the movie aliens", "skyrim interior", "vampire's lair", "japanese bedroom", "locker room", "music studio"][0:1]

def save(llm_code: str, basename: str, savefolder: str) -> None:
    if not Settings.SAVE_JSON:
        return
    folder_path = f"{savefolder}/{Settings.MODEL.replace(':', '')}"
    os.makedirs(folder_path, exist_ok=True)
    savepath = f"{folder_path}/{basename}.py"
    info(f"saving at '{savepath}'")
    with open(savepath, "w") as file:
        file.write(llm_code)

def run_layout(llm_code: str, basename: str | None, env_code: str) -> Scene | None:
    llm_code = remove_comments(llm_code)
    optimizer = Optimizer(basename, env_code, OUTPUT_FOLDER)
    result = optimizer.run(llm_code)
    if basename is not None and Settings.RENDER_EACH_SCENE:
        os.makedirs("bin", exist_ok=True)
        os.chdir('bin')
        #os.system(f"SceneVisualizer.exe folder=../{OUTPUT_FOLDER}/ filename={basename} size=1200x1200 panelwidth=540 ao=-1 font=10x20 distance=11.5 super=1 names=true allnames=false ortho=false")
        #os.system(f"SceneVisualizer.exe folder=../{OUTPUT_FOLDER}/ filename={basename}- size=1200x1200 panelwidth=0 ao=-1 font=10x20 distance=11.5 super=2 ortho=false names=false mask=true")
        os.system(f"SceneVisualizer.exe folder=../{OUTPUT_FOLDER}/ filename={basename}- {Settings.VISUALIZER}")
        os.chdir('..')
    return result

def chain(env_code: str, scheme_llm: LLM, layout_llm: LLM, query: str) -> Scene:
    basename = query.replace(" ", "_")
    scheme_code = scheme_llm.run(query)
    scheme = run_layout(scheme_code, None, env_code)
    new_size = ideal_size(scheme.size, scheme.filled_area(), scheme.max_object_length(), Settings.MIN_FILL, Settings.MAX_FILL)
    updated_scheme_code = scheme_code
    if new_size.x != scheme.size.x or new_size.y != scheme.size.y:
        lines = scheme_code.splitlines()
        lines[1] = f"set_size(width={new_size.x}, depth={new_size.y}, height={new_size.z})"
        updated_scheme_code = '\n'.join(lines)
        info(f"changing size in {basename}")
    save(updated_scheme_code, basename, "templates")
    layout_code = layout_llm.run(updated_scheme_code)
    scene_code = updated_scheme_code + "\n\n" + layout_code
    save(scene_code, basename, "layouts")
    return run_layout(scene_code, basename, env_code)



def main() -> None:
    if Settings.MODE != MODE.RENDER:
        delete_all_files(OUTPUT_FOLDER)
    this_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'optimizer', 'env.py'), 'r', encoding='utf-8') as file:
        env_code = file.read()

    start_time = time.time()
    scenes = []

    if Settings.MODE == MODE.CHAIN:
        scheme_dialog = [scheme_system]
        for example_name in scheme_incontexts:
            with open(os.path.join(this_path, "templates", f"{example_name}.py"), "r", encoding='utf-8') as file:
                code = file.read()
            scheme_dialog.append(example_name.lower().replace('_', ' '))
            scheme_dialog.append(code)
        scheme_llm = LLM(Settings.MODEL, scheme_dialog)
        layout_dialog = [layout_system]
        for example_name in layout_incontexts:
            with open(os.path.join(this_path, "templates", f"{example_name}.py"), "r", encoding='utf-8') as file:
                scheme_code = file.read()
            with open(os.path.join(this_path, "layouts", f"{example_name}.py"), "r", encoding='utf-8') as file:
                layout_code = file.read()
            layout_dialog.append(scheme_code)
            layout_dialog.append(layout_code)
        layout_llm = LLM(Settings.MODEL, layout_dialog)
        for i, query in enumerate(QUERIES):
            info(f"\n>> {query} << {i + 1}/{len(QUERIES)}")
            scene = chain(env_code, scheme_llm, layout_llm, query)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.GENERATE_SCHEME:
        dialog = [scheme_system]
        for example_name in scheme_incontexts:
            with open(os.path.join(this_path, "templates", f"{example_name}.py"), "r", encoding='utf-8') as file:
                code = file.read()
            dialog.append(example_name.lower().replace('_', ' '))
            dialog.append(code)
        llm = LLM(Settings.MODEL, dialog)
        for i, query in enumerate(QUERIES):
            basename = query.replace(" ", "_")
            info(f"\n>> {basename} << {i + 1}/{len(QUERIES)}")
            llm_code = llm.run(query)
            save(llm_code, basename, "templates")
            run_layout(llm_code, basename, env_code)
    elif Settings.MODE == MODE.GENERATE_COORDS:
        dialog = [coord_system]
        for example_name in coord_incontexts:
            with open(os.path.join(this_path, "templates", f"{example_name}.py"), "r", encoding='utf-8') as file:
                scheme_code = file.read()
            with open(os.path.join(this_path, "coords", f"{example_name}.py"), "r", encoding='utf-8') as file:
                layout_code = file.read()
            dialog.append(scheme_code)
            dialog.append(layout_code)
        llm = LLM(Settings.MODEL, dialog)
        for i, SCENENAME in enumerate(FILENAMES):
            with open(os.path.join(this_path, "templates", f"{SCENENAME}.py"), "r", encoding='utf-8') as file:
                scheme_code = file.read()
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            layout_code = llm.run(scheme_code)
            scene_code = scheme_code + "\n\n" + layout_code
            save(scene_code, basename, "coords")
            scene = run_layout(scene_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.GENERATE_LAYOUT:
        dialog = [layout_system]
        for example_name in layout_incontexts:
            with open(os.path.join(this_path, "templates", f"{example_name}.py"), "r", encoding='utf-8') as file:
                scheme_code = file.read()
            with open(os.path.join(this_path, "layouts", f"{example_name}.py"), "r", encoding='utf-8') as file:
                layout_code = file.read()
            dialog.append(scheme_code)
            dialog.append(layout_code)
        llm = LLM(Settings.MODEL, dialog)
        for i, SCENENAME in enumerate(FILENAMES):
            with open(os.path.join(this_path, "templates", f"{SCENENAME}.py"), "r", encoding='utf-8') as file:
                scheme_code = file.read()
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            layout_code = llm.run(scheme_code)
            scene_code = scheme_code + "\n\n" + layout_code
            save(scene_code, basename, "layouts")
            scene = run_layout(scene_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.UPDATE_SCHEME:
        for i, SCENENAME in enumerate(FILENAMES):
            file_path = os.path.join(this_path, "templates", f"{SCENENAME}.py")
            with open(file_path, "r", encoding='utf-8') as file:
                scheme_code = file.read()
            scheme = run_layout(scheme_code, None, env_code)
            info(os.path.basename(SCENENAME))
            print(f"scheme filled_area = {scheme.filled_area()}")
            new_size = ideal_size(scheme.size, scheme.filled_area(), scheme.max_object_length(), Settings.MIN_FILL, Settings.MAX_FILL)
            if new_size.x != scheme.size.x or new_size.y != scheme.size.y:
                lines = scheme_code.splitlines()
                lines[1] = f"set_size(width={new_size.x}, depth={new_size.y}, height={new_size.z})"
                scheme_code = '\n'.join(lines)
                info(f"updating {SCENENAME}")
                with open(file_path, "w", encoding='utf-8') as file:
                    file.write(scheme_code)
    elif Settings.MODE == MODE.GENERATE_FULL_SCENE:
        dialog = [single_chain_system]
        for example_name in single_chain_incontexts:
            with open(os.path.join(this_path, "examples", f"{example_name}.py"), "r", encoding='utf-8') as file:
                code = file.read()
            dialog.append(example_name.lower().replace('_', ' '))
            dialog.append(code)
        llm = LLM(Settings.MODEL, dialog)
        for i, query in enumerate(QUERIES):
            basename = query.replace(" ", "_")
            info(f"\n>> {basename} << {i + 1}/{len(QUERIES)}")
            llm_code = llm.run(query)
            save(llm_code, basename, "examples")
            scene = run_layout(llm_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.RUN_SCHEME: # по сути просто run_scene
        for i, SCENENAME in enumerate(FILENAMES):
            with open(f"templates/{SCENENAME}.py", 'r', encoding='utf-8') as scene_file:
                scene_code = remove_comments(scene_file.read())
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            scene = run_layout(scene_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.RUN_COORD_LAYOUT:
        for i, SCENENAME in enumerate(FILENAMES):
            #with open(f"templates/{SCENENAME}.py", 'r', encoding='utf-8') as scheme_file:
            #    scheme_code = remove_comments(scheme_file.read())
            with open(f"coords/{SCENENAME}.py", 'r', encoding='utf-8') as layout_file:
                layout_code = remove_comments(layout_file.read())
            #scene_code = scheme_code + "\n" + layout_code
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            scene = run_layout(layout_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.RUN_LAYOUT:
        for i, SCENENAME in enumerate(FILENAMES):
            with open(f"templates/{SCENENAME}.py", 'r', encoding='utf-8') as scheme_file:
                scheme_code = remove_comments(scheme_file.read())
            with open(f"layouts/{SCENENAME}.py", 'r', encoding='utf-8') as layout_file:
                layout_code = remove_comments(layout_file.read())
            scene_code = scheme_code + "\n" + layout_code
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            scene = run_layout(scene_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)
    elif Settings.MODE == MODE.RUN_FULL_SCENE or Settings.MODE == MODE.RUN_FULL_LAYOUT:
        folder = "layouts" if Settings.MODE == MODE.RUN_FULL_LAYOUT else "examples"
        for i, SCENENAME in enumerate(FILENAMES):
            with open(f"{folder}/{SCENENAME}.py", 'r', encoding="utf-8", errors="replace") as scene_file:
                scene_code = scene_file.read()
            basename = os.path.basename(SCENENAME)
            info(f"\n>> {basename} << {i + 1}/{len(FILENAMES)}")
            scene = run_layout(scene_code, basename, env_code)
            if scene is not None:
                scenes.append(scene)

    end_time = time.time()
    elapsed_time = end_time - start_time
    info(f"executed in {elapsed_time:.1f} seconds")

    if len(scenes) > 0:
        stat = Stat(scenes)
        stat.print()

    if Settings.RENDER_EACH_SCENE is False:
        os.makedirs("bin", exist_ok=True)
        os.chdir('bin')
        os.system(f"SceneVisualizer.exe folder=../{OUTPUT_FOLDER}/ {Settings.RENDER_STR if Settings.MODE == MODE.RENDER else Settings.VISUALIZER}")
        os.chdir('..')

    #if Settings.AST:
    #    if not Settings.GENERATE: # просто выполнить код
    #        with open("code/ring.py", 'r', encoding='utf-8') as layout_file:
    #            code = layout_file.read()
    #        run_layout(code, "ring.py", env_code, None)
    #    else:
    #        with open("code/ring.py", "r") as file:
    #            code = file.read()
    #        syntax_tree = ast.parse(code)
    #        print(ast.dump(syntax_tree, indent=4))


main()

"""
Давайте в openai перейдём на официальную библиотеку.
Есть вероятность, что maxtokens влияет на ленивость генерации.
не забыть добавить температуру
Особенно будет интересно для reasoning models.

Изменение вертикального положения монтированных объектов должно стоить больше - добавить в optimal transport cost.

Вычисление коста можно оптимизировать через таблицу изменённых объектов.

Практически полезная оптимизация для фиксированных мультиплайеров: вычисление коста убираем, но оптимизируем константы от конца к началу. Потому что последние константы меньше влияют на лейоут (из-за природы императивных программ).

(!) Хм, так давайте действительно разрешим векторные направления, а потом их округлим до 4-х сторон света! Это гораздо более естественно в плане языка!
М.б. действительно нужно делать векторозначные facing вместо Y_POS, X_NEG.
Просто лучше сцены получатся.

FACING = 5
FACING_SCENE = 6
FACING_WALL = 7
Кажется, я пришёл к пониманию, как организовать этот тип ошибки: сравнения с ЛЛМ-вариантом быть не должно
"""
