#!/usr/bin/env python
import pytest
from .solution import first_frequesncy_reached_twice
from .solution import sum_lines


INPUT = [("+1\n+1\n+1", 3), ("+1\n+1\n-2", 0), ("-1\n-2\n-3", -6)]


@pytest.fixture(params=INPUT)
def input_part1(request):
    return request.param


class TestDay01Part01:
    def test_adding_input_file_lines(self, input_part1):
        input, expected = input_part1
        assert sum_lines(input) == expected


INPUT = [
    ("+1\n-1", 0),
    ("+3\n+3\n+4\n-2\n-4", 10),
    ("-6\n+3\n+8\n+5\n-6", 5),
    ("+7\n+7\n-2\n-7\n-4", 14),
]


@pytest.fixture(params=INPUT)
def input_part2(request):
    return request.param


class TestDay01Part02:
    def test_first_frequesncy_reached_twice(self, input_part2):
        input, expected = input_part2
        assert first_frequesncy_reached_twice(input) == expected
