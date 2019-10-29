#!/usr/bin/env python
from typing import Iterator
from typing import List


def split_input_by_line(content: str) -> List[int]:
    return [int(x.strip()) for x in content.split("\n") if x]


def sum_lines(content: str) -> int:
    return sum(split_input_by_line(content))


def gen_input(input_list: List[int]) -> Iterator[int]:
    while 1:
        for x in input_list:
            yield x


def first_frequesncy_reached_twice(content: str) -> int:
    _cache = [0]
    _current_freq = 0
    g = gen_input(split_input_by_line(content))
    while 1:
        _current_freq += next(g)
        if _current_freq in _cache:
            return _current_freq
        else:
            _cache.append(_current_freq)
