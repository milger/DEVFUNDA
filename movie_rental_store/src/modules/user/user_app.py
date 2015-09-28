__author__ = 'CarlaIllanes'

class UserApp(object):
    """ Class to get an instance of user with attributes"""
    
    def __init__(self, code, first_name, last_name, user_name, password, role, status):
        """ Constructor for User class
        
        Arguments:
        code -- numeric value to identify a user
        first_name -- string value with the first name of user
        last_name -- string value with the last name of user
        user_name --  string value with the user name
        password -- string value with the password of user
        role -- string value with the role type of user
        status -- ACTIVE/INACTIVE values
        
        """
        self._code = code
        self._first_name = first_name
        self._last_name = last_name
        self._user_name = user_name
        self._password = password
        self._role = role
        self._status = status
        
    def set_code(self, code):
        """ Set cod for user 
        
        Argument:
        code -- numeric value to identify a user
        
        """
        self._code = code
    
    def set_first_name(self, first_name):
        """ Set first_name for user 
        
        Argument:
        firs_name -- string value with the first name of user
        
        """
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        """ Set last_name for user 
        
        Argument:
        last_name -- string value with the last name of user
        
        """
        self._last_name = last_name
        
    def set_user_name(self, user_name):
        """ Set user_name for user 
        
        Argument:
        user_name -- string value with the user name 
        
        """
        self._user_name = user_name 
        
    def set_password(self, password):
        """ Set password for user 
        
        Argument:
        password -- string value with the password of user 
        
        """
        self._password = password   
        
    def set_role(self, role):
        """ Set role for user 
        
        Argument:
        role -- string value with the password of user 
        
        """
        self._role = role   
        
    def set_status(self, status):
        """ Set status for user 
        
        Argument:
        status -- string value with the status of user 
        
        """
        self._status = status
        
    def get_code(self):
        """ get the code user
        
        Return an integer value
        
        """
        return self._code
        
    def get_first_name(self):
        """ get the first name of the user
        
        Return a  string value
        
        """
        return self._first_name
    
    def get_last_name(self):
        """ get the last name of the user
        
        Return a  string value
        
        """
        return self._last_name
    
    def get_user_name(self):
        """ get the user name
        
        Return a string value
        
        """
        return self._user_name
    
    def get_password(self):
        """ get the password of the user
        
        Return a  string value
        
        """
        return self._password
    
    def get_status(self):
        """ get the status of the user
        
        Return a  string (ACTIVE or INACTIVE) value
        
        """
        return self._status
    
    def get_role(self):
        """ Get role of the user 
        
        Return an string value
        
        """
        return self._role 