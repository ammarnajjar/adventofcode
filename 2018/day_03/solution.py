#!/usr/bin/env python
# -*- coding: utf-8 -*-


def shared_squares(input_data: str) -> int:
    data_list = input_data.strip().split("\n")
    height = max([
        int(
            line.split()[-2].replace(':', '').split(',')[-1],
        ) + int(line.split()[-1].split('x')[-1])
        for line in data_list
    ])
    width = max([
        int(
            line.split()[-2].replace(':', '').split(',')[0],
        ) + int(line.split()[-1].split('x')[0])
        for line in data_list
    ])

    grid = []

    # initialize empty grid with dots
    for i in range(height):
        grid_line = ['.'] * width
        grid.append(grid_line)

    for line in data_list:
        _id, _, _loc, dim = line.split()
        _id = _id.replace('#', '')
        x, y = _loc.replace(':', '').split(',')
        w, h = dim.split('x')
        # mark id territory on grid
        for i in range(int(y), int(y) + int(h)):
            for j in range(int(x), int(x) + int(w)):
                if (grid[i][j] == '.'):
                    grid[i][j] = _id
                else:
                    grid[i][j] = 'x'
    # count the x's
    count = 0
    for i in range(height):
        count += grid[i].count('x')

    return count
