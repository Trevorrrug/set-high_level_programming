#!/usr/bin/python3
"""Multiply two matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the matrix product computed by NumPy."""
    return np.matmul(m_a, m_b)
