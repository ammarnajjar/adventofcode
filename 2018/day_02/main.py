#!/usr/bin/env python
import os

from solution import checksum
from solution import common_letters_between_correct_codes as common


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f"{current_path}/input", "r") as fi:
        input_text = fi.read()
        print(f"Checksum = {checksum(input_text)}")
        print(f"Common Letters = {common(input_text)}")


if __name__ == "__main__":
    main()
