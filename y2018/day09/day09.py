import os
from collections import deque
from typing import Deque
from typing import Dict


def calc(input_str: str) -> int:
    splitted = input_str.split()
    players, marbles = int(splitted[0]), int(splitted[-2])

    scores: Dict[int, int] = {}
    g: Deque[int] = deque([0])

    for m in range(1, marbles + 1):
        if m % 23 == 0:
            player = (m - 1) % players
            g.rotate(-7)
            score = scores.get(player, 0) + m + g.pop()
            scores.update({player: score})
        else:
            g.rotate(2)
            g.append(m)
    return max(
        scores.get(player, 0) for player in range(1, players + 1)
    )


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input09', 'r') as input_file:
        input_text = input_file.read().strip()
    print(calc(input_text))
