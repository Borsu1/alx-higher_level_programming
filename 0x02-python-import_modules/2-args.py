#!/usr/bin/python3
import sys

def main():
    num_args = len(sys.argv) - 1
    print("Number of argument{}: {}".format('s' if num_args != 1 else '', num_args), end='.\n' if num_args == 0 else ':\n')
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
