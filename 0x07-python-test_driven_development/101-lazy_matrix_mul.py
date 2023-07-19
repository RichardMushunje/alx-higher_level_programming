#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
=======
"""
Defines lazy_matrix function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ calculates the matrix multiplication of two matrices"""
    return numpy.matmul(m_a, m_b)
>>>>>>> 3718ea35554d77fff0fd6b0f2ed3d840c9010816
