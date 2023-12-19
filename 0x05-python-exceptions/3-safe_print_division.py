#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Error: {}".format(str(e)))
    finally:
        print("Inside result: {}".format(result))
    return result
