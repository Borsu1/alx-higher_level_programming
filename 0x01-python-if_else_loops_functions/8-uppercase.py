#!/usr/bin/python3
def uppercase(str):
    result = "i"
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print("The original string is: %s" % str)
    print("The string in uppercase is: %s" % result)
