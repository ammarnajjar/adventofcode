import pytest

from solutions.y2018.day01 import first_frequesncy_reached_twice
from solutions.y2018.day01 import sum_lines


FREQ_INPUT1 = [('+1\n+1\n+1', 3), ('+1\n+1\n-2', 0), ('-1\n-2\n-3', -6)]


@pytest.fixture(params=FREQ_INPUT1)
def input_part1(request):
    return request.param


class TestDay01Part01:
    def test_adding_input_file_lines(self, input_part1):
        input_str, expected = input_part1
        assert sum_lines(input_str) == expected


FREQ_INPUT2 = [
    ('+1\n-1', 0),
    ('+3\n+3\n+4\n-2\n-4', 10),
    ('-6\n+3\n+8\n+5\n-6', 5),
    ('+7\n+7\n-2\n-7\n-4', 14),
]


@pytest.fixture(params=FREQ_INPUT2)
def input_part2(request):
    return request.param


class TestDay01Part02:
    def test_first_frequesncy_reached_twice(self, input_part2):
        input_str, expected = input_part2
        assert first_frequesncy_reached_twice(input_str) == expected
