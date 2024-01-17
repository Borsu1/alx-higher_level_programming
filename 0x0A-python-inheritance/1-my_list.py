#!/usr/bin/python3
"""Defines an inherited list class MyList."""


Class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascendingorder."""
        print(sorted(self))
