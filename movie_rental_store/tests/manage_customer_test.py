import sys
sys.path.append('../src')

import unittest
from modules.customer import Customer
from modules.manage_customer import ManageCustomer

class ManageCustomerTest(unittest.TestCase):

    def setUp(self):
        """Setup method to instance an object of Customer class"""
        
        self.manage_customer = ManageCustomer("cust_001")
        self.customer = self.manage_customer.get_customer()    
        
    def test_create_manage_customer_with_required_data(self):
        """Test if an instance of Manage Customer class is created with required"""
        
        self.assertIsInstance(self.manage_customer, ManageCustomer)

    def test_read_first_name_from_console_and_update_customer_class(self):
        """Test if to read first name and update data in customer class"""

        self.manage_customer.read_first_name()
        self.assertNotEqual("", self.customer.get_first_name())
        
    def test_read_last_name_from_console_and_update_customer_class(self):
        """Test if to read last name and update data in customer class"""

        self.manage_customer.read_last_name()
        self.assertNotEqual("", self.customer.get_last_name())

    def test_read_date_of_birth_from_console_and_update_customer_class(self):
        """Test if to read date of birth and update data in customer class"""

        self.manage_customer.read_date_of_birth()
        self.assertNotEqual("", self.customer.get_date_of_birth())

    def test_read_addresses_from_console_and_update_customer_class(self):
        """Test if to read addresses and update data in customer class"""

        self.manage_customer.read_addresses()
        self.assertNotEqual([], self.customer.get_addresses())
        
    def test_read_phones_from_console_and_update_customer_class(self):
        """Test if to read phones and update data in customer class"""

        self.manage_customer.read_phones()
        self.assertNotEqual([], self.customer.get_phones())

    def test_read_membership_from_console_and_update_customer_class(self):
        """Test if to read membership and update data in customer class"""

        self.manage_customer.read_membership()
        self.assertNotEqual("", self.customer.get_membership())

    def test_read_status_from_console_and_update_customer_class(self):
        """Test if to read status and update data in customer class"""

        self.manage_customer.read_status()
        self.assertNotEqual("", self.customer.get_status())

        
if __name__ == "__main__":
    unittest.main()

