import coverage
from coverage import coverage

cov = coverage()
cov.start()
import os
import sys
sys.path.append(os.path.abspath("../src"))


import unittest
from customer_tests.customer_test import CustomerTest
from customer_tests.manage_customer_test import ManageCustomerTest
from util_tests.input_validation_test import InputValidationTest
from util_tests.csv_operations_test import CsvOperations
from database_tests.database_test import DatabaseTest
from csv_tests.import_csv_test import ImportCsvTest
from customer_tests.import_customer_test import ImportCustomerTest
from log_tests.logger_handler_test import LoggerHandlerTest


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(CustomerTest))
suite.addTest(unittest.makeSuite(ManageCustomerTest))
suite.addTest(unittest.makeSuite(InputValidationTest))
suite.addTest(unittest.makeSuite(CsvOperations))
suite.addTest(unittest.makeSuite(DatabaseTest))
suite.addTest(unittest.makeSuite(ImportCsvTest))
suite.addTest(unittest.makeSuite(ImportCustomerTest))
suite.addTest(unittest.makeSuite(LoggerHandlerTest))

unittest.TextTestRunner(verbosity = 2).run(suite)

cov.stop()
cov.html_report(directory='report')