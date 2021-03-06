import os
import sys
from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


def str_to_points(input_data: str) -> List[Point]:
    """parse multi line string into points
    considering that every line contains
    the coordinates of exactly one point
    """
    r = []
    for line in input_data.strip().split('\n'):
        # each line has coordinates for exactly one point
        x, y = [
            int(a.strip())
            for a in line.split(',')
        ]
        r.append(Point(x, y))
    return r


def manhatten_distance(p1: Point, p2: Point) -> int:
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    return dx + dy


def get_quarter(dx: int, dy: int) -> int:
    """check in which quarter a point
    is located relatively to another.
    """
    if dx > 0:
        if dy > 0:
            return 1
        return 4
    elif dy > 0:
        return 2
    return 3


def non_outer_points(points: List[Point]) -> List[Point]:
    """A point is marked as outer point
    if there is not at least one other
    point in every quarter, after moving
    the center to that point.
    """
    r = []
    for p1 in points:
        quarters = []
        other_points = [p for p in points if p != p1]
        for p2 in other_points:
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            quarters.append(get_quarter(dx, dy))
        if {1, 2, 3, 4}.issubset(set(quarters)):
            r.append(p1)
    return r


def largest_area(points_string: str) -> int:
    points = str_to_points(points_string)
    target_points = non_outer_points(points)
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    areas = []
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            print(f'scanning ({x}, {y})')
            min_d = sys.maxsize
            for p in points:
                d = manhatten_distance(Point(x, y), p)
                if d < min_d:
                    min_d = d
                    area = p
            areas.append(area)
    print('areas are calculated')
    return max(areas.count(a) for a in target_points)


def region_size(points_string: str, max_size: int) -> int:
    points = str_to_points(points_string)
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    region = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            print(f'scanning ({x}, {y})')
            d = sum(
                manhatten_distance(Point(x, y), p)
                for p in points
            )
            if d < max_size:
                region += 1
    return region


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input06', 'r') as input_file:
        input_text = input_file.read().strip()
        print(f'Largest area = {largest_area(input_text)}')
        print(f'Region size = {region_size(input_text, 10000)}')
