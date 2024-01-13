#!/usr/bin/python3
"""This is a class for defining a square."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int or float): The square's size. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        area(): Returns the area of the square.
        __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__(): Allow
        Square instance to answer to comparators based on the square area.
    """

    """The constructor for the Square class"""
    def __init__(self, size=0):
        """
        Parameters:
            size (int or float, optional): The square's size. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

        """The size property."""
    @property
    def size(self):
        """
        Returns:
            int or float: The size of the square.
        """
        return self.__size

        """The size property setter."""
    @size.setter
    def size(self, value):
        """
        Parameters:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        The function to calculate the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2
        """The function to check if two squares are equal based on their areas.
        """

    def __eq__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the two squares have the same area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

        """Function checks if two squares are not equal based on their areas.
        """
    def __ne__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if two squares have different areas, False otherwise.
        """
        return not self.__eq__(other)

        """Function checks if one square's area is less than another's."""
    def __lt__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if square's area is smaller than another's,
            False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

        """Function checks if square's area is less than or equal to another's.
        """
    def __le__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
        bool: True if square's area is less or equal to another's,
        False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

        """"Function checks if a square's area is greater than another's.
        """
    def __gt__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
            "bool: True if square's area is larger than another's,
            False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

        """Function checks square's area is greater or equal to another's."""
    def __ge__(self, other):
        """
        Parameters:
            other (Square): The other square to compare with.

        Returns:
            "bool: True if square's area is larger or equal to another's,
            False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
