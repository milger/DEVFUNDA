import sys
import os
sys.path.append(os.path.abspath("../../src"))


import unittest
from utils.csv_operations import CsvOperations


class CsvTest(unittest.TestCase):
    """ Class to test if the read and write operationes in csv are working fine"""
    
    def setUp(self):
        """For the test there is a file memberships.csv that contains the following information
        
        1, Gold, 10
        2, Platinum,5
        3, Bronze,0
        
        """    
        self.file_name = "memberships.csv"
        self.empty_file = "empty.csv"
        self.inexistent_file = "xxx.csv"
        
        
    def test_read_empty_file(self):
        """ test that empty list is returned when an empty file is read"""
        self.assertEqual(CsvOperations.read_data(self.empty_file), [])
    
    def test_read_inexistent_file(self):
        """ test that none data is returned when inexistent file is read"""
        self.assertEqual(CsvOperations.read_data(self.inexistent_file), None)
        
    def test_read_data_from_csv(self):
        """ test that all data are being read from csv file"""
        self.assertEqual(CsvOperations.read_data(self.file_name)[0], ["1", "Gold", "10"])
        self.assertEqual(CsvOperations.read_data(self.file_name)[1], ["2", "Platinum", "5"])
        self.assertEqual(CsvOperations.read_data(self.file_name)[2], ["3", "Bronze", "0"])
        
    def test_write_data_in_csv(self):
        """ Test that all data are wrote in the csv file"""
        expected = [["uno", "dos", "tres"], ["cuatro", "cinco", "seis"]]
        CsvOperations.write_data("test.csv", expected)
        self.assertEqual(CsvOperations.read_data("test.csv"), expected)
    
        
if __name__ == "__main__":
    unittest.main()
