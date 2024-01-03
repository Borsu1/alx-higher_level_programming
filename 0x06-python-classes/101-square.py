#!/usr/bin/python3
class Square:
    """
    This is a class for defining a square.

    Attributes:
        __size (int): The size of the square. It's a private attribute.
        __position (tuple): The position of the square. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        position: A property that gets or sets the position of the square.
        area(): Returns the area of the square.
        my_print(): Prints the square using the "#" character.
        __str__(): Returns a string representation of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        The size property.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size property setter.

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

    @property
    def position(self):
        """
        The position property.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The position property setter.

        Parameters:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        The function to calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        The function to print the square using the "#" character.

        Prints:
            str: The square represented by the "#" character. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))

    def __str__(self):
        """
        The function to return a string representation of the square.

        Returns:
            str: The square represented by the "#" character. If size is 0, returns an empty string.
        """
        if self.__size == 0:
            return ""
        else:
            return "\n" * self.__position[1] + "\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size))
