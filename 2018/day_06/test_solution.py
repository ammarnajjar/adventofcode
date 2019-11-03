#!/usr/bin/env python
import pytest

from .solution import manhatten_distance
from .solution import Point

input_points = [
    (
        Point(1, 2),
        Point(1, 2),
        0,
    ),
    (
        Point(2, 2),
        Point(1, 2),
        1,
    ),
    (
        Point(1, 2),
        Point(2, 2),
        1,
    ),
    (
        Point(1, 2),
        Point(2, 1),
        2,
    ),
    (
        Point(1, 2),
        Point(2, 1),
        2,
    ),
]


@pytest.fixture(params=input_points)
def input_points_part1(request):
    return request.param


class TestDay06Part01:
    def test_manhatten_distance(self, input_points_part1):
        p1, p2, distance = input_points_part1
        assert manhatten_distance(p1, p2) == distance
