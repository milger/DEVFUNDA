import sys
sys.path.append('../src')

import unittest
from utils.input_validation import *

class InputValidationTest(unittest.TestCase):
  
        
    def test_correct_type_date_input(self):
        """Test the type of date correctly as datetime"""

        date = get_date_input("Date")
        self.assertEqual(type(date), datetime.datetime)

    def test_wrong_type_date_input(self):
        """Test the type of date wrong as str"""

        date = get_date_input("Date")
        self.assertNotEqual(type(date), str)

    def test_correct_type_integer_input(self):
        """Test the type of integer number correctly as int"""

        number = get_integer_input("Integer Number")
        self.assertEqual(type(number), int)

    def test_wrong_type_integer_input(self):
        """Test the type of integer number wrong as str"""

        number = get_integer_input("Integer Number")
        self.assertNotEqual(type(number), str)

    def test_correct_option_in_list(self):
        """Test the option selected is in list"""
        abc_list = ["a", "b", "c"]
        print abc_list
        option = get_option_input("Options", abc_list)
        self.assertTrue(option in abc_list)

    def test_wrong_option_in_list(self):
        """Test the option selected is not list"""
        abc_list = ["a", "b", "c"]
        number_list = ["1", "2", "3"]
        print number_list
        option = get_option_input("Options", number_list)
        self.assertFalse(option in abc_list)

        
        
if __name__ == "__main__":
    unittest.main()

