#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from .solution import checksum


INPUT = [
    "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n",
]


@pytest.fixture(params=INPUT)
def input_data(request):
    return request.param


class TestDay02Part01:
    def test_checksum(self, input_data):
        assert checksum(input_data) == 12
