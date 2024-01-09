#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """
    Rectangle is a class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle. This is a private attribute.
        __height (int): The height of the rectangle. This a private attribute.

    Methods:
        __init__: Initializes a new instance of the Rectangle class.
        area: Returns the area of the rectangle.
        __str__: Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
