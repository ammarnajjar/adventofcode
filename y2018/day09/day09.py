import os
from collections import deque
from typing import Deque
from typing import Dict
from typing import Tuple


def parse(input_str: str) -> Tuple[int, int]:
    splitted = input_str.split()
    players = int(splitted[0])
    marbles = int(splitted[-2])
    return marbles, players


def cycle(i: int, circle: Deque):
    if i > 0:
        v = circle.pop()
        circle.appendleft(v)
        circle = cycle(i - 1, circle)
    elif i < 0:
        v = circle.popleft()
        circle.append(v)
        circle = cycle(i + 1, circle)
    return circle


def calc(input_str: str) -> int:
    marbles, players = parse(input_str)

    scores: Dict[int, int] = {}
    g = deque([0])

    for m in range(1, marbles + 1):
        if m % 23 == 0:
            player = (m - 1) % players
            cycle(-7, g)
            score = scores.get(player, 0) + m + g.pop()
            scores.update({player: score})
        else:
            g = cycle(2, g)
            g.append(m)
    return max(
        scores.get(player, 0) for player in range(1, players + 1)
    )


def part2(input_str: str) -> int:
    return calc(input_str)


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input09', 'r') as input_file:
        input_text = input_file.read().strip()
    print(part2(input_text))
