from enum import Enum
from .helper import whole_folder

class MODE(Enum):
    RUN_SCHEME = 0
    RUN_LAYOUT = 1
    RUN_COORD_LAYOUT = 2
    RUN_FULL_SCENE = 3
    RUN_FULL_LAYOUT = 4 # like RUN_FULL_SCENE, but from layouts folder
    GENERATE_SCHEME = 5
    GENERATE_COORDS = 6
    GENERATE_LAYOUT = 7
    GENERATE_FULL_SCENE = 8
    CHAIN = 9
    UPDATE_SCHEME = 10
    RENDER = 11



#FILENAMES = ["Bedroom"]
#FILENAMES = ["Cozy_Italian_Restaurant"]
#FILENAMES = ["Garage"]
#FILENAMES = ["Theater"]

#FILENAMES = ["Labyrinth"]
#FILENAMES = ["Maze"]

#FILENAMES = ["ErroneousRestaurant"]
#FILENAMES = ["claude-3-5-sonnet-20241022/250105/Botanical_Garden"]

#FILENAMES = whole_folder("templates", "claude-3-5-sonnet-20241022/250105")[0:5]
FILENAMES = whole_folder("layouts", "claude-3-5-sonnet-20241022/250105")



class Settings:
    MODEL = "gpt-5.2-2025-12-11"
    #MODEL = "claude-3-5-sonnet-20241022"
    FLOOR_THICKNESS = 0.1 # 0.1
    WALL_THICKNESS = 0.1 # 0.1
    POST_POLISH = False # True
    PRINT_ORIENTATION_CASES = False # False
    ALL_WALLS = True # True
    MIN_FILL = 0.12 # 0.12
    MAX_FILL = 0.5 # 0.5
    SEARCH_CONSTANTS = True # True
    SEARCH_ORIENTATIONS = True # True
    FIXED_MULTIPLIERS = False
    OPTIMAL_TRANSPORT = False
    MERGE_CONSTANTS = False
    COMPUTE_COSTS = True # True
    ANIMATION_FRAMES = 1 # 1
    RENDER_EACH_SCENE = True # None
    SAVE_JSON = True # False
    SAVE_PYTHON = False # False
    MIN_SIZE = 65 # 65
    MAX_TILES = 1 # 5
    SEED = None # None, 3
    GRADIENT_DESCENT = False
    VISUALIZER = "size=1200x1200 panelwidth=540 ao=-1 font=10x20 distance=11.5 super=1 names=false allnames=true ortho=false mask=false"
    RENDER_STR = "size=1600x1600 panelwidth=0 ao=-1 font=10x20 distance=11.5 super=2 ortho=false names=true mask=false"
    MODE = MODE.GENERATE_LAYOUT # RUN_FULL_LAYOUT
