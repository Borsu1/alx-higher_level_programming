#!/usr/bin/python3
class Square(Rectangle):
    """
    Square is a class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square. This is a private attribute.

    Methods:
        __init__: Initializes a new instance of the Square class.
        area: Returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
