from itertools import combinations


def checksum(input_data: str) -> int:
    data_list = input_data.strip().split('\n')
    twos, threes = 0, 0
    for line in data_list:
        lo = line.strip().lower()
        unique_chars = set(lo)

        for unique_char2 in unique_chars:
            if lo.count(unique_char2) == 2:
                twos += 1
                break
        for unique_char3 in unique_chars:
            if lo.count(unique_char3) == 3:
                threes += 1
                break
    return twos * threes


def common_letters_between_correct_codes(input_data: str) -> str:
    data_list = input_data.strip().split('\n')
    for x, y in combinations(data_list, 2):
        # get index where two strings differ
        r = [
            (i, z)
            for i, z in enumerate(zip(x, y))
            if z[0] != z[1]
        ]
        if len(r) < 2:
            index = r[0][0]
            return x[:index] + x[index + 1:]
    return ''
