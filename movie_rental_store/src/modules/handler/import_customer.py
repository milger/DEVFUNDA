"""Class to import a csv to create customers"""
__author__ = 'JimenaSanabria'

import sys
sys.path.append('../../src')
from random import randint
from modules.entity.customer import Customer
from utils.csv_handler.import_csv_file import *


class ImportCustomer(object):
    """Class to import csv file to handle the customers"""

    def get_data_from_csv(self, abs_file_path):
        """Get all data from csv file.

        Keyword arguments:
        abs_file_path -- the str with file path from csv file

        Return in a list with string dictionary with data to create customer objects

        """
        return parse_csv_file(abs_file_path)


    def create_customer_object(self, code, data):
        """Get customer object with data from csv file.

        Keyword arguments:
        code -- the str with code to create customer object
        data -- the string dictionary with data to create customer object

        Return in a customer object

        """

        customer = Customer(code)
        customer.set_first_name(data.get("First Name"))
        customer.set_last_name(data.get("Last Name"))
        customer.set_date_of_birth(data.get("Date of birth"))
        customer.set_email(data.get("Email"))  
        customer.set_membership(data.get("Membership"))
        customer.set_status(data.get("Status"))
        customer.set_addresses(get_string_list_data(data, "Addresses"))
        customer.set_phones(get_integer_list_data(data, "Phone numbers"))

        return customer


    def import_customer_csv_file(self, abs_file_path):
        """Get all customer object after reading a csv file.

        Keyword arguments:
        abs_file_path -- the str with file path from csv file

        Return in a list with customer object

        """

        complete_data = self.get_data_from_csv(abs_file_path)
        customers = []
        for data in complete_data:
            code = 'cust%d' % (randint(0, 100000),)
            customers.append(self.create_customer_object(code, data))
        return customers
