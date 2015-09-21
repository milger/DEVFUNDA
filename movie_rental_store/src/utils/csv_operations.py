__author__ = 'GrettaRocha'

import csv
import sys

class CsvOperations(object):
    """ class that contains functions to write/read  data in CSV file """

    @staticmethod 
    def write_data(file_name, data):
        """Static method to write some data in the csv file, 
        
        Argument:
        filename -- name of CSV file where the data will be saved
        data -- data array that will be saved in the csv file
       
        """
        try:
            writer = csv.writer(open(file_name, "wb"))
            for row in data:
                writer.writerow(row)
        except IOError as error:
            print "I/O error({0}): {1}".format(error.errno, error.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    
    
    @staticmethod 
    def read_data(file_name):
        """ Static method to read data from csv file
        
        Argument:
        file_name -- name of CSV file from the data will be read
        """
        try:
            with open(file_name, 'rb') as index_file:
                list_data = [row for row in csv.reader(index_file.read().splitlines())]
            return list_data
        
        except IOError as error:
            print "I/O error({0}): {1}".format(error.errno, error.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    