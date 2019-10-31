#!/usr/bin/env python
import os

from solution import shared_squares


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f"{current_path}/input", "r") as fi:
        input_text = fi.read()
        print(f"Shared Squares = {shared_squares(input_text)}")


if __name__ == "__main__":
    main()
