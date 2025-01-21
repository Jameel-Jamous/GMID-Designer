from gmid.contexts.OptionContext import OptionContext
from gmid.factories.Factory import MainFactory
from gmid.settings import setterInstance


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
            for item in self.strategies:
                self.output.append(item.execute())
        return self

    def print(self):
        outstr = f"For '{setterInstance.header}' = {setterInstance.value}:\n\n\t"
        errstr = ""
        self.output = sorted(self.output, key=lambda k: len(k))
        for eachDict in self.output:
            for key, value in eachDict.items():
                if key != "Invalid":
                    outstr += f"'{key}' = {value}, "
                else:
                    errstr = f"'{value}' is not a selectable header. Please use 'gmid view' to see selectable headers."
        if errstr == "":
            outstr = outstr.rstrip(", ")
        else:
            outstr = errstr
        return outstr
