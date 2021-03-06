import os
from typing import Iterator
from typing import List


def split_input_by_line(input_str: str) -> List[int]:
    return [int(x.strip()) for x in input_str.split('\n') if x]


def sum_lines(input_str: str) -> int:
    return sum(split_input_by_line(input_str))


def gen_input(input_list: List[int]) -> Iterator[int]:
    while 1:
        for x in input_list:
            yield x


def first_frequesncy_reached_twice(input_str: str) -> int:
    freq_cache = [0]
    current_freq = 0
    g = gen_input(split_input_by_line(input_str))
    while 1:
        current_freq += next(g)
        if current_freq in freq_cache:
            return current_freq
        else:
            freq_cache.append(current_freq)


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input01', 'r') as input_file:
        content_text = input_file.read()
        freq = sum_lines(content_text)
        print(f'Resulting frequency = {freq}')
        freq = first_frequesncy_reached_twice(content_text)
        print(f'First frequency reached twice= {freq}')
