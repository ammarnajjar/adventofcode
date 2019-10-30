#!/usr/bin/env python
# -*- coding: utf-8 -*-


def checksum(input_data: str) -> int:
    input_data = input_data.strip().split('\n')
    _twos, _threes = 0, 0
    for line in input_data:
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

