#!/usr/bin/env python
from solution import checksum


def main():
    with open("input", "r") as fi:
        input_text = fi.read()
        print(f"Checksum = {checksum(input_text)}")


if __name__ == "__main__":
    main()
