#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    This function updates a dictionary by adding a new key/value pair or replacing the value of an existing key.

    Parameters:
    a_dictionary (dict): The dictionary to update.
    key (str): The key to add or update in the dictionary.
    value: The value to associate with the key.

    Returns:
    dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
