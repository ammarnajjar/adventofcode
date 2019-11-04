#!/usr/bin/env python
import pytest

from .solution import manhatten_distance
from .solution import Point
from .solution import str_to_points

input_manhatten_str = [
    (
        '1, 2\n1, 2\n',
        0,
    ),
    (
        '2, 2\n1, 2\n',
        1,
    ),
    (
        '1, 2\n2, 2\n',
        1,
    ),
    (
        '1, 2\n2, 1\n',
        2,
    ),
    (
        '2, 1\n1, 2\n',
        2,
    ),
]

points_str = [
    (
        '1, 2\n1, 2\n1, 2\n1, 2\n',
        [Point(1, 2)] * 4,
    ),
    (
        '2, 2\n1, 2\n2, 2\n1, 2\n',
        [Point(2, 2), Point(1, 2)] * 2,
    ),
]


@pytest.fixture(params=points_str)
def input_points_str(request):
    return request.param


@pytest.fixture(params=input_manhatten_str)
def input_points_part1(request):
    return request.param


class TestDay06Part01:
    def test_str_to_points(self, input_points_str):
        points_string, expected = input_points_str
        assert str_to_points(points_string) == expected

    def test_manhatten_distance(self, input_points_part1):
        points_string, distance = input_points_part1
        p1, p2 = str_to_points(points_string)
        assert manhatten_distance(p1, p2) == distance
