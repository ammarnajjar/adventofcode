#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations


def checksum(input_data: str) -> int:
    data_list = input_data.strip().split("\n")
    _twos, _threes = 0, 0
    for line in data_list:
        lo = line.strip().lower()
        unique_chars = set(lo)

        for c in unique_chars:
            if lo.count(c) == 2:
                _twos += 1
                break
        for c in unique_chars:
            if lo.count(c) == 3:
                _threes += 1
                break
    return _twos * _threes


def common_letters_between_correct_codes(input_data: str) -> str:
    data_list = input_data.strip().split("\n")
    result = ""
    for x, y in combinations(data_list, 2):
        # get index where two strings differ
        r = [(i, z) for i, z in enumerate(zip(x, y)) if z[0] != z[1]]
        if len(r) < 2:
            index = r[0][0]
            result = x[:index] + x[index + 1:]
            break
    return result
