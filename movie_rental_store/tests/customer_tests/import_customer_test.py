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
        self.customers = self.import_customer.import_customer_csv_file(self.customer_file_path)

    def test_create_import_customer_object(self):
        """Test to verify instance if ImportCustomer"""

        self.assertIsInstance(self.import_customer, ImportCustomer)

    def test_import_csv_file_return_customer_object(self):
        """Test to verify that a customer list is getting after reading csv file"""

        self.assertIsInstance(self.customers[0], Customer)

    def test_import_csv_file_return_empty_customer_object(self):
        """Test to verify an empty list of customer is getting when csv file is empty"""

        empty_customers = self.import_customer.import_customer_csv_file(self.empty_customer_file_path)
        self.assertEqual([], empty_customers)

    def test_import_customer_without_data(self):
        """Test to verify that a customer is created with code only and empty data"""

        customer = self.import_customer.create_customer_object("cust002010", {})
        self.assertIsInstance(customer, Customer)

    def test_data_when_import_customer_with_data(self):
        """Test to verify that a data for customer is according csv file"""

        customer = self.customers[0]
        self.assertEqual("Jimena", customer.get_first_name())
        self.assertEqual("Sanabria", customer.get_last_name())
        self.assertEqual("21-08-1980", customer.get_date_of_birth())
        self.assertEqual(["Nueva Granada #1837"], customer.get_addresses())
        self.assertEqual([4244270,70759942], customer.get_phones())
        self.assertEqual("giovi_times@hotmail.com", customer.get_email())
        self.assertEqual("Gold", customer.get_membership())
        self.assertEqual("Active", customer.get_status())

if __name__ == "__main__":
    unittest.main()
