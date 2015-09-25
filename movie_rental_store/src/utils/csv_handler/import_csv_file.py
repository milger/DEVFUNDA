"""Methods to import the data from csv file."""

__author__ = 'JimenaSanabria'

import os
import csv


def get_file_name(file_path):
    """Get the file name of a path.

    Keyword arguments:
    file_path -- the str with the path of file

    Return a string with the name of file

    """

    head, tail = os.path.split(file_path)
    return tail


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
    file_name = get_file_name(file_path)

    try:
        import_file = open(file_name, "rb")

    except IOError:
        print 'An error occured trying to read the file.'

    else:
        reader_file = csv.DictReader(import_file)
        complete_data_list = get_file_data(reader_file)
        import_file.close()

    return complete_data_list
