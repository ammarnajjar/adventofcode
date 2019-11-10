import copy
import os
import time
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Tuple


@dataclass
class Node:
    name: str
    before: Tuple[str, ...] = field(default_factory=lambda: ())
    after: Tuple[str, ...] = field(default_factory=lambda: ())


def parse_str(input_data: str) -> Tuple[Tuple[str, str], ...]:
    r = []
    for line in input_data.strip().split('\n'):
        s = line.split()
        r.append((s[1], s[7]))
    return tuple(r)


STEP_TYPE = Tuple[Tuple[str, str], ...]


def gen_nodes(steps: STEP_TYPE) -> Tuple[Node, ...]:
    # Node is not hashable, therefore set cannot be used here
    nodes: List[Node] = []
    for step in steps:
        for name in step:
            if not [n for n in nodes if n.name == name]:
                nodes.append(Node(name))

    for node in nodes:
        for (before, after) in steps:
            if before == node.name and after not in node.after:
                node.after = (*node.after, after)
            if after == node.name and before not in node.before:
                node.before = (*node.before, before)
    return tuple(nodes)


def sort_child_nodes(nodes: Tuple[Node, ...]) -> Tuple[Node, ...]:
    sorted_nodes = sorted(nodes, key=lambda n: n.name)
    for node in sorted_nodes:
        # order chiild nodes
        node.before = tuple(sorted(node.before))
        node.after = tuple(sorted(node.after))
    return tuple(sorted_nodes)


def order_nodes(nodes: Tuple[Node, ...]) -> Tuple[str, ...]:
    r = ''
    # copy nodes first
    rest = copy.deepcopy(list(nodes))
    local_nodes = copy.deepcopy(list(nodes))
    while (rest):
        for node in local_nodes:
            if not node.before:
                r += node.name
                rest = [x for x in rest if x != node]
                for n in rest:
                    if node.name in n.before:
                        n_before = list(n.before)
                        n_before.remove(node.name)
                        n.before = tuple(n_before)
                    if node.name in n.after:
                        n_after = list(n.after)
                        n_after.remove(node.name)
                        n.after = tuple(n_after)
                break
        local_nodes = rest
    return tuple(r)


def find_dir_graph(input_data: str) -> str:
    parsed_nodes = parse_str(input_data)
    nodes = gen_nodes(parsed_nodes)
    nodes = sort_child_nodes(nodes)
    return ''.join(order_nodes(nodes))


def collect_parallelizable_nodes(
    nodes: Tuple[Node, ...],
) -> Tuple[List[str], ...]:
    stk = []  # stak parallel jobs
    rest = list(copy.deepcopy(nodes))
    while (rest):
        par = [
            node.name
            for node in rest
            if not node.before
        ]
        stk.append(par)
        rest = [
            node
            for node in rest
            if node.name not in par
        ]
        for node in rest:
            node.before = tuple(
                x for x in node.before
                if x not in par
            )
            node.after = tuple(
                x for x in node.after
                if x not in par
            )
    return tuple(stk)


def cost(job: str, offset: int = 0) -> int:
    return ord(job) - ord('A') + 1 + offset


def work(node: Node) -> None:
    for _ in range(cost(node.name)):
        print(node.name)
        time.sleep(0.5)


def work_all(nodes: Tuple[Node, ...], order: Tuple[str, ...]) -> None:
    par = collect_parallelizable_nodes(nodes)
    print(par)
    local_order = list(order)
    while (local_order):
        current = local_order.pop(0)
        node = next(n for n in nodes if n.name == current)
        for npar in par:
            if node.name in npar:
                npar.remove(node.name)
        print(local_order, node)


def work_duration(
    input_data: str,
    workers_count: int = 5,
    init_cost: int = 60,
) -> int:
    parsed_nodes = parse_str(input_data)
    nodes = gen_nodes(parsed_nodes)
    print('1 = ', nodes)
    order = order_nodes(nodes)
    print('3 = ', nodes)
    work_all(nodes, order)
    return 0


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input07', 'r') as input_file:
        input_text = input_file.read().strip()
        # HPDTNXYLOCGEQSIMABZKRUWVFJ
        print(f'Directet graph = {find_dir_graph(input_text)}')
