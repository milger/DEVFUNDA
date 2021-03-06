"""Unit Test."""

import sys
import os
sys.path.append(os.path.abspath("../../src"))

import unittest
import csv
from utils.csv_handler.import_csv_file import *

class ImportCsvTest(unittest.TestCase):
    """Unit Tests to test method from import_csv_file utility."""

    def setUp(self):
        """Setup method to get the path to csv files to test them"""

        self.expected_data = {"Measure":"SIM_BASE_PRICE1",
                         "Scope":"VP02/Arlington",
                         "Error":"The formula could not be evaluated",
                         "Number":"5"}
                         
        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_file = dir_name + "/csv_files"
        self.test_file_path = path_file + "/test.csv"
        self.test_empty_file_path = path_file + "/test_empty.csv"

    def test_get_data_of_file(self):
        """Test get a list with dictionary (key:value)"""
        import_file = open(self.test_file_path, "rb")
        reader_file = csv.DictReader(import_file)
        complete_data = get_file_data(reader_file)
        import_file.close()
        self.assertNotEqual([], complete_data)

    def test_import_csv_file_empty(self):
        """Test the parse of an empty csv file"""

        complete_data = parse_csv_file(self.test_empty_file_path)
        self.assertEqual([], complete_data)

    def test_import_csv_file_filled(self):
        """Test the parse of csv file"""

        complete_data = parse_csv_file(self.test_file_path)
        self.assertNotEqual([], complete_data)

    def test_import_csv_file_a_row(self):
        """Test the parse of csv file and get first row"""

        complete_data = parse_csv_file(self.test_file_path)
        self.assertEqual(self.expected_data, complete_data[0])

    def test_a_list_of_string_is_get_in_dictionary(self):
        """Test the list of string is get in a dictionary"""

        list_getter = get_string_list_data(self.expected_data, "Scope")
        self.assertEqual(["VP02/Arlington"], list_getter)

    def test_a_list_of_integers_is_get_in_dictionary(self):
        """Test the list of integers is get in a dictionary"""
        
        list_getter = get_integer_list_data(self.expected_data, "Number")
        self.assertEqual([5], list_getter)

if __name__ == "__main__":
    unittest.main()