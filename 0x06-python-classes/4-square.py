#!/usr/bin/python3
"""This is a class for defining a square."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        area(): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
