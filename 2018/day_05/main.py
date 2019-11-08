import os

from solution import chars_after_reactions
from solution import min_chars_after_reactions


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f'{current_path}/input', 'r') as input_file:
        input_text = input_file.read().strip()
        print(f'Len after reactions = {chars_after_reactions(input_text)}')
        print(f'Min after reactions = {min_chars_after_reactions(input_text)}')


if __name__ == '__main__':
    main()
