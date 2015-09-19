import sys
sys.path.append('../../src/modules/membership')

import unittest
from membership import Membership
from manage_membership import ManageMembership

class ManageMembershipTest(unittest.TestCase):
        
    def setUp(self):
        """ setup method to instance an object of ManageMembership class """
        code = 5
        name = "Gold"
        discount = 10
        self.membership = Membership(code, name, discount)
        self.file_name = "membership.csv" 
    
    def test_membership_code_is_correctly_saved_in_csv(self):
        """ Method to test if the memnershipd code is correctly saved in the csv file"""
        manage_membership = ManageMembership()
        manage_membership.save_membership_data_to_csv(self.file_name, self.membership)
        retrievedData = manage_membership.read_membership_data_from_csv(self.file_name)
        self.assertEqual(5, int(retrievedData[0]))
        
    def test_membership_name_is_correctly_saved_in_csv(self):
        """ Method to test if the memnershipd name is correctly saved in the csv file"""
        manage_membership = ManageMembership()
        manage_membership.save_membership_data_to_csv(self.file_name, self.membership)
        retrievedData = manage_membership.read_membership_data_from_csv(self.file_name)
        self.assertEqual("Gold", retrievedData[1])
        
    def test_discount_is_correctly_saved_in_csv(self):
        """ Method to test if the memnershipd discount is correctly saved in the csv file"""
        manage_membership = ManageMembership()
        manage_membership.save_membership_data_to_csv(self.file_name, self.membership)
        retrievedData = manage_membership.read_membership_data_from_csv(self.file_name)
        self.assertEqual(10, int(retrievedData[2]))
        
if __name__=="__main__":
    unittest.main()