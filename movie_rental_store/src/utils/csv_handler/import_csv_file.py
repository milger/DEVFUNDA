"""Methods to import the data from csv file."""

__author__ = 'JimenaSanabria'

import csv

def parse_csv_file(file_name):
    """Parse the csv file.

    Keyword arguments:
    file_name -- the str with the name of csv file to be parsed

    Return an array with dictionary of string after parsing a csv file

    """
    complete_data_list = []
    file = file_name + ".csv"
    import_file = open(file, "rb")
    reader_file = csv.reader(import_file)
    row_index = 0
    for row in reader_file:
        row_data = {}
        if row_index == 0:
            header = row
        else:
            column_index = 0
            for column in row:
                row_data[header[column_index]] = column
                column_index += 1
            complete_data_list.append(row_data)
        row_index += 1

    import_file.close()
    return complete_data_list
