"""General singleton class."""

__author__ = 'JimenaSanabria'
import sys
import os
class Singleton(type):
    """Class to handle singleton patron."""
 
    def __init__(cls, name, bases, dct):
        """Constructor of class."""
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls):
        """Call class.
        
        Return its own instance
        
        """
        if cls.__instance is None:
            cls.__instance = type.__call__(cls)
        return cls.__instance