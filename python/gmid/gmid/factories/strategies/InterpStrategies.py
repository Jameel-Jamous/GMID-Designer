from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.interpolator import Interpolator
from gmid.settings import setterInstance

class InterpHeaderStrat(OptionStrategy):
    """Interpolates a header (argument) at the set value"""
    def __init__(self, params):
        super().__init__()
        self.y_header = params
        self.yAtX = None

    def execute(self):
        self.yAtX = Interpolator(self.y_header, setterInstance.header).execute()
        return self.yAtX

    def print(self):
        return f"For {setterInstance.header} = {setterInstance.value}:\n\n{self.y_header} = {self.yAtX}"

        
class InterpHeadStrat(OptionStrategy):
    """Interpolates a tuple of headers at the set value"""
    def __init__(self, params):
        super().__init__()
        self.headers = params 

    def execute(self):
        ret = []
        for item in self.headers:
            ret.append(Interpolator(item, setterInstance.header).execute())
        return ret
            
    def print(self):
        return ""

# TODO: Implement Me
class InterpAnnotateStrat(OptionStrategy):
    """Interpolates a header or a tuple of headers with plot annotations"""
    def __init__(self, params):
        super().__init__()
    
    def execute(self):
        return
    
    def print(self):
        return ""