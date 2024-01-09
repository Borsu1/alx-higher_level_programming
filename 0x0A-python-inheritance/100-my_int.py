#!/usr/bin/python3
class MyInt(int):
    """
    MyInt is a class that inherits from int.

    MyInt is a rebel. It has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other (int): The other integer to compare with.

        Returns:
            bool: True if self and other are not equal, False otherwise.
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other (int): The other integer to compare with.

        Returns:
            bool: True if self and other are equal, False otherwise.
        """
        return int.__eq__(self, other)
