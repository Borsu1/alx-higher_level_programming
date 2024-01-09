#!/usr/bin/python3


class MyList(list):
    """
    Print the elements of the list in ascending order.
    """

    def print_sorted(self):
        print(sorted(self))
