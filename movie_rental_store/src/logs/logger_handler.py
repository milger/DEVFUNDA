"""Class to Handler the logger."""
import sys
import os
import logging
import logging.handlers

sys.path.append(os.path.abspath("../"))
ABS_LOG_PATH = os.path.abspath("../../logs")
from utils.singleton import Singleton

class LoggerHandler():
    """Class to Handler the logger (Singleton pattern)."""
    __metaclass__ = Singleton

    def __init__(self):
        """Constructor to set the configuration of logger with DEBUG level by default"""

        abs_path_logfile = ABS_LOG_PATH + "/movie_rental_store.log"

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.handlers.TimedRotatingFileHandler(abs_path_logfile, when='D', interval=30)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)


    @staticmethod
    def debug(msg):
        """Method to log debug messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        logging.debug(msg)

    @staticmethod
    def info(msg):
        """Method to log info messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        logging.info(msg)

    @staticmethod
    def warning(msg):
        """Method to log warning messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        logging.warning(msg)

    @staticmethod
    def error(msg):
        """Method to log error messages

        Keyword arguments:
        msg -- the str with the message to be written in log file"""

        logging.error(msg)
