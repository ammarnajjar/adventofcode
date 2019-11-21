"""
As this is a visual challenge, no tests are provided
The idea is to look for the point where dx and dy are minimum
That means that all points are as close to each other as they could be.

Result:

iteration = 10641

text:

#         #           # # #     # # # # #             # # #
#         #             #       #         #             #
#         #             #       #         #             #
#         #             #       #         #             #
# # # # # #             #       # # # # #               #
#         #             #       #         #             #
#         #             #       #         #             #
#         #     #       #       #         #     #       #
#         #     #       #       #         #     #       #
#         #       # # #         # # # # #         # # #


 #         #    # # # # #           # #         # # # # # #
 #         #    #         #       #     #                 #
   #     #      #         #     #         #               #
   #     #      #         #     #         #             #
     # #        # # # # #       #         #           #
     # #        #     #         # # # # # #         #
   #     #      #       #       #         #       #
   #     #      #       #       #         #     #
 #         #    #         #     #         #     #
 #         #    #         #     #         #     # # # # # #

"""
import copy
import os
import re
from dataclasses import dataclass
from typing import List


@dataclass
class Point:  # pragma no cover
    x: int
    y: int
    vx: int = 0
    vy: int = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy


def pprint(mat):  # pragma no cover
    for x in mat:
        print(' '.join(x))
    print()


def calc(input_text: str) -> List[List[str]]:  # pragma no cover
    pattern = re.compile(
        r'^\S+<([\s-]*\d+),([\s-]+\d+)>\s\S+<([\s-]*\d+),([\s-]+\d+)>$',
    )
    a = []
    for line in input_text.split('\n'):
        for x, y, vx, vy in re.findall(pattern, line):
            a.append(Point(int(x), int(y), int(vx), int(vy)))

    for i in range(1, 100000):
        aa = copy.deepcopy(a)
        maxx_before = max(p.x for p in a)
        minx_before = min(p.x for p in a)
        maxy_before = max(p.y for p in a)
        miny_before = min(p.y for p in a)
        for p in a:
            p.move()
        maxx_after = max(p.x for p in a)
        minx_after = min(p.x for p in a)
        maxy_after = max(p.y for p in a)
        miny_after = min(p.y for p in a)
        if (
            (maxy_after - miny_after) > (maxy_before - miny_before) or
            (maxx_after - minx_after) > (maxx_before - minx_before)
        ):
            print(i - 1)
            mat = []
            for y in range(miny_before, maxy_before + 1):
                matx = []
                for x in range(minx_before, maxx_before + 1):
                    matx.append(' ')
                mat.append(matx)
            for p in aa:
                mat[p.y-miny_before][p.x-minx_before] = '#'
            break
    return mat


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    # with open(f'{current_path}/input_text', 'r') as input_file: # no qa E800
    with open(f'{current_path}/input10', 'r') as input_file:
        input_text = input_file.read().strip()
    pprint(calc(input_text))
