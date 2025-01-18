from gmid.contexts.OptionContext import OptionContext
from gmid.factories.Factory import MainFactory


class ViewOptionContext(OptionContext):
    def __init__(self, args, kwargs):
        self.__reset__()
        super().__init__(args, kwargs)
        self.toStrategy()

    def __reset__(self):
        self.output = None

    def toStrategy(self):
        for keys, values in self.options.items():
            self.append(MainFactory.create("View").create(keys, values))

    def execute(self):
        if not self.isEmpty():
            for item in self.strategies:
                self.output = item.execute()
        return self

    def print(self):
        temp = ""
        if not self.isEmpty():
            for item in self.strategies:
                temp += item.print()
        return temp
