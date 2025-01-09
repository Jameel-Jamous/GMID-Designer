from gmid.contexts.OptionContext import OptionContext
from gmid.factories.Factory import MainFactory
from gmid.factories.strategies.SetStrategies import SetHeadStrat, SetValueStrat

class SetOptionContext(OptionContext):
    def __init__(self, args, kwargs):
        self.__reset__()
        super().__init__(args, kwargs)
        self.toStrategy()

    def __reset__(self):
        self.output = None

    def toStrategy(self):
        for keys, values in self.options.items():
            self.append(MainFactory.create("Set").create(keys, values))

    def execute(self):
        if(not self.isEmpty()):
            for item in self.strategies:
                self.output = item.execute()
        return self
            
    def print(self):
        tail = ""
        head = ""
        if(not self.isEmpty()):
            for item in self.strategies:
                if(isinstance(item, SetHeadStrat)):
                    head = item.print()
                else:
                    tail += item.print()
        return head + tail 
