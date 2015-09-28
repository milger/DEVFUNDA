import sys
sys.path.append('../../src/modules/user')

import unittest
from user_app import UserApp

class UserTest(unittest.TestCase):
    
    def setUp(self):
        """ Setup Method to instance an object of Customer class """
        
        code = 3606855
        first_name = "Gretta"
        last_name = "Rocha"
        user_name = "grocha"
        password = "gretita"
        role = "Administrator"
        status = "ACTIVE"
        self.user = UserApp(code, first_name, last_name, user_name, password, role, status)
        self.user_test = UserApp("11111", "Carla", "Illanes", "cillanes", "Carlita", "Employee", "ACTIVE")
    
    def test_create_user(self):
        """ Test if an instance of user class is created with the required data """
        self.assertIsInstance(self.user_test, UserApp)
        
    def test_update_code_user(self):
        """ Test if the user code is updated """
        other_code = "55555"
        self.user_test.set_code(other_code)
        self.assertEqual(other_code, self.user_test.get_code())
        
    def test_update_first_name_user(self):
        """ Test if the first name of user is updated """
        other_first_name = "Brenda"
        self.user_test.set_first_name(other_first_name)
        self.assertEqual(other_first_name, self.user_test.get_first_name())
        
    def test_update_last_name_user(self):
        """ Test if the last name of user is updated """
        other_last_name = "Carpio"
        self.user_test.set_last_name(other_last_name)
        self.assertEqual(other_last_name, self.user_test.get_last_name())
        
    def test_update_user_name(self):
        """ Test if the user name is updated """
        other_user_name = "bcarpio"
        self.user_test.set_user_name(other_user_name)
        self.assertEqual(other_user_name, self.user_test.get_user_name())      

    def test_update_password_user(self):
        """ Test if the password of user is updated """
        other_password = "Brendita"
        self.user_test.set_password(other_password)
        self.assertEqual(other_password, self.user_test.get_password())      

    def test_update_role_user(self):
        """ Test if the role of user is updated """
        other_role = "Visitor"
        self.user_test.set_role(other_role)
        self.assertEqual(other_role, self.user_test.get_role())       
        
        
    def test_update_status_user(self):
        """ Test if the status of  user is updated """
        other_status = "INACTIVE"
        self.user_test.set_status(other_status)
        self.assertEqual(other_status, self.user_test.get_status()) 

if __name__ == "__main__":
    unittest.main()	
