import os

from solution import claim_not_overlaped
from solution import shared_squares


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f'{current_path}/input', 'r') as input_file:
        input_text = input_file.read()
        print(f'Shared squares = {shared_squares(input_text)}')
        print(f'Claim not overlapped = {claim_not_overlaped(input_text)}')


if __name__ == '__main__':
    main()
