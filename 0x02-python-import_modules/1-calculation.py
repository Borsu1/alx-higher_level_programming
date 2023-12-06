#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    sum_result = add(a, b)
    print("The sum of a and b is:", sum_result)

    diff_result = sub(a, b)
    print("The difference of a and b is:", diff_result)

    prod_result = mul(a, b)
    print("The product of a and b is:", prod_result)

    quot_result = div(a, b)
    print("The quotient of a and b is:", quot_result)


if __name__ == "__main__":
    main()
