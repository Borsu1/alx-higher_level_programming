#!/usr/bin/python3
def islower(c):
    # Get the ASCII code of the character
    code = ord(c)
    # Return True if the code is between 97 and 122 (lowercase letters), False otherwise
    return 97 <= code <= 122
