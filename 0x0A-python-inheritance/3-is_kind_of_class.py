#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or if the object is an
    instance of a class that inherited from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with the type of obj.

    Returns:
    bool: True if obj is an instance of a_class or a subclass of a_class,
    False otherwise.
    """

    return isinstance(obj, a_class)
