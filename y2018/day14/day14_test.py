from day14 import part1
from day14 import part2


def test_part1():
    assert part1('37', 5) == '0124515891'
    assert part1('37', 9) == '5158916779'
    assert part1('37', 18) == '9251071085'
    assert part1('37', 2018) == '5941429882'


def test_part2():
    assert part2('37', '51589') == 9
    assert part2('37', '01245') == 5
    assert part2('37', '92510') == 18
    assert part2('37', '59414') == 2018
