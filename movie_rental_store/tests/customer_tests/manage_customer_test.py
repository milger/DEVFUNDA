"""Unit test for manage_customer file"""
import sys
import os
import __builtin__
sys.path.append(os.path.abspath("../../src"))

import unittest
import datetime
from modules.entity.customer import Customer
from modules.handler.manage_customer import ManageCustomer

class ManageCustomerTest(unittest.TestCase):
    """Unit test for ManageCustomer class"""

    def setUp(self):
        """Setup method to instance an object of Customer class"""

        self.manage_customer = ManageCustomer("cust_001")
        self.customer = self.manage_customer.get_customer()

    def test_create_manage_customer_with_required_data(self):
        """Test if an instance of Manage Customer class is created with required"""

        self.assertIsInstance(self.manage_customer, ManageCustomer)

    def test_read_first_name_from_console_and_update_customer_class(self):
        """Test if to read first name and update data in customer class"""
        __builtin__.raw_input = lambda _: "Andrea"
        self.manage_customer.read_first_name()
        self.assertEqual("Andrea", self.customer.get_first_name())

    def test_read_last_name_from_console_and_update_customer_class(self):
        """Test if to read last name and update data in customer class"""

        __builtin__.raw_input = lambda _: "Serna"
        self.manage_customer.read_last_name()
        self.assertEqual("Serna", self.customer.get_last_name())

    def test_read_date_of_birth_from_console_and_update_customer_class(self):
        """Test if to read date of birth and update data in customer class"""

        __builtin__.raw_input = lambda _: "21-08-1980"
        self.manage_customer.read_date_of_birth()
        date = datetime.datetime.strptime("21-08-1980", "%d-%m-%Y")
        self.assertEqual(date, self.customer.get_date_of_birth())

    def test_read_addresses_from_console_and_update_customer_class(self):
        """Test if to read addresses and update data in customer class"""

        __builtin__.input = lambda _: 1
        __builtin__.raw_input = lambda _s: "Nueva Granada #123"
        self.manage_customer.read_addresses()
        self.assertEqual(["Nueva Granada #123"], self.customer.get_addresses())

    def test_read_phones_from_console_and_update_customer_class(self):
        """Test if to read phones and update data in customer class"""

        __builtin__.input = lambda _: 1
        self.manage_customer.read_phones()
        self.assertEqual([1], self.customer.get_phones())

    def test_read_membership_from_console_and_update_customer_class(self):
        """Test if to read membership and update data in customer class"""

        __builtin__.raw_input = lambda _: "Gold"
        self.manage_customer.read_membership()
        self.assertEqual("Gold", self.customer.get_membership())

    def test_read_status_from_console_and_update_customer_class(self):
        """Test if to read status and update data in customer class"""

        __builtin__.raw_input = lambda _: "Active"
        self.manage_customer.read_status()
        self.assertEqual("Active", self.customer.get_status())


if __name__ == "__main__":
    unittest.main()
