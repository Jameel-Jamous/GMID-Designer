from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.plotter import plotterInstance as PLI
from gmid.settings import setterInstance as STI


class PlotHeaderStrat(OptionStrategy):
    def __init__(self, params, flags):
        super().__init__()
        self.x_header = STI.header
        self.y_header = params
        self.outDict = {}

    def execute(self):
        if self.x_header in STI.df.columns and (
            self.y_header in STI.df.columns or self.y_header == "all"
        ):
            if self.y_header != "all":
                PLI.x_header = self.x_header
                PLI.y_headers.append(self.y_header)
                PLI.numOfPlots += 1
                self.outDict = {f"{self.y_header}": True}
            elif self.y_header == "all":
                temp = [item for item in STI.df.columns if item != STI.header]
                self.outDict = PlotHeadStrat(params=temp, flags=None).execute()
            else:
                self.outDict = {f"{self.y_header}": False}
        else:
            self.outDict = {f"{self.y_header}": False}
        return self.outDict

    def print(self):
        return f"<Header> : {self.y_header}, {self.outDict}"


class PlotHeadStrat(OptionStrategy):
    def __init__(self, params, flags):
        super().__init__()
        self.headers = params
        self.flags = flags
        self.outDict = {}
        self.thePlotter = None

    def execute(self):
        PLI.x_header = STI.header
        for item in self.headers:
            if item in STI.df.columns:
                PLI.y_headers.append(item)
                self.outDict.update({f"{item}": True})
            else:
                self.outDict.update({f"{item}": False})
        PLI.numOfPlots += len(self.headers)
        return self.outDict

    def print(self):
        return f"<Head> : {self.headers}, {self.flags}"


class PlotAnnotatedStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()

    def execute(self):
        PLI.options.update({"annotate": True})
        return {}

    def print(self):
        return f"<Annotate> : {None}"


class PlotZoomStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()
        if type(params) is str:
            f1, f2 = params.split(":")
        self.range = (float(f1), float(f2))

    def execute(self):
        PLI.options.update({"zoom": self.range})
        return {}

    def print(self):
        return f"<zoom> : {self.range}"


class PlotOutputAsStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()
        self.format = params

    def execute(self):
        PLI.options.update({"output_as": self.format})
        return {}

    def print(self):
        return f"<output_as> : {self.format}"


class PlotFiguresStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()

    def execute(self):
        PLI.options.update({"figures": True})
        return {}

    def print(self):
        return f"<figures> : {None}"
