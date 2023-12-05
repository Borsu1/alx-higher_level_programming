#!/usr/bin/python3
import calculator_1 as calc

def main():
    a = 10
    b = 5

    add = calc.add(a, b)
    sub = calc.sub(a, b)
    mul = calc.mul(a, b)
    div = calc.div(a, b)

    print(f"The sum of {a} and {b} is: {add}")
    print(f"The difference between {a} and {b} is: {sub}")
    print(f"The product of {a} and {b} is: {mul}")
    print(f"The division of {a} by {b} is: {div}")

if __name__ == "__main__":
    main()
