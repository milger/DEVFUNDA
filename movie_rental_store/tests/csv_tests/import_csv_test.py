"""Unit Test."""

import sys
sys.path.append('../../src')

import unittest
import csv
from utils.csv_handler.import_csv_file import get_file_name
from utils.csv_handler.import_csv_file import get_file_data
from utils.csv_handler.import_csv_file import parse_csv_file


class ImportCsvTest(unittest.TestCase):
    """Unit Tests to test method from import_csv_file utility."""

    def test_get_file_name_distinct_folder(self):
        """Test get file name when that is other folder"""

        file_name = get_file_name("csv_files/test.csv")
        self.assertEqual("test.csv", file_name)

    def test_get_file_name_from_same_folder(self):
        """Test get file name when that is in same folder"""

        file_name = get_file_name("test_empty.csv")
        self.assertEqual("test_empty.csv", file_name)

    def test_get_data_of_file(self):
        """Test get a list with dictionary (key:value)"""

        import_file = open("test.csv", "rb")
        reader_file = csv.DictReader("test.csv")
        complete_data = get_file_data(reader_file)
        import_file.close()
        self.assertNotEqual([], complete_data)

    def test_import_csv_file_empty(self):
        """Test the parse of an empty csv file"""

        complete_data = parse_csv_file("test_empty.csv")
        self.assertEqual([], complete_data)

    def test_import_csv_file_filled(self):
        """Test the parse of csv file"""

        complete_data = parse_csv_file("test.csv")
        self.assertNotEqual([], complete_data)

    def test_import_csv_file_first_row(self):
        """Test the parse of csv file and get first row"""

        expected_data = {"Measure":"SIM_BASE_PRICE1",
                         "Scope":"VP02/Arlington",
                         "Error":"The formula could not be evaluated"}
        complete_data = parse_csv_file("csv_files/test.csv")
        self.assertEqual(expected_data, complete_data[0])

    def test_import_csv_file_last_row(self):
        """Test the parse of csv file and get last row"""

        expected_data = {"Measure":"SIM_BASE_PRICE4",
                         "Scope":"VP01/Arlington",
                         "Error":"The formula could not be evaluated"}
        complete_data = parse_csv_file("test.csv")
        self.assertEqual(expected_data, complete_data[3])

if __name__ == "__main__":
    unittest.main()
