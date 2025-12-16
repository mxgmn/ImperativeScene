# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

from typing import Dict

from .Scene import Scene
from .Relation import RELATION, relation_table
from .logger import info

class Stat:
    average_num_objects: float
    average_groups: float
    average_range: float
    average_fill: float
    average_num_relations: float
    average_detailed_relations: list[float]
    average_loss: float
    average_num_corrections: float
    error_free_rate: float

    average_area: float
    average_width: float
    average_depth: float

    constants_dict: Dict[float, int]

    def __init__(self, scenes: list[Scene]):
        sum_num_objects = 0.0
        sum_groups = 0.0
        sum_range = 0.0
        sum_fill = 0.0
        sum_num_relations = 0
        sum_detailed_relations = [0 for r in RELATION]
        sum_loss = 0
        num_error_free = 0
        sum_corrections = 0

        sum_area = 0.0
        sum_width = 0.0
        sum_depth = 0.0

        self.constants_dict = {}

        for scene in scenes:
            sum_num_objects += len(scene.objs)
            sum_groups += len(scene.group_names)
            sum_range += len(scene.objs) / len(scene.group_names)
            sum_fill += scene.fill_percentage()
            sum_num_relations += len(scene.relations)
            for r in scene.relations:
                sum_detailed_relations[r.rtype.value] += 1
            sum_loss += sum(rel.loss for rel in scene.relations)
            if len(scene.relations) == 0:
                num_error_free += 1
            sum_corrections += scene.number_of_corrections

            sum_area_in_scene = 0.0
            sum_width_in_scene = 0.0
            sum_depth_in_scene = 0.0
            for o in scene.objs:
                sum_area_in_scene += o.width * o.depth
                sum_width_in_scene += o.width
                sum_depth_in_scene += o.depth
            sum_area += sum_area_in_scene / len(scene.objs)
            sum_width += sum_width_in_scene / len(scene.objs)
            sum_depth += sum_depth_in_scene / len(scene.objs)

            for f in scene.constant_vec:
                if f in self.constants_dict:
                    self.constants_dict[f] = self.constants_dict[f] + 1
                else:
                    self.constants_dict[f] = 1

        self.average_num_objects = sum_num_objects / len(scenes)
        self.average_groups = sum_groups / len(scenes)
        self.average_range = sum_range / len(scenes)
        self.average_fill = sum_fill / len(scenes)
        self.average_num_relations = sum_num_relations / len(scenes)
        self.average_detailed_relations = [s / len(scenes) for s in sum_detailed_relations]
        self.average_num_corrections = sum_corrections / len(scenes)

        self.average_loss = sum_loss / len(scenes)
        self.error_free_rate = num_error_free / len(scenes)

        self.average_area = sum_area / len(scenes)
        self.average_width = sum_width / len(scenes)
        self.average_depth = sum_depth / len(scenes)


    def print(self) -> None:
        info()
        info(f"average number of objects = {int(self.average_num_objects)}")
        info(f"average number of groups = {self.average_groups:.1f}")
        info(f"average range = {self.average_range:.1f}")
        info(f"average fill percentage = {int(100.0 * self.average_fill)}")
        info(f"average number of relations = {self.average_num_relations:.2f}")
        for R in RELATION:
            info(f"    {relation_table[R.value].name} = {self.average_detailed_relations[R.value]:.2f}")
        info(f"average loss = {self.average_loss:.2f}")
        info(f"{int(100.0 * self.error_free_rate)}% error-free scenes")
        info(f"average object area = {self.average_area:.2f} = {self.average_width:.2f} x {self.average_depth:.2f}")
        info(f"average number of corrections = {self.average_num_corrections:.2f}")

        #sorted_items = sorted(self.constants_dict.items(), key=lambda item: item[1], reverse=True)
        #for key, value in sorted_items:
        #    print(f"x{value} {key}")






