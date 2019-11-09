import pytest
from day07 import collect_parallelizable_nodes
from day07 import find_dir_graph
from day07 import gen_nodes
from day07 import Node
from day07 import order_nodes
from day07 import parse_str
from day07 import sort_child_nodes
from day07 import work_duration
from day07 import Worker


input_str = [
    (
        'Step C must be finished before step A can begin.',
        [('C', 'A')],
    ),
    (
        'Step C must be finished before step A can begin.\n'
        'Step C must be finished before step B can begin.\n',
        [('C', 'A'), ('C', 'B')],
    ),
    (
        'Step C must be finished before step A can begin.\n' * 100,
        [('C', 'A')] * 100,
    ),
    (
        'Step C must be finished before step A can begin.\n'
        'Step C must be finished before step F can begin.\n'
        'Step A must be finished before step B can begin.\n'
        'Step A must be finished before step D can begin.\n'
        'Step B must be finished before step E can begin.\n'
        'Step D must be finished before step E can begin.\n'
        'Step F must be finished before step E can begin.\n',
        [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ],
    ),
]


@pytest.fixture(params=input_str)
def input_steps_str(request):
    return request.param


input_steps_list = [
    (
        [('C', 'A')],
        [
            Node('C', [], ['A']),
            Node('A', ['C'], []),
        ],
    ),
    (
        [('C', 'A')] * 10,
        [
            Node('C', [], ['A']),
            Node('A', ['C'], []),
        ],
    ),
    (
        [('C', 'A'), ('C', 'B')],
        [
            Node('C', [], ['A', 'B']),
            Node('A', ['C'], []),
            Node('B', ['C'], []),
        ],
    ),
    (
        [('C', 'B'), ('C', 'A')],
        [
            Node('C', [], ['B', 'A']),
            Node('B', ['C'], []),
            Node('A', ['C'], []),
        ],
    ),
    (
        [('C', 'B'), ('C', 'A')],
        [
            Node('C', [], ['B', 'A']),
            Node('B', ['C'], []),
            Node('A', ['C'], []),
        ],
    ),
    (
        [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ],
        [
            Node('C', [], ['A', 'F']),
            Node('A', ['C'], ['B', 'D']),
            Node('F', ['C'], ['E']),
            Node('B', ['A'], ['E']),
            Node('D', ['A'], ['E']),
            Node('E', ['B', 'D', 'F'], []),
        ],
    ),
]


@pytest.fixture(params=input_steps_list)
def input_steps(request):
    return request.param


input_sort_list = [
    (
        [
            Node('C', [], ['A']),
            Node('A', ['C'], []),
        ],
        [
            Node('A', ['C'], []),
            Node('C', [], ['A']),
        ],
    ),
    (
        [
            Node('C', ['A'], []),
            Node('A', [], ['D', 'C']),
            Node('D', [], ['C']),
        ],
        [
            Node('A', [], ['C', 'D']),
            Node('C', ['A'], []),
            Node('D', [], ['C']),
        ],
    ),
    (
        [
            Node('C', [], ['B', 'A']),
            Node('B', ['C', 'A'], []),
            Node('A', ['C'], []),
        ],
        [
            Node('A', ['C'], []),
            Node('B', ['A', 'C'], []),
            Node('C', [], ['A', 'B']),
        ],
    ),
    (
        [
            Node('C', [], ['A', 'F']),
            Node('A', ['C'], ['B', 'D']),
            Node('F', ['C'], ['E']),
            Node('B', ['A'], ['E']),
            Node('D', ['A'], ['E']),
            Node('E', ['B', 'D', 'F'], []),
        ],
        [
            Node('A', ['C'], ['B', 'D']),
            Node('B', ['A'], ['E']),
            Node('C', [], ['A', 'F']),
            Node('D', ['A'], ['E']),
            Node('E', ['B', 'D', 'F'], []),
            Node('F', ['C'], ['E']),
        ],
    ),
]


@pytest.fixture(params=input_sort_list)
def input_sorting(request):
    return request.param


input_nodes_list = [
    (
        [
            Node('A', ['C'], []),
            Node('C', [], ['A']),
        ],
        'CA',
    ),
    (
        [
            Node('A', [], ['C']),
            Node('C', ['A'], []),
        ],
        'AC',
    ),
    (
        [
            Node('A', ['C'], []),
            Node('B', ['C'], []),
            Node('C', [], ['A', 'B']),
            Node('D', ['A'], []),
            Node('F', ['A'], []),
        ],
        'CABDF',
    ),
    (
        [
            Node('A', ['C'], []),
            Node('B', ['C'], []),
            Node('C', [], ['A', 'B']),
            Node('D', ['A'], ['B']),
            Node('F', ['A'], []),
        ],
        'CABDF',
    ),
]


@pytest.fixture(params=input_nodes_list)
def input_nodes(request):
    return request.param


input_sample1 = [
    (
        'Step C must be finished before step A can begin.\n'
        'Step C must be finished before step F can begin.\n'
        'Step A must be finished before step B can begin.\n'
        'Step A must be finished before step D can begin.\n'
        'Step B must be finished before step E can begin.\n'
        'Step D must be finished before step E can begin.\n'
        'Step F must be finished before step E can begin.\n',
        'CABDFE',
    ),
]


@pytest.fixture(params=input_sample1)
def input_sample_str(request):
    return request.param


class TestDay07Part01:
    def test_parse_str(self, input_steps_str):
        steps_str, expected = input_steps_str
        assert parse_str(steps_str) == expected

    def test_gen_nodes(self, input_steps):
        steps, expected = input_steps
        assert gen_nodes(steps) == expected

    def test_sort_child_nodes(self, input_sorting):
        nodes, expected = input_sorting
        assert sort_child_nodes(nodes) == expected

    def test_order_nodes(self, input_nodes):
        nodes, expected = input_nodes
        assert order_nodes(nodes) == expected

    def test_find_dir_graph(self, input_sample_str):
        steps_str, expected = input_sample_str
        assert find_dir_graph(steps_str) == expected


input_for_cost = [
    (
        'A',
        0,
        1,
    ),
    (
        'A',
        60,
        61,
    ),
    (
        'Z',
        0,
        26,
    ),
    (
        'Z',
        60,
        86,
    ),
]


@pytest.fixture(params=input_for_cost)
def input_cost(request):
    return request.param


input_for_work = [
    (
        'A',
        0,
        'A',
    ),
    (
        'A',
        60,
        'A' * 61,
    ),
    (
        'Z',
        0,
        'Z' * 26,
    ),
    (
        'Z',
        60,
        'Z' * 86,
    ),
]


@pytest.fixture(params=input_for_work)
def input_work(request):
    return request.param


input_sample2 = [
    (
        'Step C must be finished before step A can begin.\n'
        'Step C must be finished before step F can begin.\n'
        'Step A must be finished before step B can begin.\n'
        'Step A must be finished before step D can begin.\n'
        'Step B must be finished before step E can begin.\n'
        'Step D must be finished before step E can begin.\n'
        'Step F must be finished before step E can begin.\n',
        2,
        0,
        15,
    ),
]


@pytest.fixture(params=input_sample2)
def input_sample_str2(request):
    return request.param


input_for_parallelisation = [
    (
        [
            Node('C', [], ['B', 'A']),
            Node('B', ['C'], []),
            Node('A', ['C'], []),
        ],
        [
            ['C'],
            ['B', 'A'],
        ],
    ),
    (
        [
            Node('C', [], ['B', 'A']),
            Node('B', ['C'], []),
            Node('D', ['C', 'B'], []),
            Node('A', ['C'], []),
        ],
        [
            ['C'],
            ['B', 'A'],
            ['D'],
        ],
    ),
    (
        [
            Node('C', [], ['A', 'D']),
            Node('B', [], ['D']),
            Node('D', ['C', 'B'], []),
            Node('A', ['C'], []),
        ],
        [
            ['C', 'B'],
            ['D', 'A'],
        ],
    ),
    (
        [
            Node('C', [], ['A', 'F']),
            Node('A', ['C'], ['B', 'D']),
            Node('F', ['C'], ['E']),
            Node('B', ['A'], ['E']),
            Node('D', ['A'], ['E']),
            Node('E', ['B', 'D', 'F'], []),
        ],
        [
            ['C'],
            ['A', 'F'],
            ['B', 'D'],
            ['E'],
        ],
    ),
    (  # same as above but different order
        [
            Node('A', ['C'], ['B', 'D']),
            Node('B', ['A'], ['E']),
            Node('C', [], ['A', 'F']),
            Node('D', ['A'], ['E']),
            Node('E', ['B', 'D', 'F'], []),
            Node('F', ['C'], ['E']),
        ],
        [
            ['C'],
            ['A', 'F'],
            ['B', 'D'],
            ['E'],
        ],
    ),
]


@pytest.fixture(params=input_for_parallelisation)
def input_parallelizable_nodes(request):
    return request.param


class TestDay07Part02:
    def test_work_duration(self, input_sample_str2):
        input_str, workers_count, init_cost, expected = input_sample_str2
        assert work_duration(input_str, workers_count, init_cost) == expected

    def test_cost(self, input_cost):
        input_chr, init_cost, expected = input_cost
        assert Worker(init_cost).cost(input_chr) == expected

    def test_work(self, input_work):
        input_chr, init_cost, expected = input_work
        assert Worker(init_cost).work(input_chr) == expected

    def test_collect_parallelizable_nodes(self, input_parallelizable_nodes):
        input_nodes, expected = input_parallelizable_nodes
        assert collect_parallelizable_nodes(input_nodes) == expected
