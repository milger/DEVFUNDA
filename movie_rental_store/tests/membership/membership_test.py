import sys
sys.path.append('../../src/modules/membership')

import unittest
from membership import Membership

class MembershipTest(unittest.TestCase):

    def setUp(self):
        """Setup method to instance an object of Membership class """
        code = 9
        name = "Gold"
        discount = 10
        self.membership = Membership (code, name, discount)
        self.test_membership = Membership(5, "Platinum", 5)
        
    def test_create_membership(self):
        """Test if an instance is created with the required data"""
        self.assertIsInstance(self.test_membership, Membership)
        
    def test_set_code_of_membership(self):
        """Test to update the membership code"""
        other_code = 10
        self.test_membership.set_code(other_code)
        self.assertEqual(other_code, self.test_membership.get_code())
        
    def test_set_name_of_membership(self):
        """ Test to update the membership name"""
        other_name = "Platinum"
        self.test_membership.set_name(other_name)
        self.assertEqual(other_name, self.test_membership.get_name())
        
    def test_set_discont_of_membership(self):
        """ Test to update the membership discount"""
        other_discount = 11
        self.test_membership.set_discount(other_discount)
        self.assertEqual(other_discount, self.test_membership.get_discount())
        

if __name__=="__main__":
    unittest.main()