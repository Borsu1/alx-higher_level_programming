#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    BaseGeometry is a base class with no attributes.

    Methods:
        area: Raises an Exception indicating the method is not implemented.
    """

    def area(self):
        """
        Raises an Exception. Message indicates that the method is not
        implemented.

        Raises:
            Exception: Always, as this method is not implemented.
        """
        raise Exception("area() is not implemented")
