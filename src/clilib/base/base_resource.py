from abc import ABC

class BaseResource(ABC):    
    def __init__(self, parser):
        self._parser = parser


    @property
    def parser(self):
        return self._parser
    
    
    @parser.setter
    def parser(self, val):
        self._parser = val
    

    @parser.deleter
    def parser(self):
        del self._parser
