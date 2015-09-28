"""Unit test for input_validation utility"""
import sys
import os
sys.path.append(os.path.abspath("../../src"))
import datetime
import __builtin__
import unittest
from utils.input_validation import *

class InputValidationTest(unittest.TestCase):
    """Test cases to cover input_validation utility"""

    def test_correct_type_date_input(self):
        """Test the type of date correctly as datetime"""
        __builtin__.raw_input = lambda _: "21-08-1980"
        date = get_date_input("Date")
        self.assertEqual(type(date), datetime.datetime)

    def test_date_input(self):
        """Test the date input value"""

        __builtin__.raw_input = lambda _: "21-08-1980"
        expected_date = datetime.datetime.strptime("21-08-1980", "%d-%m-%Y")
        date = get_date_input("Date")
        self.assertEqual(expected_date, date)

    def test_correct_type_integer_input(self):
        """Test the type of integer number correctly as int"""

        __builtin__.input = lambda _: 28
        number = get_integer_input("Integer Number")
        self.assertEqual(type(number), int)

    def test_correct_integer_input(self):
        """Test the integer input value"""

        __builtin__.input = lambda _: 1
        number = get_integer_input("Integer Number")
        self.assertEqual(1, number)

    def test_correct_option_in_list(self):
        """Test the option selected is in list"""
        abc_list = ["a", "b", "c"]
        __builtin__.raw_input = lambda _: "b"
        option = get_option_input("Options", abc_list)
        self.assertEqual("b", option)

    def test_wrong_option_in_list(self):
        """Test the option selected is not list"""
        number_list = ["1", "2", "3"]
        __builtin__.raw_input = lambda _: "2"
        option = get_option_input("Options", number_list)
        self.assertNotEqual("b", option)


if __name__ == "__main__":
    unittest.main()
