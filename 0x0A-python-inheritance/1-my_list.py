#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list clas"""

    def print_sorted(self):
        """Print the elements of the list in ascending order."""
        print(sorted(self))
