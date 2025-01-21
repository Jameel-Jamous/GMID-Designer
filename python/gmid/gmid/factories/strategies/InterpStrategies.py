from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.interpolator import Interpolator
from gmid.settings import setterInstance


# TODO: Change 'setterInstance.header' to 'self.x_header'
class InterpHeaderStrat(OptionStrategy):
    """Interpolates a single header (argument) at the set value"""

    def __init__(self, params):
        super().__init__()
        self.y_header = params  # String containing the header to be interpolated
        self.outDict = {}

    def execute(self):
        if (
            setterInstance.header in setterInstance.df.columns
            and self.y_header in setterInstance.df.columns
        ):
            self.outDict[self.y_header] = Interpolator(
                self.y_header, setterInstance.header
            ).execute()
        elif self.y_header == "all":
            # Make a list that contains all of the headers execpt for the 'set' one
            temp = [
                item
                for item in setterInstance.df.columns
                if item != setterInstance.header
            ]
            self.outDict = InterpHeadStrat(temp).execute()
        else:
            self.outDict["Invalid"] = self.y_header
        return self.outDict

    def print(self):
        return


class InterpHeadStrat(OptionStrategy):
    """Interpolates a tuple of headers at the set value"""

    def __init__(self, params):
        super().__init__()
        self.headers = params
        self.outDict = {}

    def execute(self):
        for item in self.headers:
            self.outDict.update(InterpHeaderStrat(item).execute())
        return self.outDict

    def print(self):
        return


# TODO: Implement Me
class InterpAnnotateStrat(OptionStrategy):
    """Interpolates a header or a tuple of headers with plot annotations"""

    def __init__(self, params):
        super().__init__()

    def execute(self):
        return

    def print(self):
        return ""
