# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

from dataclasses import dataclass
from enum import Enum

class RELATION(Enum):
    OUT_OF_BOUNDS = 0
    OVERLAP = 1
    AIR = 2
    SHORT_SIDE_TO_WALL = 3
    BAD_TOWER = 4
    FACING = 5
    FACING_SCENE = 6
    FACING_WALL = 7 # тут у меня были какие-то планы
    DOOR = 8 # это нужно считать оверлапом
    STANDING = 9
    MOUNTED = 10


@dataclass
class Record:
    type: RELATION
    name: str
    arity: str

# o = object, n = number, d = direction
relation_table: list[Record] = [
    Record(RELATION.OUT_OF_BOUNDS, 'outOfBounds', 'o'),
    Record(RELATION.OVERLAP, 'overlap', 'oo'),
    Record(RELATION.AIR, 'air', 'oo'),
    Record(RELATION.SHORT_SIDE_TO_WALL, 'shortSideToWall', 'o'),
    Record(RELATION.BAD_TOWER, 'badTower', 'oo'),
    Record(RELATION.FACING, 'facing', 'oo'),
    Record(RELATION.FACING_SCENE, 'facingScene', 'o'),
    Record(RELATION.FACING_WALL, 'facingWall', 'o'),
    Record(RELATION.DOOR, 'door', 'oo'),
    Record(RELATION.STANDING, 'standing', 'o'),
    Record(RELATION.MOUNTED, 'mounted', 'o'),
]

@dataclass
class Relation:
    rtype: RELATION
    args: list[int]
    loss: int
