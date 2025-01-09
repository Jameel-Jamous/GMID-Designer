from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.settings import setterInstance
from gmid.utils.SI import SI

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
    
    def print(self):
        return ""

class SetValueStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.value = None
        if(type(params) == str):
            self.value = SI(str=params) 
        elif(type(params) == float or type(params) == int):
            self.value = SI(float=params)

    def execute(self):
        setterInstance.value = self.value
        return setterInstance.value
    
    def print(self):
        return ""