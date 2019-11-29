import pytest
from day12 import calc
from day12 import get_rules

example2 = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""


@pytest.mark.parametrize(
    ('input_text', 'generations', 'result'),
    (
        (
            'initial state: #....\n\n...#. => #',
            3,
            -3,
        ),
        (
            'initial state: #....\n\n...#. => #',
            2,
            -2,
        ),
        (
            'initial state: ##....\n\n..##. => #',
            1,
            0,
        ),
        (
            'initial state: #.....\n\n...#. => #',
            1,
            -1,
        ),
        (
            'initial state: #.....\n\n....# => #',
            1,
            -2,
        ),
        (
            'initial state: #.....\n\n#.... => #',
            1,
            2,
        ),
        (example2, 20, 325),
    ),
)
def test_calc(input_text, generations, result):
    rules, state = get_rules(input_text)
    assert calc(rules, state, generations) == result
