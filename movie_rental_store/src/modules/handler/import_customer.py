"""Class to import a csv to create customers"""
__author__ = 'JimenaSanabria'

import sys
sys.path.append('../../src')
from random import randint
from modules.entity.customer import Customer
from utils.csv_handler.import_csv_file import parse_csv_file

class ImportCustomer(object):
    """Class to import csv file to handle the customers"""

    def get_data_from_csv(self, file_path):
        """Get all data from csv file.

        Keyword arguments:
        file_path -- the str with file path from csv file

        Return in a list with string dictionary with data to create customer objects

        """
        return parse_csv_file(file_path)


    def create_customer_object(self, code, data):
        """Get customer object with data from csv file.

        Keyword arguments:
        code -- the str with code to create customer object
        data -- the string dictionary with data to create customer object

        Return in a customer object

        """

        customer = Customer(code)
        for index in range(len(data.items())):
            customer.set_first_name(data["First Name"])
            customer.set_last_name(data["Last Name"])
            customer.set_date_of_birth(data["Date of birth"])
            customer.set_addresses(data["Addresses"])
            customer.set_phones(data["Phone numbers"])
            customer.set_membership(data["Membership"])
            customer.set_status(data["Status"])
        return customer


    def import_customer_csv_file(self, file_path):
        """Get all customer object after reading a csv file.

        Keyword arguments:
        file_path -- the str with file path from csv file

        Return in a list with customer object

        """

        complete_data = self.get_data_from_csv(file_path)
        customers = []
        for data in complete_data:
            code = 'cust%d' % (randint(0, 100000),)
            customers.append(self.create_customer_object(code, data))
        return customers
