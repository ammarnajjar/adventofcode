import pytest
from day_04.solution import choose_guard
from day_04.solution import guard_freq_alseep
from day_04.solution import key_with_max_value
from day_04.solution import order_chronologically
from day_04.solution import sleeping_map

soring_input = [
    (
        [
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:55] wakes up',
            '[1518-11-01 00:55] wakes up',
        ],
        [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up',
        ],
    ),
    (
        [
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:55] wakes up',
            '[1518-11-01 00:55] wakes up',
        ],
        [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up',
        ],
    ),
]

guard_sleeping = [(
    [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up',
    ],
    (
        {
            10: 50,
            99: 30,
        },
        {
            10: [(5, 25), (30, 55), (24, 29)],
            99: [(40, 50), (36, 46), (45, 55)],
        },
    ),
)]

sample_input = [
    (
        '[1518-11-04 00:02] Guard #99 begins shift\n'
        '[1518-11-01 00:05] falls asleep\n'
        '[1518-11-02 00:40] falls asleep\n'
        '[1518-11-01 23:58] Guard #99 begins shift\n'
        '[1518-11-02 00:50] wakes up\n'
        '[1518-11-05 00:45] falls asleep\n'
        '[1518-11-03 00:05] Guard #10 begins shift\n'
        '[1518-11-01 00:00] Guard #10 begins shift\n'
        '[1518-11-01 00:30] falls asleep\n'
        '[1518-11-01 00:25] wakes up\n'
        '[1518-11-03 00:24] falls asleep\n'
        '[1518-11-03 00:29] wakes up\n'
        '[1518-11-04 00:36] falls asleep\n'
        '[1518-11-04 00:46] wakes up\n'
        '[1518-11-05 00:03] Guard #99 begins shift\n'
        '[1518-11-05 00:55] wakes up\n'
        '[1518-11-01 00:55] wakes up\n',
        240,
    ),
    (
        '[1518-11-01 00:05] falls asleep\n'
        '[1518-11-04 00:46] wakes up\n'
        '[1518-11-05 00:03] Guard #99 begins shift\n'
        '[1518-11-05 00:55] wakes up\n'
        '[1518-11-03 00:05] Guard #10 begins shift\n'
        '[1518-11-01 00:00] Guard #10 begins shift\n'
        '[1518-11-01 00:30] falls asleep\n'
        '[1518-11-01 00:25] wakes up\n'
        '[1518-11-02 00:50] wakes up\n'
        '[1518-11-02 00:40] falls asleep\n'
        '[1518-11-01 00:55] wakes up\n'
        '[1518-11-01 23:58] Guard #99 begins shift\n'
        '[1518-11-04 00:02] Guard #99 begins shift\n'
        '[1518-11-05 00:45] falls asleep\n'
        '[1518-11-03 00:24] falls asleep\n'
        '[1518-11-03 00:29] wakes up\n'
        '[1518-11-04 00:36] falls asleep\n',
        240,
    ),
]


int_dict_input = [
    (
        {
            1: 3,
            4: 2,
            6: 1,
            33: 9,
            90: 10,
        },
        90,
    ),
    (
        {
            1: 3,
            4: 2,
            6: 1,
            33: 9,
            90: 0,
        },
        33,
    ),
]


@pytest.fixture(params=guard_sleeping)
def sleeping_input(request):
    return request.param


@pytest.fixture(params=soring_input)
def input_to_sort(request):
    return request.param


@pytest.fixture(params=int_dict_input)
def key_max_input(request):
    return request.param


@pytest.fixture(params=sample_input)
def choose_guard_input(request):
    return request.param


class TestDay04Part01:
    def test_order_chronologically(self, input_to_sort):
        input_str, expected = input_to_sort
        assert order_chronologically(input_str) == expected

    def test_sleeping_map(self, sleeping_input):
        input_str, expected = sleeping_input
        assert sleeping_map(input_str) == expected

    def test_key_with_max_value(self, key_max_input):
        input_str, expected = key_max_input
        assert key_with_max_value(input_str) == expected

    def test_choose_guard(self, choose_guard_input):
        input_str, expected = choose_guard_input
        assert choose_guard(input_str) == expected


sample_input2 = [
    (
        '[1518-11-04 00:02] Guard #99 begins shift\n'
        '[1518-11-01 00:05] falls asleep\n'
        '[1518-11-02 00:40] falls asleep\n'
        '[1518-11-01 23:58] Guard #99 begins shift\n'
        '[1518-11-02 00:50] wakes up\n'
        '[1518-11-05 00:45] falls asleep\n'
        '[1518-11-03 00:05] Guard #10 begins shift\n'
        '[1518-11-01 00:00] Guard #10 begins shift\n'
        '[1518-11-01 00:30] falls asleep\n'
        '[1518-11-01 00:25] wakes up\n'
        '[1518-11-03 00:24] falls asleep\n'
        '[1518-11-03 00:29] wakes up\n'
        '[1518-11-04 00:36] falls asleep\n'
        '[1518-11-04 00:46] wakes up\n'
        '[1518-11-05 00:03] Guard #99 begins shift\n'
        '[1518-11-05 00:55] wakes up\n'
        '[1518-11-01 00:55] wakes up\n',
        4455,
    ),
    (
        '[1518-11-01 00:05] falls asleep\n'
        '[1518-11-04 00:46] wakes up\n'
        '[1518-11-05 00:03] Guard #99 begins shift\n'
        '[1518-11-05 00:55] wakes up\n'
        '[1518-11-03 00:05] Guard #10 begins shift\n'
        '[1518-11-01 00:00] Guard #10 begins shift\n'
        '[1518-11-01 00:30] falls asleep\n'
        '[1518-11-01 00:25] wakes up\n'
        '[1518-11-02 00:50] wakes up\n'
        '[1518-11-02 00:40] falls asleep\n'
        '[1518-11-01 00:55] wakes up\n'
        '[1518-11-01 23:58] Guard #99 begins shift\n'
        '[1518-11-04 00:02] Guard #99 begins shift\n'
        '[1518-11-05 00:45] falls asleep\n'
        '[1518-11-03 00:24] falls asleep\n'
        '[1518-11-03 00:29] wakes up\n'
        '[1518-11-04 00:36] falls asleep\n',
        4455,
    ),
]


@pytest.fixture(params=sample_input2)
def guard_freq_alseep_input(request):
    return request.param


class TestDay04Part02:
    def test_guard_freq_alseep(self, guard_freq_alseep_input):
        input_str, expected = guard_freq_alseep_input
        assert guard_freq_alseep(input_str) == expected
