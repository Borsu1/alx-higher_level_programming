#!/usr/bin/python3

"""
This module provides a function to look up the attributes and methods of an object.

Functions:
----------
lookup(obj: object) -> list:
    Returns a list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns list of available attributes and methods of an object.

    Parameters:
    obj (object): The object whose attributes and methods you want to find.

    Returns:
    list: A list of strings with names of the object's attributes and methods.
    """
    return dir(obj)
