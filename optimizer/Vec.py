# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

import math
from random import Random

from .logger import info

class Vec:
    x: float
    y: float
    z: float

    def __init__(self, X: float, Y: float, Z: float):
        self.x = X
        self.y = Y
        self.z = Z

    def __eq__(self, other: 'Vec') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vec(-self.x, -self.y, -self.z)

    def __mul__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x / other.x, self.y / other.y, self.z / other.z)

    def __rmul__(self, other: float) -> 'Vec':
        return Vec(other * self.x, other * self.y, other * self.z)

    def __str__(self):
        return f'Vec({self.x:.3g}, {self.y:.3g}, {self.z:.3g})'

    @staticmethod
    def random_vec(rng: Random) -> 'Vec':
        x = 2.0 * (rng.random() - 0.5)
        y = 2.0 * (rng.random() - 0.5)
        z = 2.0 * (rng.random() - 0.5)
        return Vec(x, y, z)

    @staticmethod
    def min(v1: 'Vec', v2: 'Vec') -> 'Vec':
        return Vec(min(v1.x, v2.x), min(v1.y, v2.y), min(v1.z, v2.z))

    @staticmethod
    def max(v1: 'Vec', v2: 'Vec') -> 'Vec':
        return Vec(max(v1.x, v2.x), max(v1.y, v2.y), max(v1.z, v2.z))

    """
    def dot(self, other: 'Vec') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z
    """
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def volume(self) -> float:
        return self.x * self.y * self.z

    def min_component(self) -> float:
        return min(self.x, self.y, self.z)
    def max_component(self) -> float:
        return max(self.x, self.y, self.z)

    def relu(self) -> 'Vec':
        return Vec(max(self.x, 0.0), max(self.y, 0.0), max(self.z, 0.0))

    def normalization(self) -> 'Vec':
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return  Vec(self.x / length, self.y / length, self.z / length)

    """
    def abs(self) -> 'Vec':
        return Vec(abs(self.x), abs(self.y), abs(self.z))

    def slope(self, vmin: 'Vec', vmax: 'Vec') -> 'Vec':
        result = Vec(0.0, 0.0, 0.0)

        if self.x > vmax.x:
            result.x = self.x - vmax.x
        elif self.x < vmin.x:
            result.x = self.x - vmin.x

        if self.y > vmax.y:
            result.y = self.y - vmax.y
        elif self.y < vmin.y:
            result.y = self.y - vmin.y

        if self.z > vmax.z:
            result.z = self.z - vmax.z
        elif self.z < vmin.z:
            result.z = self.z - vmin.z

        return result
    """

    def flip_yz(self) -> 'Vec':
        return Vec(self.x, self.z, self.y)
    def flip_yz_minus(self) -> 'Vec':
        return Vec(self.x, self.z, -self.y)
    def json(self) -> str:
        return f'[{self.x:.4g}, {self.y:.4g}, {self.z:.4g}]'
    #def json(self, flip: bool = False) -> str:
    #    return f'[{self.x:.4g}, {self.z:.4g}, {(-self.y if flip else self.y):.4g}]'
    #def json_round(self) -> str:
    #    return f'[{round(self.X)}, {round(self.Y)}, {round(self.Z)}]'

    def cardinal_dir(self) -> int:
        if self.x >= self.y and self.x > -self.y:
            return 0
        elif self.y < self.x and self.y <= -self.x:
            return 3
        elif self.x <= self.y and self.x < -self.y:
            return 2
        else:
            return 1


def random_position(min_pos: Vec, max_pos: Vec, rng: Random) -> Vec:
    return min_pos + (max_pos - min_pos) * Vec(rng.random(), rng.random(), rng.random())

def best_dir(a: Vec, b: Vec, bsize: Vec) -> int:
    if a.x < b.x - 0.5 * bsize.x:
        d0 = b.x - 0.5 * bsize.x - a.x
    elif a.x > b.x + 0.5 * bsize.x:
        d0 = a.x - b.x - 0.5 * bsize.x
    else:
        d0 = 0.0
    if a.y < b.y - 0.5 * bsize.y:
        d1 = b.y - 0.5 * bsize.y - a.y
    elif a.y > b.y + 0.5 * bsize.y:
        d1 = a.y - b.y - 0.5 * bsize.y
    else:
        d1 = 0.0
    if d0 == 0 and d1 == 0:
        d0 = abs(a.x - b.x)
        d1 = abs(a.y - b.y)
    return (1 if b.y > a.y else 3) if d0 <= d1 else (0 if b.x > a.x else 2)


def ideal_size(original_size: Vec, filled_area: float, max_length: float, MIN_FILL: float, MAX_FILL: float) -> Vec:
    fill_percentage = filled_area / (original_size.x * original_size.y)
    print(f"fill_percentage = {fill_percentage}")
    if MIN_FILL <= fill_percentage <= MAX_FILL:
        return original_size
    elif fill_percentage < MIN_FILL:
        scaling_factor = math.sqrt(filled_area / (MIN_FILL * original_size.x * original_size.y))
        if scaling_factor <= 0.95:
            new_x = float(round(original_size.x * scaling_factor))
            new_y = float(round(original_size.y * scaling_factor))
            if new_x < max_length:
                new_x = max_length
                info(f"limited x by max_length {max_length}")
            if new_y < max_length:
                new_y = max_length
                info(f"limited y by max_length {max_length}")
            if new_x != original_size.x or new_y != original_size.y:
                info(f"  {int(fill_percentage)} => scaling down from {original_size.x}x{original_size.y} to {new_x:.0f}x{new_y:.0f}, factor of {scaling_factor:.2f}")
                return Vec(new_x, new_y, original_size.z)
    """
    elif fill_percentage > MAX_FILL:
        scaling_factor = math.sqrt(filled_area / (MAX_FILL * original_size.x * original_size.y))
        new_x = round(original_size.x * scaling_factor)
        new_y = round(original_size.y * scaling_factor)
        if new_x != original_size.x or new_y != original_size.y:
            print(f"  {int(fill_percentage)} => scaling up from {original_size.x}x{original_size.y} to {new_x:.0f}x{new_y:.0f}, factor of {scaling_factor:.2f}")
            return Vec(new_x, new_y, original_size.z)
    """
    return original_size

