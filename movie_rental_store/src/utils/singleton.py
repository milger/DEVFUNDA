"""General singleton class."""

__author__ = 'JimenaSanabria'

class Singleton(type):
    """Class to handle singleton patron."""
 
    def __init__(cls, name, bases, dct):
        """Constructor of class."""
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, name):
        """Call class.
        
        Return its own instance
        
        """
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, name)
        return cls.__instance