import os
from typing import List
from typing import Tuple


def parse(input_data: List[int]) -> Tuple[int, int, List[int]]:
    n_child, n_meta = input_data[:2]
    input_data = input_data[2:]
    totals = 0
    data_values = []
    for _ in range(n_child):
        total, data_value, input_data = parse(input_data)
        totals += total
        data_values.append(data_value)
    totals += sum(input_data[:n_meta])
    if n_child == 0:
        data_value = sum(input_data[:n_meta])
    else:
        data_value = sum(
            # list index starts at 0, meta index starts at 1
            data_values[i - 1]
            for i in input_data[:n_meta]
            # ignore if no children referenced
            if 0 < i <= len(data_values)
        )
    return totals, data_value, input_data[n_meta:]


def part1(input_text: str) -> int:
    x = [int(c) for c in input_text.strip().split()]
    p = parse(x)
    return p[0]


def part2(input_text: str) -> int:
    x = [int(c) for c in input_text.strip().split()]
    p = parse(x)
    return p[1]


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input08', 'r') as input_file:
        input_text = input_file.read().strip()
    # part1 solution is between 55110 and 35713 -> 40977
    print(part1(input_text))
    print(part2(input_text))
