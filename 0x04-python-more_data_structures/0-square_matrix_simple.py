#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions
    new_matrix = []
    for i in range(len(matrix)):
        # For each row, create a new row
        new_row = []
        for j in range(len(matrix[i])):
            # Square each element and add it to the new row
            new_row.append(matrix[i][j] ** 2)
        # Add the new row to the new matrix
        new_matrix.append(new_row)
    return new_matrix
