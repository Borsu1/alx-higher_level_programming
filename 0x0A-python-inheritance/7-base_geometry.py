class BaseGeometry:
    """
    BaseGeometry is a base class with no attributes.

    Methods:
        area: Raises an Exception indicating the method is not implemented.
        integer_validator: Validates that a value is an integer and is greater
        than 0.
    """

    def area(self):
        """
        Raises an Exception. Message indicates that the method is not
        implemented.

        Raises:
            Exception: Always, as this method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and is greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
