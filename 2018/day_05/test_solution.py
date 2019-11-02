#!/usr/bin/env python
import pytest

from .solution import chars_after_reactions
from .solution import min_chars_after_reactions

input_formula = [
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


@pytest.fixture(params=input_formula)
def input_to_scan(request):
    return request.param


class TestDay05Part01:
    def test_chars_after_reactions(self, input_to_scan):
        input, expected = input_to_scan
        assert chars_after_reactions(input) == expected


input_formula = [
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


@pytest.fixture(params=input_formula)
def input_part2(request):
    return request.param


class TestDay05Part02:
    def test_min_chars_after_reactions(self, input_part2):
        input, expected = input_part2
        assert min_chars_after_reactions(input) == expected
