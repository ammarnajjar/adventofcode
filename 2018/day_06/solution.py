#!/usr/bin/env python
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


def str_to_points(input_data: str) -> List[Point]:
    r = []
    for line in input_data.strip().split('\n'):
        # each line has coordinates for exactly one point
        x, y = [int(a.strip()) for a in line.split(',')]
        r.append(Point(x, y))
    return r


def manhatten_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
