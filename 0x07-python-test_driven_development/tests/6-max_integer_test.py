#!/usr/bin/python3
import unittest

"""Module to find the max integer in a list"""


def max_integer(lst):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    for num in lst:
        if num > result:
            result = num
    return result


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_empty(self):
        """Checks that the function returns None for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        """Checks that the function returns the correct max integer"""
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([10, 5, 8]), 10)
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_single_element(self):
        """Checks that the function returns the correct result for a list with a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_max(self):
        """Checks that the function handles duplicate max values correctly"""
        self.assertEqual(max_integer([2, 4, 6, 6, 4, 2]), 6)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_negative_numbers(self):
        """Checks that the function handles negative numbers correctly"""
        self.assertEqual(max_integer([-5, -2, -7, -1]), -1)
        self.assertEqual(max_integer([-1, -10, -3, -5]), -1)

    def test_mixed_numbers(self):
        """Checks that the function handles mixed positive and negative numbers correctly"""
        self.assertEqual(max_integer([-5, 10, -3, 8]), 10)
        self.assertEqual(max_integer([0, 3, -2, 1]), 3)

    def test_float_numbers(self):
        """Checks that the function handles floating-point numbers correctly"""
        self.assertEqual(max_integer([1.5, 2.7, 0.9, 2.3]), 2.7)
        self.assertEqual(max_integer([-2.5, -1.1, -3.7]), -1.1)

    def test_string_values(self):
        """Checks that the function handles string values correctly"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")

    def test_mixed_values(self):
        """Checks that the function handles mixed numeric and string values correctly"""
        self.assertEqual(max_integer([1, 2, "a", 3, "b"]), 3)
        self.assertEqual(max_integer([1, "a", "b", 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()

