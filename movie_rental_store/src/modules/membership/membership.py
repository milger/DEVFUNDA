__author__= 'GrettaRocha'

class Membership(object):
    """ Class to get an instance of membership with attributes:"""
    
    def __init__(self, code, name, discount):
        
        """ Constructor method for membership class
        Arguments:
        code -- numeric value to identify a membership
        name -- string value for the name of membership
        discount -- numeric value for the discount(percent)
        """
        self._code = code
        self._name = name
        self._discount = discount

    def set_code(self, code):
        """ Method to set code for membership
        Arguments:
        code -- numeric value with code of membership
        """
        self._code = code
    
    def set_name(self, name):
        """ Method to set name for membership
        
        Arguments:
        name -- string value with name of membership

        """
        self._name = name
        
    def set_discount(self, discount):
        """ Method to set discount for membership
        
        Arguments:
        discount -- numeric value with the discount(percent)

        """
        self._discount = discount
        
    def get_code(self):
        """Method to get the membership code.

        Return numeric value with the membership code

        """
        return self._code
        
    def get_name(self):
        """Method to get the membership name.

        Return a string with the membership name

        """
        return self._name

    def get_discount(self):
        """Method to get the membership discount.

        Return an integer with the membership discount

        """
        return self._discount

                
        
 
        
                
