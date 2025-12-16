scene: Scene
X_MAX = 0
Y_MAX = 1
X_MIN = 2
Y_MIN = 3
Z_MIN = 0
Z_MAX = 1

RIGHT_WALL = 0
TOP_WALL = 1
LEFT_WALL = 2
BOTTOM_WALL = 3

def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            #error_class = err.__class__.__name__
            #cl, exc, tb = sys.exc_info()
            #scene.llm_error(ERROR.PYTHON, f'INTERNAL EXCEPTION: {exc}')
            scene.llm_error(ERROR.PYTHON, f'INTERNAL EXCEPTION: {e}')
    return wrapper

def set_size(width: float, depth: float, height: float):
    scene.width = width
    scene.depth = depth
    scene.height = height
    scene.size = Vec(width, depth, height)
    scene.fcenter = Vec(0.0, 0.0, 0.5 * height)

def set_title(title: str):
    scene.title = title

def set_floor_asset(asset_name: str, color: str | None = None):
    scene.floor_asset = asset_name
    scene.floor_color = color

def set_wall_asset(asset_name: str, interior: bool = True, color: str | None = None):
    scene.wall_asset = asset_name
    scene.interior = interior
    scene.wall_color = color

def set_coordinate_frame(o: Obj):
    if o.otype != OBJECT.SCENE:
        o.finalize()
    scene.coordinate_frame = o
    o.is_frame = True

def center(o: Obj) -> Obj:
    return o

def opposite(i: int) -> int:
    return (i + 2) % 4

def number(counter: int, x: float) -> float:
    m = scene.mapping[counter]
    return x if m < 0 else scene.constant_vec[m]

def random_direction() -> int:
    return scene.rng.randint(0, 3)



@catch_errors
def Object(name: str, width: float, depth: float, height: float, support: int, color: str | None = None, dynamic: bool = False) -> Obj:
#def Object(name: str, width: float, depth: float, height: float, support: int, dynamic: bool = False) -> Obj:
    o = Obj(scene, remove_trailing_numbers(name), OBJECT.OBJECT, width, depth, height, None, support, color if isinstance(color, str) and len(color) == 6 else None, dynamic)
    #o = Obj(scene, remove_trailing_numbers(name), OBJECT.OBJECT, width, depth, height, None, support, None, dynamic)
    scene.objs.append(o)
    return o

@catch_errors
def Door(name: str, width: float, depth: float, height: float, color: str | None = None, support = -1, dynamic: bool = False) -> Obj:
#def Door(name: str, width: float, depth: float, height: float, support = -1, dynamic: bool = False) -> Obj:
    o = Obj(scene, remove_trailing_numbers(name), OBJECT.DOOR, width, depth, height, None, MOUNTED, color if isinstance(color, str) and len(color) == 6 else None, False)
    #o = Obj(scene, remove_trailing_numbers(name), OBJECT.DOOR, width, depth, height, None, MOUNTED, None, False)
    scene.objs.append(o)
    return o

@catch_errors
def Window(name: str, width: float, depth: float, height: float, color: str | None = None, support = -1, dynamic: bool = False) -> Obj:
#def Window(name: str, width: float, depth: float, height: float, support = -1, dynamic: bool = False) -> Obj:
    o = Obj(scene, remove_trailing_numbers(name), OBJECT.WINDOW, width, depth, height, None, MOUNTED, color if isinstance(color, str) and len(color) == 6 else None, False)
    #o = Obj(scene, remove_trailing_numbers(name), OBJECT.WINDOW, width, depth, height, None, MOUNTED, None, False)
    scene.objs.append(o)
    return o
