from gmid.contexts.OptionContext import OptionContext
from gmid.factories.Factory import MainFactory
from gmid.factories.strategies.InterpStrategies import InterpAnnotateStrat
from gmid.plotter import plotterInstance
from gmid.settings import setterInstance
from gmid.utils.SI import SI


class InterpOptionContext(OptionContext):
    def __init__(self, args, kwargs):
        self.__reset__()
        super().__init__(args, kwargs)
        self.toStrategy()

    def __reset__(self):
        self.output = []

    def toStrategy(self):
        self.filterOptions()
        for keys, values in self.options.items():
            self.append(MainFactory.create("Interp").create(keys, values))

    def execute(self):
        if not self.isEmpty():
            for item in list(reversed(self.strategies)):
                if type(item) is not InterpAnnotateStrat:
                    self.output.append(item.execute())
                else:
                    if "all" not in self.options.values():
                        temp = [
                            values
                            for keys, values in self.options.items()
                            if (keys == "header" or keys == "head")
                        ]
                        headersToAnnotate = [
                            item
                            for sub in temp
                            for item in (sub if isinstance(sub, tuple) else (sub,))
                        ]
                        item.params = headersToAnnotate
                    else:
                        temp = [
                            item
                            for item in setterInstance.df.columns
                            if item != setterInstance.header
                        ]
                        item.params = temp
                    item.execute()
        return self

    def print(self):
        outstr = f"For '{setterInstance.header}' = {setterInstance.value}:\n\n\t"
        errstr = ""
        self.output = sorted(self.output, key=lambda k: len(k))
        for eachDict in self.output:
            for key, value in eachDict.items():
                if key != "Invalid":
                    outstr += f"'{key}' = {SI(asFloat=value)}, "
                else:
                    errstr = f"'{value}' is not a selectable header. Please use 'gmid view' to see selectable headers."
        if errstr == "":
            outstr = outstr.rstrip(", ")
        else:
            outstr = errstr

        print(outstr)
        if "annotated" in self.options:
            plotterInstance.plot().show()
        return outstr
