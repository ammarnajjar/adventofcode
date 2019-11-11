import pytest
from day08 import part1
from day08 import part2


input_part1 = (
    (
        '2 2 '
        '1 1 '
        '0 2 1 1 '
        '1 '
        '0 1 1 '
        '2 2',
        2 + 2 + 1 + 1 + 1 + 1,
    ),
    (
        '3 3 '
        '2 2 '
        '1 1 '
        '0 2 1 1 '
        '1 '
        '0 1 1 '
        '2 2 '
        '2 2 '
        '0 1 1 '
        '0 2 1 1 '
        '2 2 '
        '0 3 1 1 1 '
        '3 3 3',
        27,
    ),
    (
        '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2',
        138,
    ),
    (
        '2 1 0 3 10 11 12 1 1 0 1 99 2 1',
        135,
    ),
    (
        '0 1 99',
        99,
    ),
    (
        '3 1 0 1 99 0 1 99 0 1 99 1',
        99 * 3 + 1,
    ),
    (
        '1 1 1 1 0 1 99 99 99',
        99 * 3,
    ),
)


@pytest.fixture(params=input_part1)
def sample_part1(request):
    return request.param


class TestDay8:
    def test_part1(self, sample_part1):
        input_text, expected = sample_part1
        assert part1(input_text) == expected


input_sample = (
    (
        '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2',
        66,
    ),
    (
        '2 3 0 3 10 11 12 1 1 0 1 99 1 1 1 2',
        66 + 99,
    ),
    (
        '2 2 '
        '1 1 '
        '0 2 1 1 '
        '1 '
        '0 1 1 '
        '2 2',
        2,
    ),
    (
        '3 3 '
        '2 2 '  # 2
        '1 1 '
        '0 2 1 1 '
        '1 '
        '0 1 1 '
        '2 2 '
        '2 2 '  # 4
        '0 1 1 '
        '0 2 1 1 '
        '2 2 '
        '0 3 1 1 1 '  # 3
        '1 2 3',
        2 + 4 + 3,
    ),
)


@pytest.mark.parametrize(
    'par', input_sample,
)
def test_part2(par):
    s, r = par
    assert part2(s) == r
