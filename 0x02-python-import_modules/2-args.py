#!/usr/bin/python3
import sys

def print_args():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of arguments: 0.")
    elif num_args == 1:
        print("Number of argument: 1:")
        print("1: " + sys.argv[1])
    else:
        print("Number of arguments: " + str(num_args) + ":")
        for i in range(1, num_args + 1):
            print(str(i) + ": " + sys.argv[i])

if __name__ == "__main__":
    print_args()
