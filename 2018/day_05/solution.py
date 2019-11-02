#!/usr/bin/env python
import sys


def chars_after_reactions(input_data: str) -> int:
    while 1:
        stop = True
        i = 1
        r = ''
        while i < len(input_data):
            # ord('a') - ord('A') == 32
            if abs(ord(input_data[i - 1]) - ord(input_data[i])) == 32:
                i += 1
                stop = False
            else:
                r += input_data[i - 1]
            # handle last character
            if i == len(input_data) - 1:
                r += input_data[i]
            i += 1
        input_data = r
        if stop or len(input_data) == 1:
            break
    return len(r)


def min_chars_after_reactions(input_data: str) -> int:
    all_chars = set(input_data.lower())
    _min = sys.maxsize
    for c in all_chars:
        n = chars_after_reactions(
            input_data.replace(c, '').replace(c.upper(), ''),
        )
        if n < _min:
            _min = n
        print(c, n, _min)
    return _min
