from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.interpolator import Interpolator
from gmid.settings import setterInstance


class InterpHeaderStrat(OptionStrategy):
    """Interpolates a header (argument) at the set value"""

    def __init__(self, params):
        super().__init__()
        self.y_header = params
        self.printHeaders = []
        self.yAtX = None

    def execute(self):
        if self.y_header == "all":
            self.yAtX = []
            self.printHeaders = [
                item
                for item in setterInstance.df.columns
                if item != setterInstance.header
            ]
            for item in self.printHeaders:
                self.yAtX.append(Interpolator(item, setterInstance.header).execute())
        elif self.y_header in setterInstance.df.columns:
            self.printHeaders.append(self.y_header)
            self.yAtX = Interpolator(self.y_header, setterInstance.header).execute()
        return self.yAtX

    def print(self):
        output = f"For {setterInstance.header} = {setterInstance.value}:\n\n\t"
        if self.y_header == "all":
            for keys, value in zip(self.printHeaders, self.yAtX):
                output += f"{keys} = {value}, "
            # Remove the trailing comma and space
            output = output.rstrip(", ")
        elif self.y_header in setterInstance.df.columns:
            output += f"{self.y_header} = {self.yAtX}"
        else:
            output = f"'{self.y_header}' is not a selectable header. Please use 'gmid view' to see selectable headers."
        return output


# FIXME: We need to implement the output strings better
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
        for item in self.headers:
            outstr = f"{item}"
        return outstr


# TODO: Implement Me
class InterpAnnotateStrat(OptionStrategy):
    """Interpolates a header or a tuple of headers with plot annotations"""

    def __init__(self, params):
        super().__init__()

    def execute(self):
        return

    def print(self):
        return ""
