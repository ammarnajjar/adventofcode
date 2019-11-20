import pytest
from day09 import calc


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
    assert calc(input_text) == expected
