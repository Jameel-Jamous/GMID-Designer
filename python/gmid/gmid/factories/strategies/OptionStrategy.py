from abc import ABC, abstractmethod

class OptionStrategy(ABC):
    """Template for creating strategies for options."""
    
    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def print():
        pass