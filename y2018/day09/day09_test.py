import pytest
from day09 import insert
from day09 import part1


use_cases1 = (
    (
        '9 players; last marble is worth 22 points',
        [
            0, 16, 8, 17, 4, 18, 9, 19, 2, 20,
            10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15,
        ],
    ),
    (
        '9 players; last marble is worth 23 points',
        [
            0, 16, 8, 17, 4, 18, 19, 2, 20, 10,
            21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15,
        ],
    ),
    (
        '9 players; last marble is worth 24 points',
        [
            0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 10,
            21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15,
        ],
    ),
)


@pytest.mark.parametrize(
    ('input_text', 'expected'),
    use_cases1,
)
def test_marble_insertion(input_text, expected):
    assert insert(input_text) == expected


use_cases2 = (
    (
        '9 players; last marble is worth 25 points',
        32,
    ),
    (
        '10 players; last marble is worth 1618 points',
        8317,
    ),
    (
        '13 players; last marble is worth 7999 points',
        146373,
    ),
    (
        '17 players; last marble is worth 1104 points',
        2764,
    ),
    (
        '21 players; last marble is worth 6111 points',
        54718,
    ),
    (
        '30 players; last marble is worth 5807 points',
        37305,
    ),
)


@pytest.mark.parametrize(
    ('input_text', 'expected'),
    use_cases2,
)
def test_players_score(input_text, expected):
    assert part1(input_text) == expected
