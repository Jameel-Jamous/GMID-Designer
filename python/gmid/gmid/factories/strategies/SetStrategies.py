from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.settings import setterInstance
from gmid.utils.SI import SI


class SetHeadStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.header = params

    def execute(self):
        setterInstance.prevHead = setterInstance.header
        if (self.header is None) or (self.header == ""):
            setterInstance.header = "gmid"
        elif self.header in setterInstance.df.columns:
            setterInstance.header = self.header
        else:
            setterInstance.prevHead = self.header
        return setterInstance.header

    def print(self):
        if self.header not in setterInstance.df.columns and self.header is not None:
            output = f"'{self.header}' is not a settable header. Please use 'gmid view' to see selectable headers."
        else:
            output = f"'{setterInstance.header}'"
        return output


class SetValueStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.value = SI(asFloat=10)
        self.prevVal = None
        self.prevHead = None

        if type(params) is str:
            self.value = SI(asStr=params)
        elif type(params) is float or type(params) is int:
            self.value = SI(asFloat=params)

    def execute(self):
        self.prevVal = setterInstance.value
        setterInstance.value = self.value
        return setterInstance.value

    def print(self):
        if setterInstance.prevHead in setterInstance.df.columns:
            outstr = f" set to '{setterInstance.value}'"
            if (
                self.prevVal != setterInstance.value
                and setterInstance.prevHead == setterInstance.header
            ):
                outstr += f" was '{self.prevVal}'"
        else:
            outstr = ""
        return outstr
