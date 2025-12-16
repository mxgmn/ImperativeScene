# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

import json
import math
import random
import traceback
from functools import wraps
from math import atan2, sin, cos, radians, pi
from random import Random

from .helper import comma, hopposite, direction_names, remove_trailing_numbers, random_list
from .Obj import Obj, OBJECT, overlap_loss, door_loss, X, Y, BOUND, STANDING, MOUNTED, FLOATING
from .Relation import Relation, RELATION, relation_table
from .Vec import Vec, best_dir
from .exceptions import ERROR, Error
from .Settings import Settings
from .logger import info, warning, critical

object_type_names = ['OBJECT', 'WALL', 'FLOOR', 'DOOR', 'WINDOW', 'SCENE']

class RandomWrapper:
    def __call__(self):
        return random.random()
    def __getattr__(self, attr):
        return getattr(random, attr)

safe_builtins = {
    "abs": abs,
    "all": all,
    "any": any,
    "bin": bin,
    "bool": bool,
    "chr": chr,
    "divmod": divmod,
    "enumerate": enumerate,
    "filter": filter,
    "float": float,
    "format": format,
    "int": int,
    "isinstance": isinstance,
    "issubclass": issubclass,
    "len": len,
    "list": list,
    "map": map,
    "max": max,
    "min": min,
    "next": next,
    "ord": ord,
    "pi": pi,
    "pow": pow,
    "range": range,
    "reversed": reversed,
    "round": round,
    "slice": slice,
    "sorted": sorted,
    "str": str,
    "sum": sum,
    "tuple": tuple,
    "zip": zip,
    "print": print,
 }

class Scene(Obj):
    objs: list[Obj]
    floor_asset: str
    wall_asset: str
    floor_color: str | None
    wall_color: str | None
    title: str
    errors: list[Error]
    coordinate_frame: Obj
    rng: Random | None
    group_names: list[tuple[str, OBJECT]]
    relations: list[Relation]
    interior: bool
    errors_encountered: bool # довольно странно, как именно мы это используем?
    error_free_code: str
    problematic_objects: list[bool]
    problematic_rot_objects: list[bool]
    number_of_corrections: int

    mapping: list[int] | None
    constant_vec: list[float] | None
    consult_vec: list[int | None] | None

    def __init__(self, name: str, source_code: str, env_code: str, seed: int | None, mapping: list[int] | None, constant_vec: list[float] | None, consult_vec: list[int | None] | None):
        self.name = name
        self.title = name
        self.objs = []
        self.floor_asset = 'floor'
        self.wall_asset = 'wall'
        self.floor_color = None
        self.wall_color = None
        self.errors = []
        self.coordinate_frame = self
        self.rng = None if seed is None else Random(seed)
        self.group_names = []
        self.mapping = mapping
        self.constant_vec = constant_vec
        self.consult_vec = consult_vec
        self.relations = []
        self.interior = True
        self.errors_encountered = False
        self.number_of_corrections = 0
        self.error_free_code = "NOCODE"
        super().__init__(self, name, OBJECT.SCENE, 6.0, 6.0, 3.0, 1, STANDING, None, False)
        self.soft_exec(source_code, env_code)
        for o in self.objs:
            o.finalize()
        self.calculate_relations()


    def soft_exec(self, scene_code: str, env_code: str) -> None:
        env_line_count = env_code.count('\n')
        lines = scene_code.split('\n')
        #for i, line in enumerate(lines):
        #    print(f"{i}. {line}")
        while len(lines) > 0:
            try:
                safe_globals = {
                    "__builtins__": safe_builtins,  # Disable all built-in functions by default
                    "math": math,
                    "random": RandomWrapper(),
                    "wraps": wraps,
                    "atan2": atan2,
                    "cos": cos,
                    "pi": pi,
                    "radians": radians,
                    "sin": sin,

                    "ERROR": ERROR,
                    "remove_trailing_numbers": remove_trailing_numbers,
                    "OBJECT": OBJECT,
                    "Obj": Obj,
                    "Scene": Scene,
                    "Settings": Settings,
                    "Vec": Vec,
                    "scene": self,
                    "CENTER": self,

                    "STANDING": STANDING,
                    "MOUNTED": MOUNTED,
                    "FLOATING": FLOATING,
                }
                join = '\n'.join(lines)
                total_code = env_code + join
                self.objs.clear()
                self.group_names.clear()
                exec(total_code, safe_globals)
                self.error_free_code = join
                break
            except Exception as e:
                info(f"\nError encountered: <{e}>")
                info(f"<<<\n{traceback.format_exc()}>>>")
                self.errors_encountered = True
                error_line_number = None
                if isinstance(e, (SyntaxError, IndentationError)):
                    error_line_number = e.lineno - 1 - env_line_count if e.lineno is not None else None
                    info(f"Removing bad indentation line {e.lineno}-1-{env_line_count} = {error_line_number}: <{lines[error_line_number]}>")
                else:
                    tb = traceback.extract_tb(e.__traceback__)
                    for frame in tb:
                        info(f"frame.filename = {frame.filename}")
                        if frame.filename == "<string>":
                            error_line_number = frame.lineno - 1 - env_line_count
                            info(f"Removing problematic line {error_line_number}={frame.lineno}-1-{env_line_count}: <{lines[error_line_number]}>")
                            break
                if error_line_number is None:
                    info("error not in exec() code, stopping")
                    break
                lines.pop(error_line_number)
            if len(lines) == 0:
                info("all lines removed, no valid code remaining")



    def llm_error(self, etype: ERROR, message: str) -> None:
        if etype == ERROR.PYTHON:
            if "is not defined" in message:
                etype = ERROR.HALLUCINATION
        warning(f"llm_error: {Error.legend[etype]}: {message}")
        if type != ERROR.WARNING:
            self.errors.append(Error(etype, message))


    def smin(self) -> Vec:
        return Vec(-0.5 * self.width, -0.5 * self.depth, 0.0)
    def smax(self) -> Vec:
        return Vec(0.5 * self.width, 0.5 * self.depth, self.height)

    def inbound_loss(self, omin: Vec, omax: Vec) -> float:
        smin, smax = self.smin(), self.smax()
        result = max(smin.x - omin.x, smin.y - omin.y, smin.z - omin.z, omax.x - smax.x, omax.y - smax.y)
        return max(result, omax.z - smax.z) if self.interior else result

    # лол, я тут не рассматриваю землю как саппорт
    def standing_loss(self, a: Obj) -> float:
        amin_z = a.fmin().z
        if abs(amin_z) < 0.01:
            return 0.0
        min_loss = abs(amin_z)
        for b in self.objs:
            bmin = b.fmin()
            bmax = b.fmax()
            z_loss = abs(amin_z - bmax.z)
            min_x = max(bmin.x - a.fcenter.x, 0.0)
            max_x = max(a.fcenter.x - bmax.x, 0.0)
            min_y = max(bmin.y - a.fcenter.y, 0.0)
            max_y = max(a.fcenter.y - bmax.y, 0.0)
            loss = z_loss + min_x + max_x + min_y + max_y
            if loss < 0.01:
                return 0.0
            if loss < min_loss:
                min_loss = loss
        return min_loss

    def mounted_loss(self, o: Obj) -> float:
        omin = o.fmin()
        omax = o.fmax()
        smin = self.fmin()
        smax = self.fmax()
        if o.size.x > o.size.y:
            return min(abs(omin.y - smin.y), abs(smax.y - omax.y))
        elif o.size.x < o.size.y:
            return min(abs(omin.x - smin.x), abs(smax.x - omax.x))
        else:
            return min(abs(omin.x - smin.x), abs(smax.x - omax.x), abs(omin.y - smin.y), abs(smax.y - omax.y))
        # сейчас тут просто минимальное расстояние до стены. А нельзя ли не по всем стенам брать минимум, а только по соответствующим широкой стороне?

    def calculate_relations(self) -> None:
        self.relations.clear()
        self.problematic_objects = [False for _ in self.objs]
        self.problematic_rot_objects = [False for _ in self.objs]
        for i, o in enumerate(self.objs):
            ob_loss = int(250.0 * self.inbound_loss(o.fmin(), o.fmax())) #200
            if ob_loss > 0:
                rel = Relation(RELATION.OUT_OF_BOUNDS, [i], ob_loss)
                self.relations.append(rel)
                self.problematic_objects[i] = True
                self.problematic_rot_objects[i] = True

            for j in range(0, i):
                o2 = self.objs[j]
                ol_loss = int(100.0 * overlap_loss(o, o2))
                if ol_loss > 0:
                    rel = Relation(RELATION.OVERLAP, [i, j], ol_loss)
                    self.relations.append(rel)
                    self.problematic_objects[i] = True
                    self.problematic_objects[j] = True
                    self.problematic_rot_objects[i] = True
                    self.problematic_rot_objects[j] = True

            """
            if Settings.SUPPORTING_SURFACE_ENABLED:
                if isinstance(o.supporting_surface, Obj):
                    support: Obj = o.supporting_surface
                    j = self.objs.index(support)
                    floss = max(support.fmin().x - o.fcenter.x, 0.0) + max(o.fcenter.x - support.fmax().x, 0.0) + max(support.fmin().y - o.fcenter.y, 0.0) + max(o.fcenter.y - support.fmax().y, 0.0)
                    air_loss = int(100.0 * floss)
                    if air_loss > 0:
                        rel = Relation(RELATION.AIR, [i, j], air_loss)
                        self.relations.append(rel)
                        self.problematic_objects[i] = True
                        self.problematic_rot_objects[j] = True
                    z_loss = int(100.0 * max(o.fmin().z - support.fmax().z, 0.0))
                    if z_loss > 0:
                        rel = Relation(RELATION.Z2, [i, j], z_loss)
                        self.relations.append(rel)
                        self.problematic_objects[i] = True
                    if o.direction != support.direction and o.directed and support.directed:
                        l1 = o.size.max_component()
                        l2 = support.size.max_component()
                        loss = max(int(min(l1, l2)), 10)
                        rel = Relation(RELATION.BAD_TOWER, [i, j], loss)
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                        self.problematic_rot_objects[j] = True
                elif o.supporting_surface == GROUND and o.fmin().z > 0.0:
                    rel = Relation(RELATION.Z1, [i], int(100.0 * o.fmin().z))
                    self.relations.append(rel)
                    self.problematic_objects[i] = True
            """
            if o.support == STANDING:
                st_int_loss = int(100.0 * self.standing_loss(o))
                if st_int_loss > 0:
                    self.relations.append(Relation(RELATION.STANDING, [i], st_int_loss))
                    self.problematic_objects[i] = True # на самом деле все объекты являются проблемными, если есть хоть один standing_loss. Ну что ж
                    self.problematic_rot_objects[i] = True
            elif o.support == MOUNTED:
                mounted_int_loss = int(100.0 * self.mounted_loss(o))
                if mounted_int_loss > 0:
                    self.relations.append(Relation(RELATION.MOUNTED, [i], mounted_int_loss))
                    self.problematic_objects[i] = True
                    self.problematic_rot_objects[i] = True

            if isinstance(o.mem_facing, Obj):
                if o.direction != best_dir(o.fcenter, o.mem_facing.fcenter, o.mem_facing.size):
                    rel = Relation(RELATION.FACING_SCENE, [i], 1) if o.mem_facing.otype == OBJECT.SCENE else Relation(RELATION.FACING, [i, self.objs.index(o.mem_facing)], 1)
                    self.relations.append(rel)
                    self.problematic_rot_objects[i] = True

            if o.otype == OBJECT.DOOR or o.otype == OBJECT.WINDOW:
                for j in range(0, len(self.objs)):
                    o2 = self.objs[j]
                    if j == i or o2.is_rug():
                        continue
                    ol_loss = int(50.0 * door_loss(o, o2, 0.5 * o.width if o.otype == OBJECT.DOOR else min(0.25 * o.width, 0.4)))
                    if ol_loss > 0:
                        rel = Relation(RELATION.DOOR, [i, j], ol_loss)
                        self.relations.append(rel)
                        self.problematic_objects[i] = True
                        self.problematic_objects[j] = True
                        #self.problematic_rot_objects[i] = True
                        self.problematic_rot_objects[j] = True

            nexttowalls = [False, False, False, False]
            #any_ntw = False
            for r in o.relations:
                if r.btype == BOUND.MAX and r.axis == X and abs(o.fmax().x - self.fmax().x) < 0.05: #abs(r.value - 0.5 * self.width) <= o.size.x: # лол! Это может быть баунд вообще с другим объектом!
                    nexttowalls[0] = True
                    #any_ntw = True
                #if r.btype == BOUND.MAX and r.axis == Y and abs(r.value - 0.5 * self.depth) <= o.size.y:
                if r.btype == BOUND.MAX and r.axis == Y and abs(o.fmax().y - self.fmax().y) < 0.05:
                    nexttowalls[1] = True
                    #any_ntw = True
                #if r.btype == BOUND.MIN and r.axis == X and abs(r.value + 0.5 * self.width) <= o.size.x:
                if r.btype == BOUND.MIN and r.axis == X and abs(o.fmin().x - self.fmin().x) < 0.05:
                    nexttowalls[2] = True
                    #any_ntw = True
                #if r.btype == BOUND.MIN and r.axis == Y and abs(r.value + 0.5 * self.depth) <= o.size.y:
                if r.btype == BOUND.MIN and r.axis == Y and abs(o.fmin().y - self.fmin().y) < 0.05:
                    nexttowalls[3] = True
                    #any_ntw = True
            #if Settings.SUPPORTING_SURFACE_ENABLED and (o.supporting_surface == RIGHT_WALL or o.supporting_surface == TOP_WALL or o.supporting_surface == LEFT_WALL or o.supporting_surface == BOTTOM_WALL):
            #    nexttowalls[o.supporting_surface] = True
            #    any_ntw = True

            #if o.fmin().z > 0.1: # mounted objects should touch the wall with their backs
            #    if any_ntw and not nexttowalls[(o.direction + 2) % 4]:
            #        rel = Relation(RELATION.SHORT_SIDE_TO_WALL, [i], 500)
            #        self.relations.append(rel)
            #        self.problematic_rot_objects[i] = True
            if o.directed and o.direction != o.mem_facing:
                if nexttowalls[o.direction]:
                    self.relations.append(Relation(RELATION.FACING_WALL, [i], 1))
                    self.problematic_rot_objects[i] = True
                coefficient = 100.0 if o.support == MOUNTED else 10.0
                rel = Relation(RELATION.SHORT_SIDE_TO_WALL, [i], max(int(coefficient * o.size.max_component()), 1))
                if nexttowalls[0] and not nexttowalls[1] and not nexttowalls[2] and not nexttowalls[3]:
                    if (o.direction == 1 or o.direction == 3) and o.width >= o.depth:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                    if (o.direction == 0 or o.direction == 2) and o.depth > 2.0 * o.width:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                elif nexttowalls[2] and not nexttowalls[0] and not nexttowalls[1] and not nexttowalls[3]:
                    if (o.direction == 1 or o.direction == 3) and o.width >= o.depth:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                    if (o.direction == 0 or o.direction == 2) and o.depth > 2.0 * o.width:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                elif nexttowalls[3] and not nexttowalls[0] and not nexttowalls[1] and not nexttowalls[2]:
                    if (o.direction == 0 or o.direction == 2) and o.width >= o.depth:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                    if (o.direction == 1 or o.direction == 3) and o.depth > 2.0 * o.width:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                elif nexttowalls[1] and not nexttowalls[0] and not nexttowalls[2] and not nexttowalls[3]:
                    if (o.direction == 0 or o.direction == 2) and o.width >= o.depth:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True
                    if (o.direction == 1 or o.direction == 3) and o.depth > 2.0 * o.width:
                        self.relations.append(rel)
                        self.problematic_rot_objects[i] = True

            if o.is_frame:
                self.problematic_rot_objects[i] = True



    def random_position(self, width: float, depth: float, height: float) -> Vec:
        if width >= self.width or depth >= self.depth:
            return Vec(0, 0, 0.5 * height)
        rx = self.rng.uniform(self.fmin().x + 0.5 * width, self.fmax().x - 0.5 * width)
        ry = self.rng.uniform(self.fmin().y + 0.5 * depth, self.fmax().y - 0.5 * depth)
        return Vec(rx, ry, 0.5 * height)

    """
    def best_position(self, width: float, depth: float, height: float) -> Vec: # квадратичная функция от количества объектов!
        smin, smax = self.fmin(), self.fmax()
        min_loss = 1000000.0
        x_min, y_min = -100.0, -100.0
        y = smin.y
        while y < smax.y:
            x = smin.x
            while x < smax.x:
                min1 = Vec(x, y, 0.0)
                max1 = Vec(x + width, y + depth, height)
                total_loss = self.inbound_loss(min1, max1) + sum(overlap_loss_xy(min1, max1, o) for o in self.objs if o.size is not None)
                if total_loss == 0.0:
                    return Vec(x + 0.5 * width, y + 0.5 * depth, 0.5 * height)
                elif total_loss < min_loss:
                    x_min, y_min = x, y
                    min_loss = total_loss
                x += 0.1
            y += 0.1
        return Vec(x_min + 0.5 * width, y_min + 0.5 * depth, 0.5 * height)
    """


    def all_objects(self) -> list[Obj]:
        #DELETE_CEILING_OBJECTS = Settings.POST_POLISH
        DELETE_OUT_OF_BOUNDS = Settings.POST_POLISH
        DELETE_COVERED_OBJECTS = False
        DELETE_GIANT_OBJECTS = False
        DELETE_AIR_OBJECTS = Settings.POST_POLISH
        DELETE_EXTERIOR_WINDOWS = Settings.POST_POLISH

        good_objects = []
        for o in self.objs:
            #if DELETE_CEILING_OBJECTS and o.mounted_on_ceiling():
            #    self.llm_error(ERROR.WARNING, f"deleting a ceiling object {o}")
            #    continue
            if DELETE_COVERED_OBJECTS and o.covered():
                self.llm_error(ERROR.WARNING, f"deleting a covered object {o}")
                continue
            if DELETE_OUT_OF_BOUNDS and o.completely_out_of_bounds():
                self.llm_error(ERROR.WARNING, f"deleting a completely-out-of-bounds object {o}")
                continue
            if DELETE_GIANT_OBJECTS and o.fmin().z > 0.4 and o.width * o.depth > 0.5 * self.width * self.depth:
                self.llm_error(ERROR.WARNING, f"deleting a giant object {o}")
                continue
            if DELETE_AIR_OBJECTS and o.support == STANDING and o.height_above_support() > 0.5 * o.height:
                self.llm_error(ERROR.WARNING, f"deleting an air object {o}")
                continue
            if DELETE_EXTERIOR_WINDOWS and not self.interior and o.otype == OBJECT.WINDOW:
                self.llm_error(ERROR.WARNING, f"deleting an exterior window {o}")
                continue
            good_objects.append(o)

        result = []
        for o in good_objects:
            result.append(o)

        floor = Obj(self, self.floor_asset, OBJECT.FLOOR, self.size.x, self.size.y, Settings.FLOOR_THICKNESS, 1, STANDING, self.floor_color, False)
        floor.fcenter = Vec(0, 0, -Settings.FLOOR_THICKNESS / 2)
        result.append(floor)

        # Более тонкая настройка: стена не ставится, если объект уже висит более широкой стороной на другой стене. Наверняка это можно элегантно выразить.
        walls = [False, False, False, False]
        if Settings.ALL_WALLS:
            if self.interior:
                walls = [True, True, True, True]
        else:
            EPS = 0.02
            for o in good_objects:
                if o.fmin().z < EPS and o.otype == OBJECT.OBJECT: # нужно смотреть только на те объекты, которые висят в воздухе, а не на все вторичные объекты. Но и так неплохо
                    continue
                #if Settings.SUPPORTING_SURFACE_ENABLED and (o.mem_supporting_surface == RIGHT_WALL or o.mem_supporting_surface == TOP_WALL or o.mem_supporting_surface == LEFT_WALL or o.mem_supporting_surface == BOTTOM_WALL):
                #    walls[o.mem_supporting_surface] = True

        for d in range(4):
            if walls[d]:
                result.append(self.wall(d))
        return result


    def wall(self, d: int) -> Obj:
        w = self.depth if d % 2 == 0 else self.width
        h = self.height + Settings.FLOOR_THICKNESS
        wall = Obj(self, self.wall_asset, OBJECT.WALL, w, Settings.WALL_THICKNESS, h, hopposite[d], STANDING, self.wall_color, False)
        Z = 0.5 * (self.height - Settings.FLOOR_THICKNESS)
        if d == 0:
            wall.fcenter = Vec(self.fmax().x + 0.5 * Settings.WALL_THICKNESS, self.fcenter.y, Z)
        elif d == 1:
            wall.fcenter = Vec(self.fcenter.x, self.fmax().y + 0.5 * Settings.WALL_THICKNESS, Z)
        elif d == 2:
            wall.fcenter = Vec(self.fmin().x - 0.5 * Settings.WALL_THICKNESS, self.fcenter.y, Z)
        else:
            wall.fcenter = Vec(self.fcenter.x, self.fmin().y - 0.5 * Settings.WALL_THICKNESS, Z)
        return wall


    def filled_area(self) -> float:
        #return sum(o.width * o.depth for o in self.objs if not isinstance(o.mem_supporting_surface, Obj) and not o.is_rug())
        return sum(o.width * o.depth for o in self.objs if o.fmin().z <= 0.01 and not o.is_rug())
    def fill_percentage(self) -> float:
        return self.filled_area() / (self.width * self.depth)
    def max_object_length(self) -> float:
        max_length = -1.0
        for o in self.objs:
            if o.width > max_length:
                max_length = o.width
            if o.depth > max_length:
                max_length = o.depth
        return max_length

    def json(self) -> str:
        tiles_x = min(max(math.ceil(Settings.MIN_SIZE / self.size.x), 1), Settings.MAX_TILES)
        tiles_y = min(max(math.ceil(Settings.MIN_SIZE / self.size.y), 1), Settings.MAX_TILES)
        hhscene = HHScene(self.title, self.size, self.all_objects(), self.interior, tiles_x, tiles_y, self.rng)
        return hhscene.json(self.relations, len(self.constant_vec), int(100.0 * self.fill_percentage()))

    def python(self) -> str:
        support_names = ["STANDING", "MOUNTED", "FLOATING"]
        result = f'set_title("{self.title}")\n'
        result += f'set_size({self.size.x}, {self.size.y}, {self.size.z})\n'
        result += f'set_floor_asset("{self.floor_asset}", color="{self.floor_color}")\n'
        result += f'set_wall_asset("{self.wall_asset}", interior={self.interior}, color="{self.wall_color}")\n\n'
        for i, o in enumerate(self.objs):
            name = f'o{i}'
            typename = "Object"
            if o.otype == OBJECT.DOOR:
                typename = "Door"
            elif o.otype == OBJECT.WINDOW:
                typename = "Window"
            result += f'{name} = {typename}("{o.name}", {o.width}, {o.depth}, {o.height}, support={support_names[o.support]}, color="{o.color}")\n'
            result += f'{name}.center.x = {o.fcenter.x}\n'
            result += f'{name}.center.y = {o.fcenter.y}\n'
            result += f'{name}.center.z = {o.fcenter.z}\n'
            result += f'{name}.facing = {o.facing}\n\n'
        return result


def mark_as_near_wall(near_walls: list[bool], i: int, objs: list[Obj]) -> None:
    near_walls[i] = True
    for j, o in enumerate(objs):
        if not near_walls[j]:
            if objs[j].above(objs[i]):
                near_walls[j] = True
                #mark_as_near_wall(near_walls, j, objs)



class HHScene:
    title: str
    size: Vec
    objs: list[Obj]

    def __init__(self, title: str, size: Vec, objs: list[Obj], interior: bool, MX: int, MY: int, rng: Random):
        for o in objs:
            if o.dynamic:
                if o.is_tall() or o.is_flat() or o.support == MOUNTED or o.support == FLOATING:
                    o.dynamic = False
            if o.dynamic:
                for q in objs:
                    if q != o and q.on(o) and not q.dynamic:
                        o.dynamic = False
                        break

        self.title = title
        self.size = Vec(MX * size.x, MY * size.y, size.z)

        symmetries = random_list(MX * MY, 8 if size.x == size.y else 4, rng)
        near_walls = [[False for _ in objs] for _ in range(4)]
        for i, o in enumerate(objs):
            if o.otype == OBJECT.WALL or o.otype == OBJECT.FLOOR:
                continue
            if not interior and o.otype == OBJECT.OBJECT:
                continue
            if o.fmax().x + 0.01 > 0.5 * size.x:
                mark_as_near_wall(near_walls[0], i, objs)
                #print(f"{o} is near wall {0}")
            if o.fmax().y + 0.01 > 0.5 * size.y:
                mark_as_near_wall(near_walls[1], i, objs)
                #print(f"{o} is near wall {1}")
            if o.fmin().x - 0.01 < -0.5 * size.x:
                mark_as_near_wall(near_walls[2], i, objs)
                #print(f"{o} is near wall {2}")
            if o.fmin().y - 0.01 < -0.5 * size.y:
                mark_as_near_wall(near_walls[3], i, objs)
                #print(f"{o} is near wall {3}")

        self.objs = []
        permutations = [[0, 1, 2, 3], [2, 1, 0, 3], [0, 3, 2, 1], [2, 3, 0, 1], [3, 0, 1, 2], [1, 2, 3, 0], [3, 2, 1, 0], [1, 0, 3, 2]] # перестановки во второй половине могут быть ещё и обратные
        for i, o in enumerate(objs):
            cox = o.fcenter.x + 0.5 * size.x
            coy = o.fcenter.y + 0.5 * size.y
            for t in range(len(symmetries)):
                mx, my = t % MX, t // MX
                s = symmetries[t]
                perm = permutations[s]
                q = Obj(None, o.name, o.otype, o.width, o.depth, o.height, o.direction, o.support, o.color, o.dynamic)
                if s == 0:
                    sx = cox
                    sy = coy
                elif s == 1:
                    sx = size.x - cox
                    sy = coy
                    if q.direction % 2 == 0:
                        q.direction = (q.direction + 2) % 4
                elif s == 2:
                    sx = cox
                    sy = size.y - coy
                    if q.direction % 2 == 1:
                        q.direction = (q.direction + 2) % 4
                elif s == 3:
                    sx = size.x - cox
                    sy = size.y - coy
                    q.direction = (q.direction + 2) % 4
                elif s == 4:
                    sx = -o.fcenter.y + 0.5 * size.x
                    sy = o.fcenter.x + 0.5 * size.y
                    q.direction = (q.direction + 1) % 4
                elif s == 5:
                    sx = o.fcenter.y + 0.5 * size.x
                    sy = -o.fcenter.x + 0.5 * size.y
                    q.direction = (q.direction + 3) % 4
                elif s == 6:
                    sx = -o.fcenter.y + 0.5 * size.x
                    sy = -o.fcenter.x + 0.5 * size.y
                    q.direction = 3 - q.direction
                elif s == 7:
                    sx = coy
                    sy = cox
                    q.direction = q.direction + 1 if q.direction % 2 == 0 else q.direction - 1
                else:
                    raise Exception("should not happen")
                q.size = Vec(q.depth, q.width, q.height) if q.direction % 2 == 0 else Vec(q.width, q.depth, q.height)
                q.fcenter.x = sx + mx * size.x
                q.fcenter.y = sy + my * size.y
                q.fcenter.z = o.fcenter.z

                if q.otype == OBJECT.WALL:
                    present = False
                    if mx == 0 and q.direction == 0:
                        present = True
                    if mx == MX - 1 and q.direction == 2:
                        present = True
                    if my == 0 and q.direction == 1:
                        present = True
                    if my == MY - 1 and q.direction == 3:
                        present = True
                elif q.otype == OBJECT.FLOOR:
                    present = True
                else:
                    present = True
                    if interior or q.otype == OBJECT.DOOR or q.otype == OBJECT.WINDOW:
                        if mx > 0 and near_walls[perm[2]][i]:
                            present = False
                        if mx < MX - 1 and near_walls[perm[0]][i]:
                            present = False
                        if my > 0 and near_walls[perm[3]][i]:
                            present = False
                        if my < MY - 1 and near_walls[perm[1]][i]:
                            present = False

                if present:
                    self.objs.append(q)

        for o in self.objs:
            o.fcenter.x -= 0.5 * self.size.x
            o.fcenter.y -= 0.5 * self.size.y
        self.size = self.size.flip_yz()
        for o in self.objs:
            o.size = o.size.flip_yz()
            o.fcenter = o.fcenter.flip_yz_minus()



    def json(self, relations: list[Relation], num_constants: int, fill_percentage: int) -> str:
        support_names = ["STANDING", "MOUNTED", "FLOATING"]
        result = '{\n'
        result += f'  "name": "{self.title}",\n'
        result += f'  "size": {self.size.json()},\n'
        result += f'  "number_of_constants": {num_constants},\n'
        result += f'  "fill_percentage": {fill_percentage},\n'
        result += '  "objects":\n'
        result += '  [\n'
        for i, o in enumerate(self.objs):
            if o.size is None:
                critical(f"ERROR: {o} has no size")
            result += f'    {{ "name": "{o.name}", "type": "{object_type_names[o.otype.value]}", "size": {o.size.json()}, "position": {o.fcenter.json()}'
            result += f', "physics": { 2 if o.dynamic else 1 }, "support": "{support_names[o.support]}"'
            if o.color is not None:
                result += f', "color": "{o.color}"'
            if o.direction is not None and o.directed:
                result += f', "facing": "{direction_names[o.direction]}"'
            result += f' }}{comma(i, self.objs)}\n'
        result += '  ],\n'
        result += '  "relations":\n'
        result += '  [\n'
        sorted_relations = sorted(relations, key=lambda r: r.loss, reverse=True)
        for i, rel in enumerate(sorted_relations):
            data = relation_table[rel.rtype.value]
            result += f'    {{ "name": "{data.name}", "arity": "{data.arity}", "args": {json.dumps(rel.args)}, "loss": {rel.loss:.4f}'
            result += f' }}{comma(i, relations)}\n'
        result += '  ]\n'
        result += '}\n'
        return result
