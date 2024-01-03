#!/usr/bin/python3
class Square:
    """
    This class defines a square.

    Attributes:
        size (int): The size of the square.
    Usage:
        To create a square object, simply instantiate the Square class with a size parameter.
        For example:
            square = Square(5)
    """
    def __init__(self, size):
        self.__size = size
