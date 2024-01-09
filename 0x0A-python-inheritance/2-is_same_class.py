#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with the type of obj.

    Returns:
    bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
