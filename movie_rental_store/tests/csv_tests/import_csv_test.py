"""Unit Test."""

import sys
sys.path.append('../../src')

import unittest
from utils.csv_handler.import_csv_file import parse_csv_file

class ImportCsvTest(unittest.TestCase):
    """Unit Tests to test method from import_csv_file utility."""

    def test_import_csv_file_empty(self):
        """Test the parse of an emty csv file"""

        complete_data = parse_csv_file("test_empty")
        self.assertEqual([], complete_data)

    def test_import_csv_file_filled(self):
        """Test the parse of csv file"""

        complete_data = parse_csv_file("test")
        self.assertNotEqual([], complete_data)

    def test_import_csv_file_first_row(self):
        """Test the parse of csv file and get first row"""

        expected_data = {"Measure":"SIM_BASE_PRICE1",
                         "Scope":"VP02/Arlington",
                         "Error":"The formula could not be evaluated"}
        complete_data = parse_csv_file("test")
        self.assertEqual(expected_data, complete_data[0])

    def test_import_csv_file_last_row(self):
        """Test the parse of csv file and get last row"""

        expected_data = {"Measure":"SIM_BASE_PRICE4",
                         "Scope":"VP01/Arlington",
                         "Error":"The formula could not be evaluated"}
        complete_data = parse_csv_file("test")
        self.assertEqual(expected_data, complete_data[3])

if __name__ == "__main__":
    unittest.main()

