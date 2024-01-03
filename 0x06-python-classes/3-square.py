#!/usr/bin/python3
"""This is a class for defining a square."""
class Square:
    """
    Attributes:
        __size (int): The size of the square. It's a private attribute.

    Methods:
        area(): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The function to calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
