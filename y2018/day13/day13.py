import os
from collections import namedtuple
from dataclasses import dataclass
from dataclasses import field
from itertools import combinations
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple


Grid = List[List[str]]
TurnMap = Dict[Tuple[int, Optional[str]], str]
Position = namedtuple('Position', 'x, y')


@dataclass
class Cart:
    grid: Grid
    pos: Position
    direction: Optional[str]  # < , >, v, ^
    next_turn: int            # 0=left, 1=straight, 2=right
    previous_state: str = field(init=False)

    def __post_init__(self):
        state_map = {
            '<': '-',
            '>': '-',
            '^': '|',
            'v': '|',
        }
        self.previous_state = state_map.get(self.direction)

    def move(self):
        self.grid[self.pos.y][self.pos.x] = self.previous_state
        move_map = {
            '<': self.step_left,
            '>': self.step_right,
            '^': self.step_up,
            'v': self.step_down,
        }
        return move_map.get(self.direction)()

    def step_up(self):
        trans_map = {
            '\\': (0,),
            '|':  (1,),
            '/':  (2,),
            '+':  (self.next_turn, True),
        }
        next = self.grid[self.pos.y - 1][self.pos.x]
        self.grid[self.pos.y][self.pos.x] = self.previous_state
        self.previous_state = next
        self.pos = Position(self.pos.x, self.pos.y - 1)
        next_turn = trans_map.get(next)
        if next_turn:
            self.turn(*next_turn)
            self.grid[self.pos.y][self.pos.x] = self.direction
        else:
            return (self.pos.x, self.pos.y)

    def step_down(self):
        trans_map = {
            '\\': (0,),
            '|':  (1,),
            '/':  (2,),
            '+':  (self.next_turn, True),
        }
        next = self.grid[self.pos.y + 1][self.pos.x]
        self.grid[self.pos.y][self.pos.x] = self.previous_state
        self.previous_state = next
        self.pos = Position(self.pos.x, self.pos.y + 1)
        next_turn = trans_map.get(next)
        if next_turn:
            self.turn(*next_turn)
            self.grid[self.pos.y][self.pos.x] = self.direction
        else:
            return (self.pos.x, self.pos.y)

    def step_left(self):
        trans_map = {
            '\\': (2,),
            '-':  (1,),
            '/':  (0,),
            '+':  (self.next_turn, True),
        }
        next = self.grid[self.pos.y][self.pos.x - 1]
        self.grid[self.pos.y][self.pos.x] = self.previous_state
        self.previous_state = next
        self.pos = Position(self.pos.x - 1, self.pos.y)
        next_turn = trans_map.get(next)
        if next_turn:
            self.turn(*next_turn)
            self.grid[self.pos.y][self.pos.x] = self.direction
        else:
            return (self.pos.x, self.pos.y)

    def step_right(self):
        trans_map = {
            '\\': (2,),
            '-':  (1,),
            '/':  (0,),
            '+':  (self.next_turn, True),
        }
        next = self.grid[self.pos.y][self.pos.x + 1]
        self.grid[self.pos.y][self.pos.x] = self.previous_state
        self.previous_state = next
        self.pos = Position(self.pos.x + 1, self.pos.y)
        next_turn = trans_map.get(next)
        if next_turn:
            self.turn(*next_turn)
            self.grid[self.pos.y][self.pos.x] = self.direction
        else:
            return (self.pos.x, self.pos.y)

    def turn(self, turn: int, intersection: bool = False):
        d: TurnMap = {
            (0, '>'): '^',
            (2, '>'): 'v',

            (0, '<'): 'v',
            (2, '<'): '^',

            (0, '^'): '<',
            (2, '^'): '>',

            (0, 'v'): '>',
            (2, 'v'): '<',
        }
        next_dir = d.get((turn, self.direction), None)
        if next_dir:
            self.direction = next_dir
        if intersection:
            self.next_turn = (self.next_turn + 1) % 3


def plan_to_grid(plan: str) -> Grid:
    r = []
    lines = plan.split('\n')
    for line in lines:
        if line:
            r.append(list(line))
    return r


def collect_carts(grid: Grid) -> List[Cart]:
    carts_on_grid = ('<', '>', '^', 'v')
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in carts_on_grid:
                cart = Cart(
                    grid=grid,
                    pos=Position(x, y),
                    direction=grid[y][x],
                    next_turn=0,
                )
                carts.append(cart)
    carts = sorted(carts, key=lambda x: x.pos)
    return carts


def tick_to_crash(plan: str) -> Tuple[int, int]:
    grid = plan_to_grid(plan)
    carts = collect_carts(grid)
    while 1:
        for cart in carts:
            crash = cart.move()
            if crash:
                return crash
        carts = sorted(carts, key=lambda x: x.pos)


def get_crashing_carts(carts: List[Cart]) -> List[Cart]:
    r = []
    for c1, c2 in combinations(carts, 2):
        if c1.pos == c2.pos:
            r.append((c1, c2))
    return [a for b in r for a in b]  # flatten list of tuples


def tick_to_last(plan: str) -> Tuple[int, int]:
    init_grid = plan_to_grid(plan)
    grid = plan_to_grid(plan)
    carts = collect_carts(grid)
    while len(carts) > 1:
        for cart in carts:
            cart.move()
            cs = get_crashing_carts(carts)
            if cs:
                c = cs[0]
                grid[c.pos.y][c.pos.x] = init_grid[c.pos.y][c.pos.x]
            carts = [x for x in carts if x not in cs]
            if cs:
                print('crash: ', cs[0].pos, len(cs), len(carts))
        carts = sorted(carts, key=lambda x: x.pos)
    return carts[0].pos.x, carts[0].pos.y


def find_first_collesion_point(plan: str) -> Tuple[int, int]:
    return tick_to_crash(plan)


def find_last_cart_position(plan: str) -> Tuple[int, int]:
    return tick_to_last(plan)


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input13', 'r') as input_file:
        input_text = input_file.read()
    part1 = find_first_collesion_point(input_text)
    print('part1: ', part1)
    # 45,76
    part2 = find_last_cart_position(input_text)
    print('part2: ', part2)
