from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.settings import setterInstance

class SetHeadStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.header = params

    def execute(self):
        if((self.header == None) or (self.header == "")):
            setterInstance.header = "gmid"
        else:
            setterInstance.header = self.header
        return setterInstance.header
    
class SetValueStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.value = float(params)

    def execute(self):
        setterInstance.value = self.value
        return setterInstance.value