#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Check if key is a string
    if not isinstance(key, str):
        print("Error: key must be a string")
        return

    # Update the dictionary
    a_dictionary[key] = value
