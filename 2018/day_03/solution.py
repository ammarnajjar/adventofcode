from typing import List


def _all_ids(data_list: List[str]) -> List[int]:
    return [
        int(line.split()[0].replace('#', ''))
        for line in data_list
    ]


def _height(data_list: List[str]) -> int:
    return max(
        int(
            line.split()[
                -2
            ].replace(':', '').split(',')[-1],
        ) + int(line.split()[-1].split('x')[-1])
        for line in data_list
    )


def _width(data_list: List[str]) -> int:
    return max(
        int(
            line.split()[
                -2
            ].replace(':', '').split(',')[0],
        ) + int(line.split()[-1].split('x')[0])
        for line in data_list
    )


def _create_data_grid(data_list: List[str]) -> List[List[str]]:
    height = _height(data_list)
    width = _width(data_list)
    grid = []

    # initialize empty grid with dots
    for _ in range(height):
        grid_line = ['.'] * width
        grid.append(grid_line)

    for line in data_list:
        claim_id, _, loc, dim = line.split()
        claim_id = claim_id.replace('#', '')
        x, y = loc.replace(':', '').split(',')
        w, h = dim.split('x')
        # mark id territory on grid
        for i in range(int(y), int(y) + int(h)):
            for j in range(int(x), int(x) + int(w)):
                if (grid[i][j] == '.'):
                    grid[i][j] = claim_id
                else:
                    grid[i][j] += f'x{claim_id}'
    return grid


def shared_squares(input_data: str) -> int:
    data_list = input_data.strip().split('\n')
    grid = _create_data_grid(data_list)
    # count the x's
    return sum(
        len([a for a in row if 'x' in a])
        for row in grid
    )


def claim_not_overlaped(input_data: str) -> int:
    data_list = input_data.strip().split('\n')
    grid = _create_data_grid(data_list)
    xs = [cell for row in grid for cell in row if 'x' in cell]
    overlapped_ids = []
    for cell in xs:
        claim_ids = [int(claim_id) for claim_id in cell.split('x')]
        for claim_id in claim_ids:
            overlapped_ids.append(claim_id)
    all_ids = _all_ids(data_list)
    # given that there is only one claim not overlapping
    no_overlapped_id = set(all_ids) - set(overlapped_ids)
    return no_overlapped_id.pop()
