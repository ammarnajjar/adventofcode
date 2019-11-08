import os

from solution import first_frequesncy_reached_twice
from solution import sum_lines


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f'{current_path}/input', 'r') as input_file:
        content_text = input_file.read()
        freq = sum_lines(content_text)
        print(f'Resulting frequency = {freq}')
        freq = first_frequesncy_reached_twice(content_text)
        print(f'First frequency reached twice= {freq}')


if __name__ == '__main__':
    main()
