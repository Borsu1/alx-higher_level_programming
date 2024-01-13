#!/usr/bin/python3
"""This is a class module for a square."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square. It's a private attribute.
        __position (tuple): The square's position. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        position: A property that gets or sets the position of the square.
        area(): Returns the area of the square.
        my_print(): Prints the square using the "#" character.
    """

    """The constructor for the Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): Square's position. Defaults to (0, 0).

        Raises:
            TypeError: Size must be int, position a tuple of 2 positive ints.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

        """The size property."""
    @property
    def size(self):
        """
        Returns:
            int: The size of the square.
        """
        return self.__size

        """The size property setter."""
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

        """The position property."""
    @property
    def position(self):
        """
        Returns:
            tuple: The position of the square.
        """
        return self.__position

        """The position property setter."""
    @position.setter
    def position(self, value):
        """
        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

        """The function to calculate the area of the square."""
    def area(self):
        """
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

        """The function to print the square using the "#" character.""""
    def my_print(self):
        """
        Prints:
            str: Square represented by "#". If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size
                            for _ in range(self.__size)))
