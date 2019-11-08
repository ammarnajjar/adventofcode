import sys


def chars_after_reactions(input_data: str) -> int:
    while 1:
        stop = True
        i = 1
        r = ''
        while i < len(input_data):
            base_cdiff = ord('a') - ord('A')  # == 32
            cdiff = abs(
                ord(input_data[i - 1]) - ord(input_data[i]),
            )
            if cdiff == base_cdiff:
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
    min_char = sys.maxsize
    for c in all_chars:
        n = chars_after_reactions(
            input_data.replace(c, '').replace(c.upper(), ''),
        )
        if n < min_char:
            min_char = n
        print(c, n, min_char)
    return min_char
