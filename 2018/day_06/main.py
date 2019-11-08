import os

from solution import largest_area
from solution import region_size


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f'{current_path}/input', 'r') as input_file:
        input_text = input_file.read().strip()
        print(f'Largest area = {largest_area(input_text)}')
        print(f'Region size = {region_size(input_text, 10000)}')


if __name__ == '__main__':
    main()
