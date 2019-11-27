import pytest
from day11 import calc_cells
from day11 import calc_power
from day11 import get_max_power

examples2 = (
    (
        (33, 45), 18, 29,
    ),
    (
        (21, 61), 42, 30,
    ),
)


@pytest.mark.parametrize(
    ('cell', 'serial', 'power'),
    examples2,
)
def test_calc_cell(serial, cell, power):
    assert get_max_power(calc_cells(serial), 3) == (cell, power)


examples = (
    (
        (3, 5), 8, 4,
    ),
    (
        (122, 79), 57, -5,
    ),
    (
        (217, 196), 39,  0,
    ),
    (
        (101, 153), 71,  4,
    ),
)


@pytest.mark.parametrize(
    ('cell', 'serial', 'power'),
    examples,
)
def test_calc_power(cell, serial, power):
    assert calc_power(cell, serial) == power
