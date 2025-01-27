from gmid.contexts.OptionContext import OptionContext
from gmid.factories.Factory import MainFactory
from gmid.plotter import plotterInstance


class PlotOptionContext(OptionContext):
    def __init__(self, args, kwargs):
        self.__reset__()
        super().__init__(args, kwargs)
        self.toStrategy()

    def __reset__(self):
        self.output = []

    def toStrategy(self):
        self.filterOptions()
        for strat, params in self.options.items():
            self.append(
                MainFactory.create("Plot").create(strat, params, flags=self.getFlags())
            )
        # Pass the options to the plotter instance
        plotterInstance.options = self.options

    def getFlags(self):
        temp = []
        for key, item in self.options.items():
            if type(item) is bool:
                temp.append(key)
        return temp

    def execute(self):
        if not self.isEmpty():
            for item in self.strategies:
                self.output.append(item.execute())
        plotterInstance.plot().show()
        return self

    def print(self):
        outstr = ""
        for eachDict in self.output:
            for key, value in eachDict.items():
                if not value:
                    outstr += f"'{key}' is not a plottable header. Please use 'gmid view' to see plottable headers."

        return outstr
