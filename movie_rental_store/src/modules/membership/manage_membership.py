import sys
sys.path.append('../../src/utils')

from csv_operations import Csv
from membership import Membership

class ManageMembership:
    """ Class to get an instance to manage operations on membership like: create, update, delete"""
    
    def read_membership_data_from_console(self):
        """ Method to read membership data from console"""
        code = raw_input("Enter Code: ")
        name = raw_input("Enter Name:")
        discount = raw_input("Enter Discount(%):")
        membership = Membership(code, name, discount)
        return membership
    
    def read_membership_data_from_csv(self, file_name):
        """ Method to read membership data to CSV file
        
        Arguments:
        file_name -- file that will be readed to obtain the memberships
        
        Returned value:
        membership -- the first row of the returned list from CSV.read method
        
        """
        membership = Csv.read_data(file_name)
        return membership[0]
    
    def save_membership_data_to_csv(self,file_name, membership):
        """ Method to save membership data to CSV file
        
        Arguments:
        
        file_name -- file where will be saved the membership
        membership -- membership objtect that will be saved in the CSV file
        
        """
        row = [str(membership.get_code()), membership.get_name(), str(membership.get_discount())]
        list_membership = []
        list_membership.append(row)
        Csv.write_data(file_name, list_membership)
        
    def register_membership(self):
        """ Method to register/create a new menbership"""
        membership = self.read_membership_data_from_console()
        self.save_membership_data_to_csv("membership.csv", membership)
                
    
    def update_membership(self):
        """ Method to update an existent membership"""
        pass
    
    def delete_embership(self):
        """ Method to delete an existent membership"""
        pass