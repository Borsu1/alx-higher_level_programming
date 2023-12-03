#!/usr/bin/python3
import sys
def main():
    args = sys.argv[1:]
    num_args = len(args)
    print("Number of argument{}: {}".format('s' if num_args != 1 else '', num_args), end='.\n' if num_args == 0 else ':\n')
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
        if __name__ == "__main__":
            main()
