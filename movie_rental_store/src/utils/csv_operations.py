__author__ = 'GrettaRocha'

import csv

class Csv():
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
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    
    
    @staticmethod 
    def read_data(file_name):
        """ Static method to read data from csv file
        
        Argument:
        filename -- name of CSV file from the data will be read
        """
        try:
            with open(file_name, 'rb') as f:
                list_data = [row for row in csv.reader(f.read().splitlines())]
            return list_data
        
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise