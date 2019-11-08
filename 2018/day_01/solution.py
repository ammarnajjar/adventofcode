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
