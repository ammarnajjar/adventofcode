import pytest
from day05 import chars_after_reactions
from day05 import min_chars_after_reactions

INPUT_FORMULA1 = [
    (
        'dabAcCaCBAcCcaDA',
        10,
    ),
    (
        'dabAcCCBAcCcaDA',
        11,
    ),
    (
        'dbaCfgkyYKGFcABD',
        0,
    ),
    (
        'dbaCfgkyYKGFcABDx',
        1,
    ),
    (
        'xdbaCfgkyYKGFcABD',
        1,
    ),
    (
        'adbaCfgkyYKGFcABDa',
        2,
    ),
    (
        'acCcCA',
        0,
    ),
    (
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        40,
    ),
]


@pytest.fixture(params=INPUT_FORMULA1)
def input_to_scan(request):
    return request.param


class TestDay05Part01:
    def test_chars_after_reactions(self, input_to_scan):
        input_str, expected = input_to_scan
        assert chars_after_reactions(input_str) == expected


INPUT_FORMULA2 = [
    (
        'dabAcCaCBAcCcaDA',
        4,
    ),
    (
        'dbaCfgkyYKGFcABD',
        0,
    ),
    (
        'dbXaCfgkyYKGFcABDx',
        0,
    ),
    (
        'xdbaCfgkyYKGFcABD',
        0,
    ),
    (
        'xaaaaaaaaaaaaaaaXbaaaaaaaaaaaaaaaaaaaaaaaaa',
        1,
    ),
]


@pytest.fixture(params=INPUT_FORMULA2)
def input_part2(request):
    return request.param


class TestDay05Part02:
    def test_min_chars_after_reactions(self, input_part2):
        input_str, expected = input_part2
        assert min_chars_after_reactions(input_str) == expected
