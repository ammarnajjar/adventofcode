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


def calc(rules: Dict[str, str], state: str, generatiions: int) -> int:
    margin = 4
    expan = len(state) + margin
    state = f'{state:.>{expan}}'
    state = f'{state:.<{expan + margin}}'
    offset = 0
    for g in range(generatiions):
        new_state = ''
        for i in range(2, len(state) - 3):
            window = state[i - 2:i + 3]
            r = rules.get(window, '.')
            new_state += r
        state = new_state
        last_s = state.rfind('#')
        first_s = state.find('#')
        offset += first_s - 2
        state = state[first_s:last_s + 1]
        state = f'{state:.>{len(state) + margin}}'
        state = f'{state:.<{len(state) + 2 * margin}}'
        print(g + 1, state)

    last_s = state.rfind('#')
    first_s = state.find('#')
    state = state[first_s:last_s + 1]
    acc = sum(i+offset for i, x in enumerate(state) if x == '#')
    return acc


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input12', 'r') as input_file:
        input_text = input_file.read().strip()
    rules, state = get_rules(input_text)
    generations = 20
    print('part1: ', calc(rules, state, generations))  # 3798
