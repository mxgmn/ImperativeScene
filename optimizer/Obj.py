# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

import math
from dataclasses import dataclass
from enum import Enum

from .Vec import Vec, best_dir
from .exceptions import ERROR
from .Settings import Settings
from .logger import info, warning

bound_names = ["CENTER", "MIN", "MAX"]
X = 0
Y = 1
Z = 2
"""
AIR = -3
CEILING = -2
GROUND = -1
"""
RIGHT_WALL = 0
TOP_WALL = 1
LEFT_WALL = 2
BOTTOM_WALL = 3

STANDING = 0
MOUNTED = 1
FLOATING = 2

class OBJECT(Enum):
    OBJECT = 0
    WALL = 1
    FLOOR = 2
    DOOR = 3
    WINDOW = 4
    SCENE = 5

class BOUND(Enum):
    CENTER = 0
    MIN = 1
    MAX = 2

@dataclass
class Relation:
    btype: BOUND
    axis: int
    value: float



class Obj:
    group: int
    name: str
    otype: OBJECT
    support: int
    direction: int | None
    directed: bool
    size: Vec | None
    color: str | None
    is_frame: bool
    dynamic: bool

    width: float
    depth: float
    height: float
    fcenter: Vec

    #mem_supporting_surface: int | 'Obj' | None
    #mem_facing: int | 'Obj' | None
    relations: list[Relation]

    def __init__(self, scene, name: str, otype: OBJECT, width: float, depth: float, height: float, direction: int | None, support: int, color: str | None, dynamic: bool):
        if scene is not None:
            self.scene = scene
            if (name, otype) not in scene.group_names:
                scene.group_names.append((name, otype))
            self.group = len(scene.group_names) - 1
        self.name = name
        self.otype = otype
        self.support = support
        self.direction = direction
        self.directed = direction is not None and otype != OBJECT.FLOOR
        self.size = None
        self.color = color
        self.is_frame = False
        self.dynamic = dynamic

        self.width = width
        self.depth = depth
        self.height = height

        #self.mem_supporting_surface = None
        self.mem_facing = None
        self.relations = []

        if self.direction is not None:
            self.size = Vec(depth, width, height) if self.direction % 2 == 0 else Vec(width, depth, height)
        #self.fcenter = Vec(0, 0, 0) if otype == OBJECT.SCENE else Vec(0, 0, 0.5 * height)
        self.fcenter = Vec(0, 0, 0.5 * height)


    def __str__(self):
        return self.name

    def apply_relations(self) -> None:
        """
        Их нельзя применять сразу же в сеттерах, потому что изначально не известны ориентации объектов.
        """
        for rel in self.relations:
            if rel.btype == BOUND.MIN:
                if rel.axis == X:
                    self.fcenter.x = rel.value + 0.5 * self.size.x
                elif rel.axis == Y:
                    self.fcenter.y = rel.value + 0.5 * self.size.y
                else:
                    self.fcenter.z = rel.value + 0.5 * self.size.z
            elif rel.btype == BOUND.MAX:
                if rel.axis == X:
                    self.fcenter.x = rel.value - 0.5 * self.size.x
                elif rel.axis == Y:
                    self.fcenter.y = rel.value - 0.5 * self.size.y
                else:
                    self.fcenter.z = rel.value - 0.5 * self.size.z
            else:
                if rel.axis == X:
                    self.fcenter.x = rel.value
                elif rel.axis == Y:
                    self.fcenter.y = rel.value
                else:
                    self.fcenter.z = rel.value

        # тут нужно выводить ошибки, если саппортные координаты не согласуются с уже поставленными координатами
        """
        if Settings.SUPPORTING_SURFACE_ENABLED and isinstance(self.mem_supporting_surface, int):
            if self.mem_supporting_surface == GROUND and self.fcenter.z < 0.5 * self.size.z:
                self.fcenter.z = 0.5 * self.size.z
            elif self.mem_supporting_surface == CEILING:
                self.fcenter.z = self.scene.fmax().z - 0.5 * self.size.z
            elif self.mem_supporting_surface == RIGHT_WALL:
                self.fcenter.x = self.scene.fmax().x - 0.5 * self.size.x
            elif self.mem_supporting_surface == BOTTOM_WALL:
                self.fcenter.y = self.scene.fmin().y + 0.5 * self.size.y
            elif self.mem_supporting_surface == LEFT_WALL:
                self.fcenter.x = self.scene.fmin().x + 0.5 * self.size.x
            elif self.mem_supporting_surface == TOP_WALL:
                self.fcenter.y = self.scene.fmax().y - 0.5 * self.size.y
        """
        # В идеале эту штуку нужно применять, только если ЛЛМ не указала z для объекта!
        # А вообще это должен быть один из вариантов устранения ошибки. Нужно просто сравнивать лоссы различных функций.
        #elif isinstance(self.mem_supporting_surface, Obj) and self.mem_supporting_surface.otype == OBJECT.OBJECT:
        #    self.fcenter.z = self.mem_supporting_surface.fcenter.z + 0.5 * (self.size.z + self.mem_supporting_surface.size.z)


    def finalize(self) -> None:
        if self.direction is not None:
            return
        nexttowalls = [False, False, False, False]
        any_ntw = False
        #if Settings.SUPPORTING_SURFACE_ENABLED and (self.supporting_surface == RIGHT_WALL or self.supporting_surface == TOP_WALL or self.supporting_surface == LEFT_WALL or self.supporting_surface == BOTTOM_WALL):
        #    nexttowalls[self.supporting_surface] = True
        #    any_ntw = True
        #else:
        for rel in self.relations:
            if rel.btype == BOUND.MAX and rel.axis == X and rel.value == 0.5 * self.scene.width:
                nexttowalls[0] = True
                any_ntw = True
            if rel.btype == BOUND.MAX and rel.axis == Y and rel.value == 0.5 * self.scene.depth:
                nexttowalls[1] = True
                any_ntw = True
            if rel.btype == BOUND.MIN and rel.axis == X and rel.value == -0.5 * self.scene.width:
                nexttowalls[2] = True
                any_ntw = True
            if rel.btype == BOUND.MIN and rel.axis == Y and rel.value == -0.5 * self.scene.depth:
                nexttowalls[3] = True
                any_ntw = True
        #info(f"\nnexttowalls({self.name}) = {nexttowalls}")

        first_of_its_name = None
        for o in self.scene.objs:
            if o.name == self.name and o.direction is not None:
                first_of_its_name = o
                break

        self.fcenter = self.scene.random_position(self.width, self.depth, self.height)
        self.size = Vec(self.width, self.depth, self.height) if self.scene.rng is None or self.scene.rng.choice([True, False]) else Vec(self.depth, self.width, self.height) # прикидочный размер
        self.apply_relations()

        consult = None if self.scene.consult_vec is None else self.scene.consult_vec[self.group]

        case = "default"
        if self.mem_facing is not None:
            self.directed = True
            if isinstance(self.mem_facing, int):
                case = f"facing a specific dir {self.mem_facing}"
                self.direction = self.mem_facing if consult is None else consult
            elif isinstance(self.mem_facing, Obj):
                case = f"facing an object {self.mem_facing}"
                temp_dir = best_dir(self.fcenter, self.mem_facing.fcenter, self.mem_facing.size) if consult is None else consult
                self.direction = temp_dir if consult is None else consult
            else:
                self.scene.llm_error(ERROR.MISUSE, f"unknown facing type {self.mem_facing}")
        else:
            if (self.width > self.scene.size.x or self.depth > self.scene.size.y) and self.width <= self.scene.size.y and self.depth <= self.scene.size.x:
                case = "only one way to fit the object: 0 or 2"
                self.direction = self.scene.rng.choice([0, 2]) if consult is None else consult
            elif (self.width > self.scene.size.y or self.depth > self.scene.size.x) and self.width <= self.scene.size.x and self.depth <= self.scene.size.y:
                case = "only one way to fit the object: 1 or 3"
                self.direction = self.scene.rng.choice([1, 3]) if consult is None else consult

            elif nexttowalls[0] and not nexttowalls[1] and not nexttowalls[2] and not nexttowalls[3] and self.depth <= 2.0 * self.width:
                case = f"next to the right wall, ok depth => 2"
                self.direction = 2 if consult is None else consult
                self.directed = True
            elif nexttowalls[2] and not nexttowalls[0] and not nexttowalls[1] and not nexttowalls[3] and self.depth <= 2.0 * self.width:
                case = f"next to the left wall, ok depth => 0"
                self.direction = 0 if consult is None else consult
                self.directed = True
            elif nexttowalls[3] and not nexttowalls[0] and not nexttowalls[1] and not nexttowalls[2] and self.depth <= 2.0 * self.width:
                case = f"next to the bottom wall, ok depth => 1"
                self.direction = 1 if consult is None else consult
                self.directed = True
            elif nexttowalls[1] and not nexttowalls[0] and not nexttowalls[2] and not nexttowalls[3] and self.depth <= 2.0 * self.width:
                case = f"next to the top wall, ok depth => 3"
                self.direction = 3 if consult is None else consult
                self.directed = True
            elif any_ntw:
                self.direction = (self.scene.rng.choice([i for i, ntw in enumerate(nexttowalls) if ntw]) + 2) % 4
                case = f"next to wall {nexttowalls} => {self.direction}"
                if self.fmin().z > 0.1:
                    self.directed = True
            #elif (nexttowalls[0] or nexttowalls[2]) and not nexttowalls[1] and not nexttowalls[3]:
            #    case = f"next to a left/right wall, very deep => 1 or 3"
            #    self.direction = self.scene.rng.choice([0, 2]) if consult is None else consult
            #    if self.fmin().z > 0.1:
            #        self.directed = True
            #elif (nexttowalls[1] or nexttowalls[3]) and not nexttowalls[0] and not nexttowalls[2]:
            #    case = f"next to a top/bottom wall, very deep => 0 or 2"
            #    self.direction = self.scene.rng.choice([1, 3]) if consult is None else consult
            #    if self.fmin().z > 0.1:
            #        self.directed = True
            #elif isinstance(self.mem_supporting_surface, Obj):
            #    case = "on top of an oriented object"
            #    self.direction = self.mem_supporting_surface.direction
            #    if self.mem_supporting_surface.directed:
            #        self.directed = True

            elif first_of_its_name is not None:
                case = "oriented a group of objects the same way"
                self.direction = first_of_its_name.direction
                if first_of_its_name.directed:
                    self.directed = True
            else:
                case = "full random, but actually just 1"
                #self.direction = self.scene.rng.choice([0, 1, 2, 3]) if consult is None else consult
                self.direction = 1 if consult is None else consult

        if Settings.PRINT_ORIENTATION_CASES and self.scene.consult_vec is None:
            info(f"{self.name} orientation case: {case}")
        self.size = Vec(self.depth, self.width, self.height) if self.direction % 2 == 0 else Vec(self.width, self.depth, self.height)
        self.apply_relations()

        """
        if isinstance(self.mem_supporting_surface, Obj):
            b = self.mem_supporting_surface
            if self.fcenter.x - 0.5 * self.size.x > b.fmax().x:
                self.fcenter.x = b.fmax().x - 0.5 * self.size.x
            elif self.fcenter.x + 0.5 * self.size.x < b.fmin().x:
                self.fcenter.x = b.fmin().x + 0.5 * self.size.x
            if self.fcenter.y - 0.5 * self.size.y > b.fmax().y:
                self.fcenter.y = b.fmax().y - 0.5 * self.size.y
            elif self.fcenter.y + 0.5 * self.size.y < b.fmin().y:
                self.fcenter.y = b.fmin().y + 0.5 * self.size.y
        """


    def fmin(self) -> Vec:
        return self.fcenter - 0.5 * self.size
    def fmax(self) -> Vec:
        return self.fcenter + 0.5 * self.size

    # я даже не уверен, что мне тут нужно возвращать баунд. Может быть достаточно вектора
    @property
    def min(self) -> 'Bound':
        return Bound(self, BOUND.MIN)
    @property
    def max(self) -> 'Bound':
        return Bound(self, BOUND.MAX)
    @property
    def center(self) -> 'Bound':
        return Bound(self, BOUND.CENTER)

    @center.setter
    def center(self, value) -> None: # здесь я не сделал учёт локальных координат
        if isinstance(value, Bound):
            self.center.x = value.x
            self.center.y = value.y
            #self.center.z = value.z
        elif isinstance(value, Vec):
            relx = Relation(BOUND.CENTER, X, value.x)
            rely = Relation(BOUND.CENTER, Y, value.y)
            relz = Relation(BOUND.CENTER, Z, value.z)
            self.relations.append(relx)
            self.relations.append(rely)
            self.relations.append(relz)
        else:
            self.scene.llm_error(ERROR.MISUSE, f"The RHS of {self.name}.center = ... should be a bound, not {value}")

    #@property
    #def supporting_surface(self) -> int:
    #    raise Exception("supporting_surface read was deprecated")
    #    #return self.mem_supporting_surface

    #@supporting_surface.setter
    #def supporting_surface(self, value) -> None:
    #    raise Exception("supporting_surface write was deprecated")
    #    #if isinstance(value, int) or isinstance(value, Obj):
    #    #    self.mem_supporting_surface = value
    #    #else:
    #    #    raise Exception(f"supporting_surface of {self.name} should be either an int or an Obj, not {value}")

    @property
    def facing(self) -> int | None:
        self.finalize()
        return self.direction

    @facing.setter
    def facing(self, value) -> None:
        if value is None:# or self.otype == OBJECT.DOOR or self.otype == OBJECT.WINDOW:
            pass # но если мы так делаем, то нам нужно автоматически детектировать ориентацию. Но автоматически это сделать невозможно, если дверь стоит в углу!
        elif isinstance(value, int) or isinstance(value, float):
            self.mem_facing = int(value) % 4 if value < 10.0 else int(value / 90.0) % 4
        elif isinstance(value, Obj):
            self.mem_facing = value
            self.mem_facing.finalize() # неприятно, но нужно для хороших дефолтов
        elif isinstance(value, Bound):
            b = value.o
            if b.otype != OBJECT.SCENE:
                b.finalize()
            self.mem_facing = b
        else:
            raise Exception(f"{self}.facing should be either an int or an Obj, not {value}")

    def distortion(self) -> float:
        return abs(math.log(self.width / self.depth))

    def next_to_wall(self) -> bool:
        return (abs(self.fmin().x - self.scene.fmin().x) < 0.011 or abs(self.fmax().x - self.scene.fmax().x) < 0.011 or
                abs(self.fmin().y - self.scene.fmin().y) < 0.011 or abs(self.fmax().y - self.scene.fmax().y) < 0.011)
    #def mounted_on_ceiling(self) -> bool:
    #    return abs(self.fmax().z - self.scene.fmax().z) < 0.011 and abs(self.fmin().z - self.scene.fmin().z) > 0.012 and not self.next_to_wall() and self.mem_supporting_surface == CEILING

    def covered_by(self, o: 'Obj'):
        return (self.fmin().x >= o.fmin().x - 0.01 and self.fmax().x <= o.fmax().x + 0.01 and self.fmin().y >= o.fmin().y - 0.01 and self.fmax().y <= o.fmax().y + 0.01
                  and self.fmin().z >= o.fmin().z - 0.01 and self.fmax().z <= o.fmax().z + 0.01)

    def covered(self) -> bool:
        for o in self.scene.objs:
            if o == self:
                continue
            if o.name == self.name: # не решение, желательно оставлять 1 объект из группы, а остальные удалять
                continue
            if self.covered_by(o):
                return True
        return False

    def completely_out_of_bounds(self) -> bool:
        return (self.fmax().x < self.scene.fmin().x - 0.01 or self.fmin().x > self.scene.fmax().x + 0.01 or
                self.fmax().y < self.scene.fmin().y - 0.01 or self.fmin().y > self.scene.fmax().y + 0.01 or
                self.fmax().z < self.scene.fmin().z - 0.01)# or self.fmin().z > self.scene.fmax().z + 0.01)

    def height_above_support(self) -> float:
        min_z = self.fmin().z
        max_z = self.fmax().z
        if min_z < 0.025:
            return min_z
        min_height = min_z
        for o in self.scene.objs:
            if o == self:
                continue
            if not overlap_xy(o, self):
                continue
            if o.fmin().z > max_z:
                continue
            h = min_z - o.fmax().z
            if h < min_height:
                min_height = h
        return min_height

    def on(self, support: 'Obj') -> bool:
        if support.is_rug():
            return False
        return overlap_xy(self, support) and abs(self.fmin().z - support.fmax().z) < 0.05
    def above(self, support: 'Obj') -> bool:
        if support.is_rug():
            return False
        return overlap_xy(self, support) and self.fmax().z >= support.fmin().z
    def supporting_object(self):
        if abs(self.fmin().z) < 0.05:
            return self.scene
        for o in self.scene.objs:
            if o != self and self.on(o):
                return o
        return None

    def local_from_global(self, globl: Vec) -> Vec:
        v = globl - self.fcenter
        if self.direction == 0:
            return Vec(-v.y, v.x, v.z)
        elif self.direction == 1:
            return v
        elif self.direction == 2:
            return Vec(v.y, -v.x, v.z)
        elif self.direction == 3:
            return Vec(-v.x, -v.y, v.z)
        else:
            raise Exception(f"incorrect {self.name} direction {self.direction}")
    """
    def global_from_local(self, local: Vec) -> Vec:
        if self.direction == 0:
            return self.fcenter + Vec(local.y, -local.x, local.z)
        elif self.direction == 1:
            return self.fcenter + Vec(-local.x, -local.y, local.z)
        elif self.direction == 2:
            return self.fcenter + Vec(-local.y, local.x, local.z)
        elif self.direction == 3:
            return self.fcenter + local
        else:
            raise Exception(f"incorrect {self.name} direction {self.direction}")
    """

    def is_rug(self) -> bool:
        return self.height <= 0.1 * self.width and self.height <= 0.1 * self.depth and self.height < 0.2
    def is_flat(self) -> bool:
        return self.height < 0.2 * max(self.width, self.depth)
    def is_tall(self) -> bool:
        return self.height / min(self.width, self.depth) > 2.5


class Bound:
    o: 'Obj'
    btype: BOUND

    def __init__(self, o, btype):
        self.o = o
        self.btype = btype

    def __str__(self):
        return f"{self.o}.{bound_names[self.btype.value]}"

    @property
    def x(self):
        if self.o.otype != OBJECT.SCENE:
            self.o.finalize()
        frame: Obj = self.o.scene.coordinate_frame
        if self.btype == BOUND.CENTER:
            #return self.o.fcenter.x
            return frame.local_from_global(self.o.fcenter).x
        elif self.btype == BOUND.MIN:
            #return self.o.fmin().x
            if frame.direction == 0:
                return -(self.o.fmax().y - frame.fcenter.y)
            elif frame.direction == 1:
                return self.o.fmin().x - frame.fcenter.x
            elif frame.direction == 2:
                return self.o.fmin().y - frame.fcenter.y
            elif frame.direction == 3:
                return -(self.o.fmax().x - frame.fcenter.x)
            else:
                raise Exception(f"unexpected frame.direction={frame.direction} direction in getter, frame = {frame}") # это странно, потому что стол должен быть финализирован
        else:
            #return self.o.fmax().x
            if frame.direction == 0:
                return -(self.o.fmin().y - frame.fcenter.y)
            elif frame.direction == 1:
                return self.o.fmax().x - frame.fcenter.x
            elif frame.direction == 2:
                return self.o.fmax().y - frame.fcenter.y
            elif frame.direction == 3:
                return -(self.o.fmin().x - frame.fcenter.x)
            else:
                raise Exception("unexpected direction in getter")

    @property
    def y(self):
        if self.o.otype != OBJECT.SCENE:
            self.o.finalize()
        frame: Obj = self.o.scene.coordinate_frame
        if self.btype == BOUND.CENTER:
            #return self.o.fcenter.y
            return frame.local_from_global(self.o.fcenter).y
        elif self.btype == BOUND.MIN:
            #return self.o.fmin().y
            if frame.direction == 0:
                return self.o.fmin().x - frame.fcenter.x
            elif frame.direction == 1:
                return self.o.fmin().y - frame.fcenter.y
            elif frame.direction == 2:
                return -(self.o.fmax().x - frame.fcenter.x)
            elif frame.direction == 3:
                return -(self.o.fmax().y - frame.fcenter.y)
            else:
                raise Exception("unexpected direction in getter")
        else:
            #return self.o.fmax().y
            if frame.direction == 0:
                return self.o.fmax().x - frame.fcenter.x
            elif frame.direction == 1:
                return self.o.fmax().y - frame.fcenter.y
            elif frame.direction == 2:
                return -(self.o.fmin().x - frame.fcenter.x)
            elif frame.direction == 3:
                return -(self.o.fmin().y - frame.fcenter.y)
            else:
                raise Exception("unexpected direction in getter")

    @property
    def z(self):
        if self.o.otype != OBJECT.SCENE:
            self.o.finalize()
        #frame_z = self.o.coordinate_frame.fcenter.z
        if self.btype == BOUND.CENTER:
            return self.o.fcenter.z# - frame_z
        elif self.btype == BOUND.MIN:
            #print(f"{self.o}.min.z = {self.o.fmin().z - frame_z} = {self.o.fmin().z} - {frame_z}")
            #return 0.0 if self.o.otype == OBJECT.SCENE else self.o.fmin().z - frame_z
            return self.o.fmin().z# - frame_z
        else:
            #return self.o.scene.height if self.o.otype == OBJECT.SCENE else self.o.fmax().z - frame_z
            return self.o.fmax().z# - frame_z

    @x.setter
    def x(self, value) -> None:
        if not isinstance(value, float) and not isinstance(value, int):
            raise Exception(f"unsupported RHS {value}")
        o = self.o
        frame: Obj = self.o.scene.coordinate_frame
        if self.btype == BOUND.MIN:
            #rel = Relation(BOUND.MIN, X, value)
            if frame.direction == 0:
                rel = Relation(BOUND.MAX, Y, frame.fcenter.y - value)
            elif frame.direction == 1:
                rel = Relation(BOUND.MIN, X, frame.fcenter.x + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.MIN, Y, frame.fcenter.y + value)
            elif frame.direction == 3:
                rel = Relation(BOUND.MAX, X, frame.fcenter.x - value)
            else:
                raise Exception("unexpected direction in setter")
        elif self.btype == BOUND.MAX:
            #rel = Relation(BOUND.MAX, X, value)
            if frame.direction == 0:
                rel = Relation(BOUND.MIN, Y, frame.fcenter.y - value)
            elif frame.direction == 1:
                rel = Relation(BOUND.MAX, X, frame.fcenter.x + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.MAX, Y, frame.fcenter.y + value)
            elif frame.direction == 3:
                rel = Relation(BOUND.MIN, X, frame.fcenter.x - value)
            else:
                raise Exception("unexpected direction in setter")
        else:
            #rel = Relation(BOUND.CENTER, X, value)
            if frame.direction == 0:
                rel = Relation(BOUND.CENTER, Y, frame.fcenter.y - value)
            elif frame.direction == 1:
                rel = Relation(BOUND.CENTER, X, frame.fcenter.x + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.CENTER, Y, frame.fcenter.y + value)
            elif frame.direction == 3:
                rel = Relation(BOUND.CENTER, X, frame.fcenter.x - value)
            else:
                raise Exception("unexpected direction in setter")
        o.relations.append(rel)


    @y.setter
    def y(self, value) -> None:
        if not isinstance(value, float) and not isinstance(value, int):
            raise Exception(f"unsupported RHS {value}")
        o = self.o
        frame: Obj = self.o.scene.coordinate_frame
        if self.btype == BOUND.MIN:
            #rel = Relation(BOUND.MIN, Y, value)
            if frame.direction == 0:
                rel = Relation(BOUND.MIN, X, frame.fcenter.x + value)
            elif frame.direction == 1:
                rel = Relation(BOUND.MIN, Y, frame.fcenter.y + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.MAX, X, frame.fcenter.x - value)
            elif frame.direction == 3:
                rel = Relation(BOUND.MAX, Y, frame.fcenter.y - value)
            else:
                raise Exception("unexpected direction in setter")
        elif self.btype == BOUND.MAX:
            #rel = Relation(BOUND.MAX, Y, value)
            if frame.direction == 0:
                rel = Relation(BOUND.MAX, X, frame.fcenter.x + value)
            elif frame.direction == 1:
                rel = Relation(BOUND.MAX, Y, frame.fcenter.y + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.MIN, X, frame.fcenter.x - value)
            elif frame.direction == 3:
                rel = Relation(BOUND.MIN, Y, frame.fcenter.y - value)
            else:
                raise Exception("unexpected direction in setter")
        else:
            #rel = Relation(BOUND.CENTER, Y, value)
            if frame.direction == 0:
                rel = Relation(BOUND.CENTER, X, frame.fcenter.x + value)
            elif frame.direction == 1:
                rel = Relation(BOUND.CENTER, Y, frame.fcenter.y + value)
            elif frame.direction == 2:
                rel = Relation(BOUND.CENTER, X, frame.fcenter.x - value)
            elif frame.direction == 3:
                rel = Relation(BOUND.CENTER, Y, frame.fcenter.y - value)
            else:
                raise Exception("unexpected direction in setter")
        o.relations.append(rel)


    @z.setter
    def z(self, value) -> None:
        if not isinstance(value, float) and not isinstance(value, int):
            raise Exception(f"unsupported RHS {value}")
        o = self.o
        #if isinstance(o.supporting_surface, Obj) or o.supporting_surface == GROUND: #print(f"ignoring {o} z setter because of supporting surface {o.supporting_surface}")
        #    return
        #if self.btype == BOUND.MIN:
        #    value += 0.5 * o.height
        #elif self.btype == BOUND.MAX:
        #    value -= 0.5 * o.height
        #o.fcenter.z = value + o.coordinate_frame.fcenter.z
        #o.relations.append(Relation(self.btype, Z, value + o.coordinate_frame.fcenter.z))
        o.relations.append(Relation(self.btype, Z, value))

def overlap_xy(o1: Obj, o2: Obj) -> bool:
    return o1.fmax().x > o2.fmin().x and o2.fmax().x > o1.fmin().x and o1.fmax().y > o2.fmin().y and o2.fmax().y > o1.fmin().y

#def overlap_loss_xy(min1: Vec, max1: Vec, o2: Obj) -> float:
#    min2, max2 = o2.fmin(), o2.fmax()
#    min_overlap = min(max1.x - min2.x, max2.x - min1.x, max1.y - min2.y, max2.y - min1.y, max1.z - min2.z, max2.z - min1.z)
#    if min_overlap < 0.01:
#        return 0.0
#    else:
#        ox = min(max1.x, max2.x) - max(min1.x, min2.x)
#        oy = min(max1.y, max2.y) - max(min1.y, min2.y)
#        return 0.5 * (ox + oy)

def overlap_loss_xyz(min1: Vec, max1: Vec, o2: Obj) -> float:
    min2, max2 = o2.fmin(), o2.fmax()
    min_overlap = min(max1.x - min2.x, max2.x - min1.x, max1.y - min2.y, max2.y - min1.y, max1.z - min2.z, max2.z - min1.z)
    if min_overlap < 0.01:
        #if min_overlap > 0:
        #    warning(f"overlap with {o2} is tiny")
        return 0.0
    else:
        ox = min(max1.x, max2.x) - max(min1.x, min2.x)
        oy = min(max1.y, max2.y) - max(min1.y, min2.y)
        oz = min(max1.z, max2.z) - max(min1.z, min2.z)
        #return 0.33 * (ox + oy + oz)
        return math.pow(ox * oy * oz, 1.0/3.0)
        #return ox * oy * oz

def overlap_loss(o1: Obj, o2: Obj) -> float:
    if o1.is_rug() or o2.is_rug():
        #warning(f"{o1} or {o2} is rug")
        return 0.0
    result = overlap_loss_xyz(o1.fmin(), o1.fmax(), o2)
    #if result <= 0:
    #    warning(f"{o1} and {o2} don't overlap")
    return result

def door_loss(door: Obj, o2: Obj, width: float) -> float:
    if door.direction % 2 == 0:
        v = Vec(width, 0.0, 0.0)
    else:
        v = Vec(0.0, width, 0.0)
    min1, max1 = door.fmin() - v, door.fmax() + v
    min2, max2 = o2.fmin(), o2.fmax()
    min_overlap = min(max1.x - min2.x, max2.x - min1.x, max1.y - min2.y, max2.y - min1.y, max1.z - min2.z, max2.z - min1.z)
    if min_overlap < 0.01:
        return 0.0
    else:
        ox = min(max1.x, max2.x) - max(min1.x, min2.x)
        oy = min(max1.y, max2.y) - max(min1.y, min2.y)
        return 0.5 * (ox + oy)