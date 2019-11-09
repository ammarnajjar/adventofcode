import pytest

from solutions.y2018.day02 import checksum
from solutions.y2018.day02 import common_letters

INPUT1 = [('abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n', 12)]


@pytest.fixture(params=INPUT1)
def input_part1(request):
    return request.param


class TestDay02Part01:
    def test_checksum(self, input_part1):
        input_str, expected = input_part1
        assert checksum(input_str) == expected


INPUT2 = [
    ('abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz\n', 'fgij'),
    ('abcde\nasrfg\nklmno\npqrst\nasdfg\naxcye\nwvxyz\n', 'asfg'),
    ('abcde\nfghi\ngklm\nnopq\nrstu\nwvxyz\n', ''),
]


@pytest.fixture(params=INPUT2)
def input_part2(request):
    return request.param


class TestDay02Part02:
    def test_checksum(self, input_part2):
        input_str, expected = input_part2
        assert common_letters(input_str) == expected
