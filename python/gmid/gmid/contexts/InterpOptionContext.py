from OptionContext import OptionContext
from gmid.factories.Factory import MainFactory

class InterpOptionContext(OptionContext):
    def __init__(self, args, kwargs):
        self.__reset__()
        super.__init__(args, kwargs)

    def __reset__(self):
        self.output = None

    def toStrategy(self):
        for keys, values in self.options.items():
            self.append(MainFactory.create("Interp").create(keys, values))

    def execute(self):
        if not self.isEmpty():
            for item in self.strategies:
                self.output = item.execute()
     
            