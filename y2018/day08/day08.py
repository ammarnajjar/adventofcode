"""Part 1"""
import os
from typing import List
from typing import Tuple


def parse(input_data: List[int]) -> Tuple[int, List[int]]:
    n_child, n_meta = input_data[:2]
    input_data = input_data[2:]
    totals = 0
    for _ in range(n_child):
        total, input_data = parse(input_data)
        totals += total
    totals += sum(input_data[:n_meta])
    return totals, input_data[n_meta:]


def part1(input_text: str) -> int:
    x = [int(c) for c in input_text.strip().split()]
    return parse(x)[0]


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input08', 'r') as input_file:
        input_text = input_file.read().strip()
    # solution is between 55110 and 35713 -> 40977
    print(part1(input_text))
