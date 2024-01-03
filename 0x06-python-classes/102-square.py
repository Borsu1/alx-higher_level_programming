#!/usr/bin/python3
class Square:
    """
    This is a class for defining a square.

    Attributes:
        __size (int or float): The size of the square. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        area(): Returns the area of the square.
        __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__(): Allow a Square instance to answer to comparators based on the square area.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
            size (int or float, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        The size property.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size property setter.

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

    def __eq__(self, other):
        """
        The function to check if two squares are equal based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the two squares have the same area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        The function to check if two squares are not equal based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the two squares have different areas, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        The function to check if a square is less than another square based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square has a smaller area than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        The function to check if a square is less than or equal to another square based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square has a smaller or equal area than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """
        The function to check if a square is greater than another square based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square has a larger area than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        The function to check if a square is greater than or equal to another square based on their areas.

        Parameters:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square has a larger or equal area than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
