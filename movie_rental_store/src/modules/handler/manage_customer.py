__author__ = 'JimenaSanabria'

import sys
sys.path.append('../../src')

from modules.entity.customer import Customer
from modules.entity.membership_type import MembershipType
from modules.entity.status import Status
from utils.input_validation import *

class ManageCustomer(object):
    """Class to manage registratin of customer class"""
    
    def __init__(self, code):
        """Constructor for customer class.

        Keyword arguments:
        code -- the str with code for customer

        """
        
        self._customer = Customer(code)
        
    def get_customer(self):
        """Get customer attribute.

        Return in a customer object

        """
        return self._customer
        
    def read_first_name(self):
        """Read first name from console to set it in customer class."""

        first_name = raw_input("First Name:")
        self.get_customer().set_first_name(first_name)
    
    def read_last_name(self):
        """Read last name from console to set it in customer class."""

        last_name = raw_input("Last Name:")
        self.get_customer().set_last_name(last_name)

    def read_date_of_birth(self):
        """Read date of birth from console to set it in customer class."""

        date_of_birth = get_date_input("Date of birth")
        self.get_customer().set_date_of_birth(date_of_birth)

    def read_quantity_of_items(self):
        """Read quantity of items for a list.

        Return quantity of items for a list
        """

        quantity = get_integer_input("Quantity of items")
        return quantity
        
    def read_addresses(self):
        """Read addresses from console to set it in customer class."""

        addresses = []
        print "Enter the quantity of addresses to be registered."
        quantity_addresses = self.read_quantity_of_items()
        
        for index in range(quantity_addresses):
            address = raw_input("address:")
            addresses.append(address)
        self.get_customer().set_addresses(addresses)


    def read_phones(self):
        """Read phones from console to set it in customer class."""

        phones = []
        print "Enter the quantity of phones to be registered."
        quantity_phones = self.read_quantity_of_items()
        
        for index in range(quantity_phones):
            phone = get_integer_input("Phone number")            
            phones.append(phone)
        self.get_customer().set_phones(phones)


    def read_membership(self):
        """Read membership from console to set it in customer class."""

        options_membership = [MembershipType.GOLD, MembershipType.PLATINUM, MembershipType.BRONZE]

        print "Type the membeship type from following opetions:"
        for option in options_membership:
            print option
        
        membership = get_option_input("Membership", options_membership)
        self.get_customer().set_membership(membership)

    def read_status(self):
        """Read status from console to set it in customer class."""


        options_status = [Status.ACTIVE, Status.INACTIVE]

        print "Type the status from following opetions:"
        for option in options_status:
            print option
        
        status = get_option_input("Status", options_status)
        self.get_customer().set_status(status)
