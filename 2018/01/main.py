#!/usr/bin/env python
from solution import first_frequesncy_reached_twice
from solution import sum_lines


def main():
    with open("input", "r") as fi:
        content_text = fi.read()
        freq = sum_lines(content_text)
        print(f"Resulting frequency = {freq}")
        freq = first_frequesncy_reached_twice(content_text)
        print(f"First frequency reached twice= {freq}")


if __name__ == "__main__":
    main()
