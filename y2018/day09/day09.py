import os
from typing import Dict
from typing import List
from typing import Tuple


def parse(input_str: str) -> Tuple[int, int]:
    splitted = input_str.split()
    players = int(splitted[0])
    marbles = int(splitted[-2])
    return marbles, players


def inc_p(player: int, ceiling: int) -> int:
    if player == ceiling:
        return 1
    return player + 1


def calc(input_str: str) -> Tuple[List[int], int]:
    marbles, players = parse(input_str)

    scores: Dict[int, int] = {}
    g = [0, 1]

    player = 1
    pos = 1
    for m in range(2, marbles + 1):
        player = inc_p(player, players)
        if m % 23 == 0:
            pos = pos - 7
            score = g.pop(pos)
            score += m
            current_score = scores.get(player, 0)
            scores.update({player: score + current_score})
            continue
        elif (m - 1) % 23 == 0:
            pos = g.index(m - 2) - 4
        else:
            pos = g.index(m - 1) + 2
        if pos > len(g):
            pos = pos - len(g)
        g.insert(pos, m)
    print(scores)
    max_score = max(
        scores.get(player, 0) for player in range(1, players + 1)
    )
    return g, max_score


def insert(input_str: str) -> List[int]:
    return calc(input_str)[0]


def part1(input_str: str) -> int:
    return calc(input_str)[1]


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input09', 'r') as input_file:
        input_text = input_file.read().strip()
    print(part1(input_text))
