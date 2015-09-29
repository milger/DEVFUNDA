"""Unit test for import_customer file"""
import sys
import os
sys.path.append(os.path.abspath("../../src"))

import unittest
from modules.entity.customer import Customer
from modules.handler.import_customer import ImportCustomer

class ImportCustomerTest(unittest.TestCase):
    """Unit test for ImportCustomer class"""

    def setUp(self):
        """Setup method to instance an object of Customer class and get file paths"""

        self.import_customer = ImportCustomer()
        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_file = dir_name + "/csv_files"
        self.customer_file_path = path_file + "/customer.csv"
        self.empty_customer_file_path = path_file + "/empty_customer.csv"

    def test_create_import_customer_object(self):
        """Test to verify instance if ImportCustomer"""

        self.assertIsInstance(self.import_customer, ImportCustomer)

    def test_import_csv_file_return_customer_object(self):
        """Test to verify that a customer list is getting after reading csv file"""

        customers = self.import_customer.import_customer_csv_file(self.customer_file_path)
        self.assertIsInstance(customers[0], Customer)

    def test_import_csv_file_return_empty_customer_object(self):
        """Test to verify an empty list of customer is getting when csv file is empty"""

        customers = self.import_customer.import_customer_csv_file(self.empty_customer_file_path)
        self.assertEqual([], customers)

    def test_import_customer_without_data(self):
        """Test to verify that a customer is created with code only and empty data"""

        customer = self.import_customer.create_customer_object("cust002010", {})
        self.assertIsInstance(customer, Customer)


if __name__ == "__main__":
    unittest.main()
