__author__ = 'JimenaSanabria'

import datetime

"""Method to validate input data from console."""

def get_date_input(item_name):
    """Verify that the input from console is a date.
    
    Keyword arguments:
    item_name -- the str with the name of item to be register as date

    Return the date regiter by console
    
    """ 

    while True:
        try:
            item = raw_input(item_name + " (dd-mm-yyyy):")
            item = datetime.datetime.strptime(item, "%d-%m-%Y")
            break
        except:
            print "Error, a " + item_name +" needs to have the format dd-mm-yyyy."
    return item

def get_integer_input(item_name):
    """Verify that the input from console is an integer.
    
    Keyword arguments:
    item_name -- the str with the name of item to be register as integer
    
    Return the integer number register by console
    
    """

    while True:
        try:
            item = int(input(item_name + ":"))
            break
        except:
            print "Error, a " + item_name +" needs to be an integer number."
    return item
    
def get_option_input(item_name, options_list):
    """Verify that the input from console is an option of list.

    Keyword arguments:
    item_name -- the str with the name of item to be register as option of list
    options_list -- the list of str with the the option of item_name
    
    Return the option of options_list register by console
    
    """

    while True:
        item = raw_input(item_name + ":")
        if item in options_list:
            break
        else:
            print "Error, a " + item_name +" needs to be an option of list."
    return item

def get_required_input(item_name):
    """
    This method reads a required input from console.
    Returns a String with the value inserted.
    
    Params:
    @item_name    String with the name of item
    """
    while True:
        value = raw_input(item_name + ": ")
        if not value:
            print "Invalid value, " + item_name + " is required. Please try again.\n"
        else:
            break
    return value

def get_optional_input(item_name):
    """
    This method reads an optional input from console.
    Returns a String with the value inserted. If empty value is inserted, it returns None.
    
    Params:
    @item_name    String with the name of item
    """
    value = raw_input(item_name + "(press Enter to skip): ")
    if not value:
        value = None
    return value

def get_optional_integer_input(item_name):
    """
    This method reads an optional numerical input from console.
    Returns an Integer with the value inserted. If empty value is inserted, it returns None.
    
    Params:
    @item_name    String with the name of item
    """
    numerical_value = None
    while True:
        value = raw_input(item_name + "(press Enter to skip): ")
        if not value:
            break
        try:
            numerical_value = int(value)
            break
        except ValueError:
            print "Error, " + item_name + " must be an integer number."
    return numerical_value

def get_optional_float_input(item_name):
    """
    Reads an optional value from console as float.
    Returns a float number inserted by console. If empty value is inserted, it returns None.
    
    Params:
    @item_name    String with the name of item
    """
    float_value = None
    while True:
        value = raw_input(item_name + "(press Enter to skip): ")
        if not value:
            break
        try:
            float_value = float(value)
            break
        except ValueError:
            print "Error, " + item_name + " must be a number."
    return float_value

def ask_confirmation_question(question):
    """
    This method asks a yes/no question from console.
    It returns True for "yes" or False for "no".

    Params:
    @question    It is a String that is printed to the user.
    """
    valid_answers = {"yes": True, "y": True, "no": False, "n": False}
    while True:
        answer = raw_input(question + "[y/n]").lower()
        if answer in valid_answers:
            return valid_answers[answer]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
