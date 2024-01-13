#!/usr/bin/python3
"""This is a class for defining a square."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square. It's a private attribute.
        __position (tuple): Position of the square. It's a private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""
        else:
            return ("\n" * self.__position[1] +
                    "\n".join(" " * self.__position[0] + "#" * self.__size
                              for _ in range(self.__size)))
