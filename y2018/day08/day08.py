"""Part 1"""
import os


def part1(input_text: str) -> int:
    nodes = []
    rest = [int(c) for c in input_text.strip().split()]
    while rest:
        n_child = rest[0]
        n_meta = rest[1]
        if n_child > 0 and n_meta > 0:
            meta = rest[-n_meta:]
            rest = rest[2:-n_meta]
        else:
            meta = rest[2:2 + n_meta]
            rest = rest[2 + n_meta:]
        nodes.append((n_child, n_meta, meta))
    return sum(
        sum(n[2]) for n in nodes
    )


if __name__ == '__main__':  # pragma no cover
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_path}/input08', 'r') as input_file:
        input_text = input_file.read().strip()
    # solution between 55110 and 35713
    print(part1(input_text))
