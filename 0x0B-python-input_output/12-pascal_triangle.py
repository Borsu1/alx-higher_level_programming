#!/usr/bin/python3
"""Defines a Pascal triangle"""


def pascal_triangle(n):
    """
    This function generates Pascal's triangle up to n rows.

    Parameters:
    n (int): The number of rows of Pascal's triangle to generate.

    Returns:
    list: A list of lists of integers representing Pascal's triangle up to n rows.
          Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
        row.append(1)
        triangle.append(row)

    return triangle
