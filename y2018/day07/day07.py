import os
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Tuple


@dataclass
class Node:
    name: str
    before: List[str] = field(default_factory=lambda: [])
    after: List[str] = field(default_factory=lambda: [])


def parse_str(input_data: str) -> List[Tuple[str, str]]:
    r = []
    for line in input_data.strip().split('\n'):
        s = line.split()
        r.append((s[1], s[7]))
    return r


def gen_nodes(steps: List[Tuple[str, str]]) -> List[Node]:
    # Node is not hashable, therefore set cannot be used here
    nodes: List[Node] = []
    for step in steps:
        for name in step:
            if not [n for n in nodes if n.name == name]:
                nodes.append(Node(name))

    for node in nodes:
        for (before, after) in steps:
            if before == node.name and after not in node.after:
                node.after.append(after)
            if after == node.name and before not in node.before:
                node.before.append(before)
    return nodes


def sort_child_nodes(nodes: List[Node]) -> List[Node]:
    sorted_nodes = sorted(nodes, key=lambda n: n.name)
    for node in sorted_nodes:
        # order chiild nodes
        node.before.sort()
        node.after.sort()
    return sorted_nodes


def order_nodes(nodes: List[Node]) -> str:
    r = ''
    rest = nodes[:]
    while (rest):
        for node in nodes:
            if not node.before:
                r += node.name
                rest = [x for x in rest if x != node]
                for n in rest:
                    if node.name in n.before:
                        n.before.remove(node.name)
                    if node.name in n.after:
                        n.after.remove(node.name)
                break
        nodes = rest
    return r


def find_dir_graph(input_data: str) -> str:
    parsed_nodes = parse_str(input_data)
    nodes = gen_nodes(parsed_nodes)
    nodes = sort_child_nodes(nodes)
    return order_nodes(nodes)


@dataclass
class Worker:
    init_cost: int = 0
    is_working: bool = False

    def cost(self, job: str) -> int:
        return ord(job) - ord('A') + 1 + self.init_cost

    def work(self, job: str) -> str:
        return job * self.cost(job)


def collect_parallelizable_nodes(nodes: List[Node]) -> List[List[str]]:
    stk = []  # stak parallel jobs
    while (nodes):
        par = [
            node.name
            for node in nodes
            if not node.before
        ]
        stk.append(par)
        nodes = [
            node
            for node in nodes
            if node.name not in par
        ]
        for node in nodes:
            node.before = [
                x for x in node.before
                if x not in par
            ]
            node.after = [
                x for x in node.after
                if x not in par
            ]
    return stk


def work_duration(
    input_str: str,
    workers_count: int = 5,
    init_cost: int = 60,
) -> int:
    parsed_nodes = parse_str(input_str)
    nodes = gen_nodes(parsed_nodes)
    par = collect_parallelizable_nodes(nodes)
    pipeline = order_nodes(nodes)
    for i, npar in enumerate(par):
        for node in pipeline:
            if node in npar:
                print(Worker().work(node))
                print(i, node)
    return 0


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input07', 'r') as input_file:
        input_text = input_file.read().strip()
        print(f'Directet graph = {find_dir_graph(input_text)}')
