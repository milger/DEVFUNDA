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

        self.logger = LoggerHandler()

    def test_create_logger_handler_object(self):
        """Test if an instance of Customer class is created with required"""

        self.assertIsInstance(self.logger, LoggerHandler)

    def test_logger_handler_use_singleton_class(self):
        """Test singleton class used in logger handler"""

        other_logger = LoggerHandler()
        self.assertEqual(self.logger, other_logger)


if __name__ == "__main__":
    unittest.main()
