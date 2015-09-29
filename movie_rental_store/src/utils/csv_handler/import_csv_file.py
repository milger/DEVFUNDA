"""Methods to import the data from csv file."""

__author__ = 'JimenaSanabria'

import os
import csv

def get_file_data(reader_file):
    """Get a list of string dictionary for the data of a file

    Keyword arguments:
    reader_file -- the reader object of csv

    Return a list with dictionary of string with the data of header:row value

    """

    complete_data_list = []
    for row in reader_file:
        complete_data_list.append(row)

    return complete_data_list


def parse_csv_file(file_path):
    """Parse the csv file.

    Keyword arguments:
    file_path -- the str with the path of file

    Return an array with dictionary of string after parsing a csv file

    """

    complete_data_list = []

    try:
        import_file = open(file_path, "rb")

    except IOError:
        print 'An error occured trying to read the file.'

    else:
        reader_file = csv.DictReader(import_file)
        complete_data_list = get_file_data(reader_file)
        import_file.close()

    return complete_data_list


def get_string_list_data(data, header):
    """Get an array with string data.

    Keyword arguments:
    data -- the dictionary with string data to create object
    header -- the string with name of header (key)

    Return in an array with string data

    """
    list_data = []
    if data.get(header) is not None:
        list_data = (data.get(header)).split('-')
    return list_data


def get_integer_list_data(data, header):
    """Get an array with integer data.

    Keyword arguments:
    data -- the dictionary with string data to create object
    header -- the string with name of header (key)

    Return in an array with integer data

    """
    list_data = []
    if data.get(header) is not None:
        list_data = [int(number) for number in  (data.get(header)).split('-')]
    return list_data