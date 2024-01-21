#!/usr/bin/python3
"""This module defines an inherited list class MyList."""


class MyList(list):
    """
    Class -- MyList
        Inherits from the built-in list class and implements sorted printing.

    Methods:
        print_sorted: Prints the list in sorted ascending order.
    """

    def print_sorted(self):
        """
        Method -- print_sorted
            Prints the list in sorted ascending order.

        Parameters:
            self -- The current MyList object

        Returns:
            None. But this will print the list in sorted ascending order.
        """
        print(sorted(self))
