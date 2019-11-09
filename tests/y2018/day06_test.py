import pytest

from solutions.y2018.day06 import largest_area
from solutions.y2018.day06 import manhatten_distance
from solutions.y2018.day06 import non_outer_points
from solutions.y2018.day06 import Point
from solutions.y2018.day06 import region_size
from solutions.y2018.day06 import str_to_points

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

points_outers = [
    (
        '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9\n',
        [Point(3, 4), Point(5, 5)],
    ),
    (
        '2, 1\n1, 6\n8, 3\n0, 4\n5, 5\n8, 9\n',
        [Point(5, 5)],
    ),
]

points_sample1 = [
    (
        '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9\n',
        17,
    ),
    (
        '2, 1\n1, 6\n8, 3\n0, 4\n5, 5\n8, 9\n',
        20,
    ),
]


@pytest.fixture(params=points_str)
def input_points_str(request):
    return request.param


@pytest.fixture(params=input_manhatten_str)
def input_points_part1(request):
    return request.param


@pytest.fixture(params=points_outers)
def input_points_outers(request):
    return request.param


@pytest.fixture(params=points_sample1)
def input_points_sample1(request):
    return request.param


class TestDay06Part01:
    def test_str_to_points(self, input_points_str):
        points_string, expected = input_points_str
        assert str_to_points(points_string) == expected

    def test_manhatten_distance(self, input_points_part1):
        points_string, distance = input_points_part1
        p1, p2 = str_to_points(points_string)
        assert manhatten_distance(p1, p2) == distance

    def test_non_outer_points(self, input_points_outers):
        points_string, expected = input_points_outers
        points = str_to_points(points_string)
        assert non_outer_points(points) == expected

    def test_largest_area(self, input_points_sample1):
        points_string, expected = input_points_sample1
        assert largest_area(points_string) == expected


points_sample2 = [
    (
        '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9\n',
        32,
        16,
    ),
    (
        '2, 1\n1, 6\n8, 3\n0, 4\n5, 5\n8, 9\n',
        32,
        8,
    ),
]


@pytest.fixture(params=points_sample2)
def input_points_sample2(request):
    return request.param


class TestDay06Part02:
    def test_reagion_size(self, input_points_sample2):
        points_string, max_size, expected = input_points_sample2
        assert region_size(points_string, max_size) == expected
