"""
Solution for AoC 2018 day 14.

I noticed that calling to an external function in python costs a lot of time.
That's why I repeated some code for both part1 and part2.
"""


def part1(src: str, times: int) -> str:
    elf1, elf2 = 0, 1
    while(len(src) < 10 + times):
        src += str(int(src[elf1]) + int(src[elf2]))
        size = len(src)
        elf1 = (elf1 + 1 + int(src[elf1])) % size
        elf2 = (elf2 + 1 + int(src[elf2])) % size
    return src[times: times + 10]


def part2(src: str, score: str) -> int:
    elf1, elf2 = 0, 1
    while(score not in src[-8:]):
        src += str(int(src[elf1]) + int(src[elf2]))
        size = len(src)
        elf1 = (elf1 + 1 + int(src[elf1])) % size
        elf2 = (elf2 + 1 + int(src[elf2])) % size
    return src.index(score)


if __name__ == '__main__':  # pragma no cover
    start = '37'
    times = 157901

    # 9411137133 in 0.6sec
    print('part1: ', part1(start, times))

    # 20317612 in 22sec
    score = str(times)
    print('part2: ', part2(start, score))
