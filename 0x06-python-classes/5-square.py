#!/usr/bin/python3

  """This is a class for defining a square."""
  class Square:
    """
    Attributes:
        __size (int): The size of the square. It's a private attribute.

    Methods:
        size: A property that gets or sets the size of the square.
        area(): Returns the area of the square.
        my_print(): Prints the square using the "#" character.
    """

        """The constructor for the Square class."""
    def __init__(self, size=0):
        """
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

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
        """The function to calculate the area of the square."""
    def area(self):
        """
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
            for _ in range(self.__size):
                print("#" * self.__size)
