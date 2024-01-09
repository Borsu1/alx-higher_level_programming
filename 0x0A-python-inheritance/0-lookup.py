#!/usr/bin/python3
def lookup(obj):
    """
    Returns list of available attributes and methods of an object.

    Parameters:
    obj (object): The object whose attributes and methods you want to find.

    Returns:
    list: A list of strings wit names of the object's attributes and methods.
    """
    return dir(obj)
