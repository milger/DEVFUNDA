"""Unit tests"""
import sys
import os
sys.path.append(os.path.abspath("../../src"))

import unittest
from logs.logger_handler import LoggerHandler

class LoggerHandlerTest(unittest.TestCase):
    """Unit tests for LoggerHandler"""

    def setUp(self):
        """Setup method to instance an object of Logger Handler"""

        self.debug_message = "Unit test for debug log"
        self.info_message = "Unit test for info log"
        self.error_message = "Unit test for error log"
        self.warning_message = "Unit test for warning log"
        
        dir_name = os.path.dirname(os.path.abspath(__file__))
        self.log_file_path = dir_name + "/test.log"
        
        self.logger = LoggerHandler(self.log_file_path)
        self.logger.debug(self.debug_message)
        self.logger.info(self.info_message)
        self.logger.error(self.error_message)
        self.logger.warning(self.warning_message)

        file = open(self.log_file_path, "r")
        self.all_lines_path = file.readlines()
        file.close()


    def get_if_message_is_in_file(self, message):
        """Test if an instance of Customer class is created with required
        
        Keyword arguments:
        message -- the str with the message to search in log file"""
        
        is_message = False
        for line in self.all_lines_path:
            if line.find(message):
                is_message = True
        
        return is_message
        
    def test_create_logger_handler_object(self):
        """Test if an instance of Customer class is created with required"""

        self.assertIsInstance(self.logger, LoggerHandler)

    def test_logger_handler_use_singleton_class(self):
        """Test singleton class used in logger handler"""

        other_logger = LoggerHandler(self.log_file_path)
        self.assertEqual(self.logger, other_logger)

    def test_debug_log_message(self):
        """Test debug log message"""
       
        self.assertTrue(self.get_if_message_is_in_file(self.debug_message))
        
    def test_info_log_message(self):
        """Test info log message"""

        self.assertTrue(self.get_if_message_is_in_file(self.info_message))
        
    def test_warning_log_message(self):
        """Test warning log message"""
       
        self.assertTrue(self.get_if_message_is_in_file(self.error_message))
        
    def test_error_log_message(self):
        """Test error log message"""

        self.assertTrue(self.get_if_message_is_in_file(self.warning_message))


if __name__ == "__main__":
    unittest.main()
