#!/usr/bin/python3
"""Multiply two matrices using Python lists."""


def matrix_mul(m_a, m_b):
    """Return the matrix product of ``m_a`` and ``m_b``."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(value, (int, float))
               for row in m_a for value in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(value, (int, float))
               for row in m_b for value in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(m_a[row][k] * m_b[k][column]
                 for k in range(len(m_b)))
             for column in range(len(m_b[0]))]
            for row in range(len(m_a))]
