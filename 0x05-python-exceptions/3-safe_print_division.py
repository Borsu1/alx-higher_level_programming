#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Inside result: {}".format(div))
    return div
