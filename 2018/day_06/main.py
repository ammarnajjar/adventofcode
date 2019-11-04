#!/usr/bin/env python
import os

from solution import largest_area


current_path = os.path.dirname(os.path.realpath(__file__))


def main():
    with open(f"{current_path}/input", "r") as fi:
        input_text = fi.read().strip()
        print(f"Largest area = {largest_area(input_text)}")


if __name__ == "__main__":
    main()
