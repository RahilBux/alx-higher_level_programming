#!/usr/bin/python3
"""Unittests for max int list"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """Unittest for max integer function"""

    def test_order_list(self):
        """Test ordered list of ints"""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unorder_list(self):
        """Test an unorder list of ints"""
        unorder = [1, 3, 2, 4]
        self.assertEqual(max_integer(unorder), 4)

    def test_max_beg(self):
        """Test list with beginning max"""
        max_beg = [4, 2, 1, 3]
        self.assertEqual(max_integer(max_beg), 4)

    def test_empty(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_elem(self):
        """test a list with one element"""
        one_elem = [8]
        self.assertEqual(max_integer(one_elem), 8)

    def test_float(self):
        """tests a list with floats"""
        floats = [1.52, 15.3, -9.04, 6.7, 12.98]
        self.assertEqual(max_integer(floats), 15.3)

    def test_int_and_float(self):
        """tests a list of ints and floats"""
        int_float = [1.56, 7, 8.75, -4]
        self.assertEqual(max_integer(int_float), 8.75)

    def test_string(self):
        """Tests the string"""
        string = "Brendan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_strings(self):
        """Tests a list of strings"""
        strings = ["Brendan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Tests an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
