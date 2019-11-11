"""
credits go to https://www.reddit.com/user/eltrufas/
https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/
"""
import os


current_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{current_path}/input07', 'r') as input_file:
    input_text = input_file.read().strip()


def next_step(steps, l):
    return [
        s
        for s in steps
        if all(
            b != s
            for (_, b) in l
        )
    ]


def time(c):
    return 60 + ord(c) - ord('A')


def part1():
    step_lines = [l.split() for l in input_text.split('\n')]
    lines = [(l[1], l[7]) for l in step_lines]
    steps = set(
        [s[0] for s in lines] + [s[1] for s in lines],
    )
    order = ''
    while steps:
        cand = list(next_step(steps, lines))
        cand.sort()

        n = cand[0]
        order += n
        steps.remove(n)
        lines = [
            (a, b)
            for (a, b) in lines
            if a != n
        ]

    print(order)


def part2():
    step_lines = [l.split() for l in input_text.split('\n')]
    lines = [(l[1], l[7]) for l in step_lines]
    steps = set(
        [s[0] for s in lines] + [s[1] for s in lines],
    )
    t = 0
    workers = [0 for _ in range(5)]
    work = [None for _ in range(5)]
    while steps or any(w > 0 for w in workers):
        cand = list(next_step(steps, lines))
        cand.sort()
        cand = cand[::-1]

        for i in range(5):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    lines = [
                        (a, b)
                        for (a, b) in lines
                        if a != work[i]
                    ]
                if cand:
                    n = cand.pop()
                    workers[i] = time(n)
                    work[i] = n
                    steps.remove(n)

        t += 1

    print(t)


if __name__ == '__main__':
    part1()
    part2()
