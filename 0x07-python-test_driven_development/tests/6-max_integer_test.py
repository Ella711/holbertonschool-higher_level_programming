#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        # Test max integers when passed lists and digits
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 5, 9, 5]), 9)
        self.assertEqual(max_integer([9, 5]), 9)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-6, -9, -2, 0]), 0)
        self.assertEqual(max_integer([-6, -9, -2, -3]), -2)
        self.assertEqual(max_integer((2, 4)), 4)

    def test_max_string(self):
        # Test different string values
        self.assertEqual(max_integer(["5", "7", "9"]), "9")
        self.assertEqual(max_integer(["Hello", "Good", "Bye"]), "Hello")
        self.assertEqual(max_integer("5"), "5")
        self.assertEqual(max_integer("4567"), "7")
        self.assertEqual(max_integer("abcxyz"), "z")
        self.assertEqual(max_integer(["a", "b", "c", "d", "e", "y", "z"]), "z")
        self.assertEqual(max_integer(["abc", "y"]), "y")

    def test_list_floats(self):
        # Tests floats and lists
        self.assertEqual(max_integer([[1, 2], [2, 3]]), [2, 3])
        self.assertEqual(max_integer([{1, 2}, {2}, {3, 4}]), {1, 2})
        self.assertEqual(max_integer([-6.1, -9.8, -2.5, -3.7]), -2.5)

    def test_None(self):
        # Test max integers when list is empty
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_errors(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1, 5)
