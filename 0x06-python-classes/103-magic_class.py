#!/usr/bin/python3
"""Module for the MagicClass square."""


import math


class MagicClass:
    """
    This class represent a magicClass.

    Attributes:
        __radius (int or float): The circle's radius. It's a private attribute.

    Methods:
        size: A property that gets or sets the radius of the circle.
        area(): Returns the area of the circle.
        circumference(): Returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        The constructor for the MagicClass class.

        Parameters:
            radius (int or float, optional): Circle's radius. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (float or integer).
            ValueError: If radius is less than 0.
        """
        self.size = radius

    @property
    def size(self):
        """
        The size property.

        Returns:
            int or float: The radius of the circle.
        """
        return self.__radius

    @size.setter
    def size(self, value):
        """
        The size property setter.

        Parameters:
            value (int or float): The radius of the circle.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        elif value < 0:
            raise ValueError("radius must be >= 0")
        else:
            self.__radius = value

    def area(self):
        """
        The function to calculate the area of the circle.

        Returns:
            int or float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        The function to calculate the circumference of the circle.

        Returns:
            int or float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
