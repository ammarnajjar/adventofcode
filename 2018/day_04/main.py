import os

from solution import choose_guard
from solution import guard_freq_alseep


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f'{current_path}/input', 'r') as input_file:
        input_text = input_file.read()
        print(f'Chosen guard = {choose_guard(input_text)}')
        print(f'Guard frequent sleep minute = {guard_freq_alseep(input_text)}')


if __name__ == '__main__':
    main()
