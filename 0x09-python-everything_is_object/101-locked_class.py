#!/usr/bin/python3
"""
This module contains the LockedClass.
"""

class LockedClass:
    """
    The LockedClass only allows setting the attribute 'first_name'.
    """
    __slots__ = ['first_name']
