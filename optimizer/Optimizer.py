# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

import math
import random

from .helper import lerp, wrap_constants, intersect, merge, remove_markdown, remove_imports #, make_list_access_safe
from .Vec import Vec
from .Obj import Obj
from .Scene import Scene
from .exceptions import ERROR
from .Settings import Settings, MODE
from .logger import info, debug

#FIXED_MULTIPLIERS = [-1.0, 1.25, 0.75, 1.5, 0.5, 2.0, 3.0, 0.25, 4.0]
#FIXED_MULTIPLIERS = [1.25, 0.75, 1.5, 0.5, 2.0, -1.0, 3.0, 6.0]
#FIXED_MULTIPLIERS = [1.25, 0.75, 1.5, 0.5, 1.75, 2.0, -0.5, -1.0, 0.25, 2.5, 3.0, 4.0, 5.0, 6.0, -6.0, 0.768, -0.768]
#FIXED_MULTIPLIERS = [0.5, 1.75]
FIXED_MULTIPLIERS = [1.25, 0.75, 1.1, 0.85, 1.5, 0.5, 1.75, 2.0, -0.5, -1.0, 0.25, 2.5, 3.0, 4.0, 5.0, 6.0, -6.0, 0.768, -0.768]

def compute_cost(scene: Scene, prev_scene: Scene) -> float:
    if not Settings.OPTIMAL_TRANSPORT:
        total = 0.0
        for i, o in enumerate(scene.objs):
            total += o.size.volume() * (o.fcenter - prev_scene.objs[i].fcenter).length()
        return total

    total = 0.0
    current = {}
    previous = {}
    for idx, o in enumerate(scene.objs):
        current.setdefault(o.name, []).append(idx)
    for idx, o in enumerate(prev_scene.objs):
        previous.setdefault(o.name, []).append(idx)

    for name in current.keys() & previous.keys():
        cur_indices = current[name]
        prev_indices = previous[name]
        pairs = []
        for i in cur_indices:
            oi = scene.objs[i]
            for j in prev_indices:
                oj = prev_scene.objs[j]
                cost = oi.size.volume() * (oi.fcenter - oj.fcenter).length()
                pairs.append((cost, i, j))
        if not pairs:
            continue
        pairs.sort(key=lambda x: x[0])
        used_cur = set()
        used_prev = set()
        for cost, i, j in pairs:
            if i in used_cur or j in used_prev:
                continue
            total += cost
            used_cur.add(i)
            used_prev.add(j)
            if len(used_cur) == len(cur_indices) or len(used_prev) == len(prev_indices):
                break
    return total

def outofbounds_gradient(a: Obj, smin: Vec, smax: Vec):
    result = (a.fmax() - smax).relu() - (smin - a.fmin()).relu()
    result.z = 0.0
    return result

def outofbounds_loss(a: Obj, smin: Vec, smax: Vec) -> float:
    xmin = max(smin.x - a.fmin().x, 0.0)
    ymin = max(smin.y - a.fmin().y, 0.0)
    xmax = max(a.fmax().x - smax.x, 0.0)
    ymax = max(a.fmax().y - smax.y, 0.0)
    return xmin * xmin + ymin * ymin + xmax * xmax + ymax * ymax

def overlap_gradient(a: Obj, b: Obj) -> Vec:
    diff = b.fcenter - a.fcenter
    length = diff.length()
    #if length < 0.001:
    #    return Vec(0, 0, 0)
    result: Vec = 4.0 * (Vec.min(a.fmax(), b.fmax()) - Vec.max(a.fmin(), b.fmin())).relu().min_component() / length * diff
    #length = result.length()
    #if length > 0.001:
    #    result += 0.02 * length * Vec.random_vec(rng)
    result.z = 0.0
    return 0.625 * result

def overlap_loss(a: Obj, b: Obj) -> float:
    return 0.625 * 4.0 * (Vec.min(a.fmax(), b.fmax()) - Vec.max(a.fmin(), b.fmin())).relu().min_component()

def build_multipliers(rng: random.Random) -> list[float]:
    return FIXED_MULTIPLIERS if Settings.FIXED_MULTIPLIERS else [rng.choice([-1.0, 1.0]) * math.pow(4.0, rng.uniform(-1.0, 1.0)) for _ in range(10)]

def gradient_step(scene: Scene) -> None:
    gradient = [Vec(0, 0, 0) for _ in scene.objs]
    for i, a in enumerate(scene.objs):
        gradient[i] += outofbounds_gradient(a, scene.fmin(), scene.fmax())
        for j in range(i):
            b = scene.objs[j]
            og = overlap_gradient(a, b)
            gradient[i] += og
            gradient[j] -= og
    for i, o in enumerate(scene.objs):
        o.fcenter -= 0.05 * gradient[i]

def loss(scene: Scene) -> float:
    result = 0
    for i, a in enumerate(scene.objs):
        result += outofbounds_loss(a, scene.fmin(), scene.fmax())
        for j in range(i):
            b = scene.objs[j]
            result += overlap_loss(a, b)
    return result



class Optimizer:
    basename: str | None
    safe_code: str
    env_code: str
    output_folder: str
    num_constructors: int
    mapping: list[int]
    original_constants: list[float]
    seed: int
    table: list[list[bool]]
    group_table: list[list[bool]]
    rng: random.Random

    def __init__(self, basename: str | None, env_code: str, output_folder: str):
        self.basename = basename
        self.env_code = env_code
        self.output_folder = output_folder


    def run(self, llm_code: str) -> Scene | None:
        #print("LLM code:")
        #print(llm_code)
        llm_code = remove_markdown(llm_code)
        llm_code = remove_imports(llm_code)
        llm_code = llm_code.replace("while True:", "for _ in range(18):")
        #llm_code = make_list_access_safe(llm_code)

        self.seed = random.randint(0, 999) if Settings.SEED is None else Settings.SEED
        self.rng = random.Random(self.seed)
        if self.basename is not None:
            info(f"\nseed = {self.seed}")
        prelim_scene = Scene(self.basename, llm_code, self.env_code, self.seed, None, None, None)
        if len(prelim_scene.objs) == 0:
            prelim_scene.llm_error(ERROR.FATAL, f"scene '{self.basename}' has no objects, {Settings.MODEL}, and thus failed completely")
            return None
        if self.basename is None:
            return prelim_scene

        self.safe_code, raw_constants = wrap_constants(prelim_scene.error_free_code)
        self.mapping, self.original_constants = merge(raw_constants) if Settings.MERGE_CONSTANTS else ([i for i in range(len(raw_constants))], raw_constants)

        original_scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, self.original_constants, None)
        original_loss = sum(rel.loss for rel in original_scene.relations)

        self.num_constructors = len(original_scene.group_names)
        original_num_errors = len(original_scene.relations)
        info(f"original number of errors = {original_num_errors}, original loss = {original_loss}")
        info(f"num_constructors = {self.num_constructors}")
        info(f"group_names = {original_scene.group_names}")

        original_scene.consult_vec = [None for _ in range(self.num_constructors)]
        scenes = [original_scene]
        common_scene_name = f"{self.output_folder}/" + (f"(!)-" if prelim_scene.errors_encountered else "") + original_scene.name

        if Settings.GRADIENT_DESCENT:
            info(f"running gradient descent...")
            max_gradient_steps = 200
            frame_interval = None
            frames_recorded = 0
            if Settings.ANIMATION_FRAMES > 0:
                frame_interval = 1
                original_scene.calculate_relations()
                with open(f"{common_scene_name}-gd0.json", 'w') as file:
                    file.write(original_scene.json())
                frames_recorded = 1
            for i, a in enumerate(original_scene.objs):
                for j in range(i):
                    b = original_scene.objs[j]
                    if abs(a.fcenter.x - b.fcenter.x) + abs(a.fcenter.y - b.fcenter.y) < 0.02:
                        debug(f"{a} and {b} had the same location, pushing")
                        b.fcenter.x += original_scene.rng.uniform(-0.1, 0.1)
                        b.fcenter.y += original_scene.rng.uniform(-0.1, 0.1)
            for n in range(max_gradient_steps):
                gradient_step(original_scene)
                if n % 100 == 0:
                    l = loss(original_scene)
                    if l <= 0.001:
                        info(f"zero loss after {n} gradient descent steps")
                        break
                    else:
                        info(f"loss = {l}")
                if frame_interval is not None and (n + 1) % frame_interval == 0:
                    original_scene.calculate_relations()
                    with open(f"{common_scene_name}-gd{n + 1}.json", 'w') as file:
                        file.write(original_scene.json())
                    frames_recorded += 1
            original_scene.calculate_relations()
        elif (Settings.SEARCH_ORIENTATIONS or Settings.SEARCH_CONSTANTS) and Settings.MODE in [MODE.RUN_FULL_SCENE, MODE.RUN_FULL_LAYOUT, MODE.RUN_COORD_LAYOUT, MODE.CHAIN] and original_num_errors > 0:
            info(f"{len(raw_constants)}    raw constants: {raw_constants}")
            info(f"{len(self.original_constants)} merged constants: {self.original_constants}")
            info(f"mapping of length {len(self.mapping)}: {self.mapping}")
            if Settings.SEARCH_CONSTANTS:
                self.compute_change_table(original_scene)
            if Settings.SEARCH_ORIENTATIONS:
                self.compute_group_table(original_scene)
            current = original_scene
            counter = 0
            while True:
                current = self.descent(current)
                counter += 1
                if current is None:
                    break
                current.number_of_corrections = counter
                scenes.append(current)
                if len(current.relations) == 0:
                    break

        FRAMES = Settings.ANIMATION_FRAMES
        if len(scenes) == 1:
            if Settings.SAVE_JSON:
                with open(f"{common_scene_name}-{self.seed}.json", 'w') as file:
                    file.write(original_scene.json())
            if Settings.SAVE_PYTHON:
                with open(f"{common_scene_name}-{self.seed}.py", 'w') as file:
                    file.write(original_scene.python())
            return original_scene
        elif FRAMES > 0:
            for i in range(len(scenes) - 1):
                prev_scene, next_scene = scenes[i], scenes[i+1]
                ca_prev, cu_prev = prev_scene.constant_vec, prev_scene.consult_vec
                ca_next, cu_next = next_scene.constant_vec, next_scene.consult_vec
                rotation = cu_prev != cu_next
                for di in range(FRAMES):
                    if rotation:
                        ca = ca_prev
                        cu = cu_prev if di < FRAMES / 2 else cu_next
                    else:
                        ca = lerp(ca_prev, ca_next, di / FRAMES)
                        cu = cu_prev
                    scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, ca, cu)
                    with open(f"{common_scene_name}-{i}-{di}.json", 'w') as file:
                        file.write(scene.json())
            ca_last, cu_last = scenes[-1].constant_vec, scenes[-1].consult_vec
            scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, ca_last, cu_last)
            with open(f"{common_scene_name}-{len(scenes)-1}.json", 'w') as file:
                file.write(scene.json())
            if Settings.SAVE_PYTHON:
                with open(f"{common_scene_name}-{len(scenes)-1}.py", 'w') as file:
                    file.write(scene.python())
            return scene
        else:
            if Settings.SAVE_JSON:
                with open(f"{common_scene_name}-{len(scenes)-1}.json", 'w') as file:
                    file.write(scenes[-1].json())
            if Settings.SAVE_PYTHON:
                with open(f"{common_scene_name}-{self.seed}.py", 'w') as file:
                    file.write(scenes[-1].python())
            return scenes[-1]

    def compute_change_table(self, prev_scene: Scene) -> None:
        self.table = [[False] * len(prev_scene.objs) for _ in range(len(prev_scene.constant_vec))]
        for i in range(len(prev_scene.constant_vec)):
            mults = build_multipliers(self.rng)
            mult = mults[0] if len(mults) > 0 else 1.0
            constant_copy = prev_scene.constant_vec.copy()
            constant_copy[i] *= mult
            scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, constant_copy, prev_scene.consult_vec)
            if len(scene.objs) != len(prev_scene.objs):
                #print(f"constant {i} changes the number of objects!")
                for a in range(len(prev_scene.objs)):
                    self.table[i][a] = True
            else:
                for a, o in enumerate(scene.objs):
                    if o.fcenter != prev_scene.objs[a].fcenter:
                        self.table[i][a] = True
                #print(f"constant {i} changes {sum(self.table[i])} objects: {[prev_scene.objs[j].name for (j, b) in enumerate(self.table[i]) if b]}")

    def compute_group_table(self, prev_scene: Scene) -> None:
        self.group_table = [[False] * len(prev_scene.objs) for _ in prev_scene.group_names]
        for i, o in enumerate(prev_scene.objs):
            self.group_table[o.group][i] = True



    def descent(self, prev_scene: Scene) -> Scene | None:
        #info("DESCENT")
        prev_loss = sum(rel.loss for rel in prev_scene.relations)
        min_loss = prev_loss
        min_scene = None
        if Settings.SEARCH_ORIENTATIONS:
            for i in range(self.num_constructors):
                #group_name, group_type = prev_scene.group_names[i]
                #if group_type == OBJECT.DOOR or group_type == OBJECT.WINDOW:
                #    continue
                changed = self.group_table[i]
                if not intersect(changed, prev_scene.problematic_rot_objects):
                    continue
                for d in range(4):
                    consult_copy = prev_scene.consult_vec.copy()
                    consult_copy[i] = 3 - d
                    scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, prev_scene.constant_vec, consult_copy)
                    loss = sum(rel.loss for rel in scene.relations)
                    #info(f"trying to set direction of group_names[{i}]={group_name} to {d} => loss = {loss}")
                    #if group_name == "Counter" and d == 1 and loss == 30:
                    #    with open(f"output/{group_name}-{d}-{loss}.json", 'w') as file:
                    #        file.write(scene.json())
                    if loss < min_loss:
                        min_loss = loss
                        min_scene = scene
                    if not intersect(changed, scene.problematic_rot_objects):
                        break
        if Settings.SEARCH_CONSTANTS:
            min_cost = None
            for i in range(len(prev_scene.constant_vec)):
                #print(f"i = {i}")
                changed = self.table[i]
                if not intersect(changed, prev_scene.problematic_objects):
                    continue
                multipliers = build_multipliers(self.rng)
                for m, mult in enumerate(multipliers):
                    constant_copy = prev_scene.constant_vec.copy()
                    use_addition = Settings.FIXED_MULTIPLIERS and len(multipliers) >= 10 and m >= len(multipliers) - 2
                    if not use_addition:
                        constant_copy[i] *= mult
                    else:
                        constant_copy[i] += mult
                    scene = Scene(self.basename, self.safe_code, self.env_code, self.seed, self.mapping, constant_copy, prev_scene.consult_vec)
                    loss = sum(rel.loss for rel in scene.relations)
                    #print(f"multiplying constant[{i}]={prev_scene.constant_vec[i]} by {mult} => loss={loss}")
                    if loss < min_loss:
                        min_loss = loss
                        min_cost = None
                        min_scene = scene
                    elif loss == min_loss and min_scene is not None and Settings.COMPUTE_COSTS and len(scene.objs) == len(prev_scene.objs):
                        if min_cost is None:
                            min_cost = compute_cost(min_scene, prev_scene)
                        cost = compute_cost(scene, prev_scene)
                        if cost < min_cost:
                            min_cost = cost
                            min_scene = scene
                            debug(f"{i} {prev_scene.constant_vec[i]} x {mult} has the same loss, and a better cost, this is a better transformation!")
                        else:
                            debug(f"{i} {prev_scene.constant_vec[i]} x {mult} has the same loss, but a bigger cost")
                    if not intersect(changed, scene.problematic_objects):
                        break
        if min_scene is None:
            info("descent fail")
        elif min_scene.constant_vec != prev_scene.constant_vec:
            info(f"descent success with {len(min_scene.relations)} errors and {min_loss} loss! min_constant_vec = {min_scene.constant_vec}")
        else:
            info(f"descent success with {len(min_scene.relations)} errors and {min_loss} loss! min_consult_vec = {min_scene.consult_vec}")
        return min_scene
