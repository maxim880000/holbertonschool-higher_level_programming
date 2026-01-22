#!/usr/bin/python3
# This module provides a function that divides all elements of a matrix.

# The function validates the matrix structure and divides each element
# by a given number, rounding results to two decimal places.



def matrix_divided(matrix, div):
# Divide all elements of a matrix by a number.
# Returns a new matrix with elements rounded to 2 decimal places.

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
