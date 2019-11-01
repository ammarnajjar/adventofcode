#!/usr/bin/env python
from collections import defaultdict
from datetime import datetime
from typing import Dict
from typing import List
from typing import Tuple


def order_chronologically(data_list: List[str]) -> List[str]:
    return sorted(
        data_list,
        key=lambda x: datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'),
    )


SleepingMap = Tuple[Dict[int, int], Dict[int, List[Tuple[int, int]]]]


def sleeping_map(sorted_data_list: List[str]) -> SleepingMap:
    minutes: Dict[int, int] = {}
    spans: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    for entry in sorted_data_list:
        if 'Guard' in entry:
            guard_id = int(entry.split('#')[1].split()[0])
        if 'falls' in entry:
            start_sleeping = datetime.strptime(entry[1:17], '%Y-%m-%d %H:%M')
        if 'wakes' in entry:
            end_sleeping = datetime.strptime(entry[1:17], '%Y-%m-%d %H:%M')
            minutes.update({
                guard_id: minutes.get(guard_id, 0) + (
                    end_sleeping - start_sleeping
                ).seconds // 60,
            })
            spans[guard_id].append(
                (start_sleeping.minute, end_sleeping.minute),
            )
    return minutes, dict(spans)


def key_with_max_value(minutes: Dict[int, int]) -> int:
    max_asleep = 0
    chosen_guard = 0
    for _id, _asleep in minutes.items():
        if _asleep > max_asleep:
            chosen_guard = _id
            max_asleep = _asleep
    return chosen_guard


def minute_most_asleep(spans: List[Tuple[int, int]]) -> int:
    rank = {m: 0 for m in range(60)}
    for m in range(60):
        for span in spans:
            if m in range(*span):
                rank[m] += 1
    return key_with_max_value(rank)


def choose_guard(input_data: str) -> int:
    data_list = input_data.strip().split("\n")
    actions_in_order = order_chronologically(data_list)
    minutes, spans = sleeping_map(actions_in_order)
    chosen_guard = key_with_max_value(minutes)
    chosen_minute = minute_most_asleep(spans[chosen_guard])
    return chosen_guard * chosen_minute
