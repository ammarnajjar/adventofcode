from itertools import product
from typing import Dict
from typing import Tuple

SERIAL = 2568
WINDOW_SIZE = 3


def calc_power(cell, serial):
    """Calculate the power for a single cell
    """
    rack_id = cell[0] + 10
    power_level = rack_id * cell[1]
    power_level += serial
    power_level *= rack_id
    hundereds = power_level // 100
    if hundereds > 10:
        hundereds = hundereds % 10
    power_level = hundereds - 5
    return power_level


def calc_cells(serial: int) -> Dict[Tuple[int, int], int]:
    """Calculate the power for all cells
    and store them in a dict to retrieve them faster later
    """
    r = {}
    for i in range(300):
        for j in range(300):
            r.update({(i, j): calc_power((i, j), serial)})
    return r


def get_max_power(
    cells_power: Dict[Tuple[int, int], int],
    size: int,
):
    """Get the maximum power cell and its power
    """
    max_power = -999999
    selected_cell = (0, 0)
    for i in range(300 - size + 1):
        for j in range(300 - size + 1):
            pow = 0
            cell = (i, j)
            for x, y in product(range(size), range(size)):
                pow += cells_power.get((i + x, j + y), 0)
            if pow > max_power:
                selected_cell = cell
                max_power = pow
    return selected_cell, max_power


if __name__ == '__main__':  # pragma no cover
    cells_power = calc_cells(SERIAL)

    print('part1:', get_max_power(cells_power, WINDOW_SIZE))

    # this takes a lot of time to complete
    # but as soon as I saw that values are going low
    # I tried the maximum power present, and it was the correct answert
    # so I stoped the execuation.
    # a possible optimization would be to use numpy arrays
    selected_size = 3
    max_power = 0
    selected_cell = (0, 0)
    for w in range(3, 300):
        cell, power = get_max_power(cells_power, w)
        if power > max_power:
            max_power = power
            selected_cell = cell
            selected_size = w
        print(cell, power, selected_cell, max_power, w)
    print('part2:', selected_cell, max_power, selected_size)
