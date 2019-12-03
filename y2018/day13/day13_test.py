import pytest
from day13 import find_first_collesion_point


@pytest.mark.parametrize(
    ('plan', 'expected'),
    (
        (
            r"""
|
v
|
|
|
^
|""",
            (0, 3),
        ),
        (
            r"""
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """,  # noqa W291
            (7, 3),
        ),
        (
            r"""
/---\        
|   v  /----\
| /-+--+-\  |
| | |  ^ |  |
\-+-/  \-+--/
  \------/   """,  # noqa W291
            (6, 2),
        ),
        (
            r"""
/---\        
|   |  /----\
| /-+--+-\  |
| ^ ^  | |  |
\-+-/  \-+--/
  \------/   """,  # noqa W291
            (3, 2),
        ),
    ),
)
def test_find_first_collesion_point(plan, expected):
    assert find_first_collesion_point(plan) == expected
