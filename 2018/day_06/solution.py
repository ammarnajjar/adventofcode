#!/usr/bin/env python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def manhatten_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
