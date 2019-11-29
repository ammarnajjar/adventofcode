import os
from typing import Dict
from typing import Tuple


def get_rules(input_text: str) -> Tuple[Dict[str, str], str]:
    text_lst = input_text.split('\n')
    state = text_lst[0].split(':')[1].strip()
    rules = {}
    for (x, y) in (
        w.strip().split('=>')
        for w in text_lst[2:]
        if w
    ):
        rules.update({x.strip(): y.strip()})
    return rules, state


def sum_lives(state: str, offset: int) -> Tuple[str, int]:
    last_s = state.rfind('#')
    first_s = state.find('#')
    state = state[first_s:last_s + 1]
    return state, sum(i + offset for i, x in enumerate(state) if x == '#')


def pad_state(state: str, margin: int = 4) -> str:
    state = f'{state:.>{len(state) + margin}}'
    return f'{state:.<{len(state) + 2 * margin}}'


def calc(rules: Dict[str, str], state: str, generatiions: int) -> int:
    state = pad_state(state)
    offset = 0
    for g in range(generatiions):
        new_state = ''
        for i in range(2, len(state) - 3):
            window = state[i - 2:i + 3]
            r = rules.get(window, '.')
            new_state += r
        state, acc1 = sum_lives(state, offset)

        state = new_state
        first_s = state.find('#')
        offset += first_s - 2
        state, acc2 = sum_lives(state, offset)
        state = pad_state(state)
        print(g + 1, state, acc2 - acc1)

    state, acc = sum_lives(state, offset)
    return acc


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input12', 'r') as input_file:
        input_text = input_file.read().strip()
    rules, state = get_rules(input_text)
    generations = 20
    print('part1: ', calc(rules, state, generations))  # 3798
    # for part 2
    # I looked into the game of life algorithm
    # but then I thought that there might be a trick!
    # for when I started the program I saw that the pattern
    # does not chenge, so I calculated the change between
    # two sequencial generations, and saw the trick!
    generations = 150
    print(
        'part2: ',
        calc(rules, state, generations) + (
            50_000_000_000 - generations
        ) * 78,
    )  # 3900000002212
