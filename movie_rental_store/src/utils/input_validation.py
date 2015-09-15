__author__ = 'JimenaSanabria'

import datetime

"""Method to validate input data from console."""

def get_date_input(item_name):
    """Verify that the input from console is a date."""

    while True:
        try:
            item = raw_input(item_name + " (dd-mm-yyyy):")
            item = datetime.datetime.strptime(item, "%d-%m-%Y")
            break
        except:
            print "Error, a " + item_name +" needs to have the format dd-mm-yyyy."
    return item

def get_integer_input(item_name):
    """Verify that the input from console is an integer."""

    while True:
        try:
            item = int(input(item_name + ":"))
            break
        except:
            print "Error, a " + item_name +" needs to be an integer number."
    return item
    
def get_option_input(item_name, options_list):
    """Verify that the input from console is an option of list."""

    while True:
        item = raw_input(item_name + ":")
        if item in options_list:
            break
        else:
            print "Error, a " + item_name +" needs to be an option of list."
    return item
