"""Class to Handler the logger."""
import sys
import os
import logging
import logging.handlers

sys.path.append(os.path.abspath("../"))

from utils.singleton import Singleton

class LoggerHandler():

    """Class to Handler the logger (Singleton pattern)."""
    __metaclass__ = Singleton

    def __init__(self, abs_path_logfile):
        """Constructor to set the configuration of logger with DEBUG level by default"""

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.handlers.TimedRotatingFileHandler(abs_path_logfile, when='D', interval=1)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def debug(self, msg):
        """Method to log debug messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        self.logger.debug(msg)

    def info(self, msg):
        """Method to log info messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        self.logger.info(msg)

    def warning(self, msg):
        """Method to log warning messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        self.logger.warning(msg)

    def error(self, msg):
        """Method to log error messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        self.logger.error(msg)
