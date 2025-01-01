from abc import ABC, abstractmethod
from gmid.factories.strategies.OptionStrategy import OptionStrategy

class OptionContext(ABC):
    def __init__(self, args, kwargs):
        super().__init__()
        self.strategies = []
        self.options = dict(kwargs)

    def append(self, strategy : OptionStrategy):
        self.strategies.append(strategy) 
    
    def length(self):
        return len(self.strategies)

    def isEmpty(self):
        return self.length() == 0
   
    @abstractmethod 
    def execute(self):
        pass

    @abstractmethod
    def toStrategy(self):
        pass