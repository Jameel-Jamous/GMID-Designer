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
        return f"\'{setterInstance.header}\'"

class SetValueStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.value = None
        self.prevVal = None
        self.prevHead = None
        if(type(params) == str):
            self.value = SI(str=params) 
        elif(type(params) == float or type(params) == int):
            self.value = SI(float=params)

    def execute(self):
        self.prevVal = setterInstance.value
        self.prevHead = setterInstance.header
        setterInstance.value = self.value
        return setterInstance.value
    
    def print(self):
        outstr = f" set to \'{setterInstance.value}\'"
        if(self.prevVal != setterInstance.value and self.prevHead == setterInstance.header):
            outstr += f" was \'{self.prevVal}\'"
        return outstr 