#!/usr/bin/python3
import sys


def main():
    sum_args = sum(int(arg) for arg in sys.argv[1:])
    print(sum_args)


if __name__ == "__main__":
    main()
