__author__ = 'JimenaSanabria'

from membership_type import MembershipType
from status import Status


class Customer(object):
    """Class to get an instance of customer with following attributes:"""
    
    def __init__(self, code, first_name, last_name, date_of_birth, addresses = [], phones = [], email = "", membership = MembershipType.BRONZE, status = Status.ACTIVE):
        """Constructor for customer class.

        Keyword arguments:
        code -- the str with code for customer
        first_name -- the str with first name of customer
        last_name -- the str with last name of customer
        date_of_birth -- the date with date of birth of customer
        addresses -- the list of strings with addresses of customer (default [])
        phones -- the list of integers with phones of customer (default [])
        email -- the str with email account of customer (default "")
        membership -- the str with membership type of customer (default "Bronze")
        status -- the str with status of customer (default "ACTIVE")

        """
        self._code = code
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._addresses = addresses
        self._phones = phones
        self._email = email
        self._membership = membership
        self._status = status 

    def set_first_name(self, first_name):
        """Set first name for customer.

        Keyword arguments:
        first_name -- the str with first name

        """
        self._first_name = first_name

    def set_last_name(self, last_name):
        """Set last name for customer.

        Keyword arguments:
        last_name -- the str with last name

        """
        self._last_name = last_name
        
    def set_date_of_birth(self, date_of_birth):
        """Set the date of birth for customer.

        Keyword arguments:
        date_of_birth -- the str with date of birth

        """
        self._date_of_birth = date_of_birth

    def set_addresses(self, addresses = []):
        """Set the addresses customer.

        Keyword arguments:
        addresses -- the list of strings with addresses of customer (default [])

        """
        self._addresses = addresses
               
    def set_phones(self, phones = []):
        """Set phone numbers for customer.

        Keyword arguments:
        phones -- the list of integers with phones of customer (default [])

        """
        self._phones = phones
       
    def set_email(self, email = ""):
        """Set email account for customer.

        Keyword arguments:
        email -- the str with email account (default "")

        """
        self._email = email

    def set_membership(self, membership = MembershipType.BRONZE):
        """Set membership type for customer.

        Keyword arguments:
        membership -- the str with membership type (default "Bronze")

        """
        self._membership = membership
        
    def set_status(self, status = Status.ACTIVE):
        """Set status type for customer.

        Keyword arguments:
        status -- the str with status type (default "ACTIVE")

        """
        self._status = status

        
    def get_first_name(self):
        """Get first name of customer.

        Return in a string the first name of customer

        """
        return self._first_name
        
    def get_last_name(self):
        """Get last name of customer.

        Return in a string the last_name attribute of customer

        """
        return self._last_name
        
    def get_date_of_birth(self):
        """Get the date of birth of customer.

        Return in a date the date_of_birth attribute of customer

        """
        return self._date_of_birth
        
    def get_addresses(self):
        """Get list of strings with addresses of customer.

        Return in a list the addresses attribute of customer

        """
        return self._addresses
       
    def get_phones(self):
        """Get phone numbers of customer.

        Return in a list of integers with phones attribute of customer

        """
        return self._phones
               
    def get_email(self):
        """Get email account of customer.

        Return in a string the email attribute of customer

        """
        return self._email
        
    def get_membership(self):
        """Get the membership type of customer.

        Return in a string the membership attribute of customer

        """
        return self._membership
        
    def get_status(self):
        """Get status (ACTIVE or INACTIVE) of customer.

        Return in a string the status attribute of customer

        """
        return self._status

