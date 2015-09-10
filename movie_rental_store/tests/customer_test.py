import sys
sys.path.append('../src')

import unittest
from modules.customer import Customer

class CustomerTest(unittest.TestCase):

    def setUp(self):
        """Setup method to instance an object of Customer class"""
        
        code = "cust_002"
        first_name = "Jimena"
        last_name = "Sanabria"
        date_of_birth = "21/08/1980"
        address_1 = "Calle Nueva Granada #1837"
        phone_1 = "70759942"
        phone_2 = "4295449"
        email = "giovi_times@hotmail.com"
        membership = "Gold"
        status = "ACTIVE"

        self.required_customer = Customer("cust_001", "Andrea", "Vargas", "01/01/2000") 
        self.customer = Customer(code, first_name, last_name, date_of_birth, [address_1], [phone_1, phone_2], email, membership, status)
        
    def test_create_customer_with_required_data(self):
        """Test if an instance of Customer class is created with required"""
        self.assertIsInstance(self.required_customer, Customer)
        
    def test_update_name_of_required_customer(self):
        """Test to update the first_name attribute"""
        update_name = "Pamela"
        self.required_customer.set_first_name(update_name)
        self.assertEqual(update_name, self.required_customer.get_first_name())
        
    def test_update_last_name_of_required_customer(self):
        """Test to update the last_name attribute"""
        update_last_name = "Veizaga"
        self.required_customer.set_last_name(update_last_name)
        self.assertEqual(update_last_name, self.required_customer.get_last_name())
        
    def test_update_date_of_birth_of_required_customer(self):
        """Test to update the date_of_birth attribute"""
        update_date_of_birth = "01/10/2001"
        self.required_customer.set_date_of_birth(update_date_of_birth)
        self.assertEqual(update_date_of_birth, self.required_customer.get_date_of_birth())
        
    def test_add_addresses_of_required_customer(self):
        """Test to add addresses attribute"""
        addresses = ["Calle Melchor Perez #3232", "Av. Blanco Galindo"]
        self.required_customer.set_addresses(addresses)
        self.assertEqual(addresses, self.required_customer.get_addresses())
        
    def test_add_phones_of_required_customer(self):
        """Test to add phones attribute"""
        phones = ["3254789", "7894789"]
        self.required_customer.set_phones(phones)
        self.assertEqual(phones, self.required_customer.get_phones())
        
    def test_add_email_of_required_customer(self):
        """Test to add the email attribute"""
        email = "mi_mail@hotmail.com"
        self.required_customer.set_email(email)
        self.assertEqual(email, self.required_customer.get_email())
        
    def test_updated_memebership_type_of_required_customer(self):
        """Test to update the membership attribute"""
        update_membership = "Gold"
        self.required_customer.set_membership(update_membership)
        self.assertEqual(update_membership, self.required_customer.get_membership())
        
    def test_update_status_of_required_customer(self):
        """Test to update the status attribute"""
        update_status = "INACTIVE"
        self.required_customer.set_status(update_status)
        self.assertEqual(update_status, self.required_customer.get_status())
    
    def test_create_customer(self):
        """Test if an instance of Customer class is created"""
        self.assertIsInstance(self.customer, Customer)
    
    def test_update_name_of_customer(self):
        """Test to update the first_name attribute"""
        update_name = "Giovanna"
        self.customer.set_first_name(update_name)
        self.assertEqual(update_name, self.customer.get_first_name())
        
    def test_update_last_name_of_customer(self):
        """Test to update the last_name attribute"""
        update_last_name = "Tames"
        self.customer.set_last_name(update_last_name)
        self.assertEqual(update_last_name, self.customer.get_last_name())
        
    def test_update_date_of_birth_of_customer(self):
        """Test to update the date_of_birth attribute"""
        update_date_of_birth = "22/08/2000"
        self.customer.set_date_of_birth(update_date_of_birth)
        self.assertEqual(update_date_of_birth, self.customer.get_date_of_birth())
        
    def test_update_addresses_of_customer(self):
        """Test to update the addresses attribute"""
        update_addresses = ["Calle Madrid # 333", "Calle Villa de Oropeza # 111"]
        self.customer.set_addresses(update_addresses)
        self.assertEqual(update_addresses, self.customer.get_addresses())
        
    def test_update__phone_numbers_of_customer(self):
        """Test to update the phones attribute"""
        update_phones = ["78957894", "60745628"]
        self.customer.set_phones(update_phones)
        self.assertEqual(update_phones, self.customer.get_phones())

    def test_update_email_account_of_customer(self):
        """Test to update the email attribute"""
        update_email = "jimena.sanabria@jalasoft.com"
        self.customer.set_email(update_email)
        self.assertEqual(update_email, self.customer.get_email())
        
    def test_update_membership_type_of_customer(self):
        """Test to update the membership attribute"""
        update_membership = "Platinum"
        self.customer.set_membership(update_membership)
        self.assertEqual(update_membership, self.customer.get_membership())
        
    def test_update_status_of_customer(self):
        """Test to update the status attribute"""
        update_status = "INACTIVE"
        self.customer.set_status(update_status)
        self.assertEqual(update_status, self.customer.get_status())
        
if __name__ == "__main__":
    unittest.main()

