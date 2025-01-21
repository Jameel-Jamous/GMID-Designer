from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.interpolator import Interpolator as interp
from gmid.plotter import Plotter
from gmid.settings import setterInstance


class PlotHeaderStrat(OptionStrategy):
    def __init__(self, params, flags):
        super().__init__()
        self.x_header = setterInstance.header
        self.y_header = params
        self.flags = flags
        self.outDict = {}
        self.thePlotter = None

    def plotterWithAnnotations(self, xHeader, yHeader, xAnno, yAnno):
        self.thePlotter = (
            Plotter(xHeader=xHeader, yHeader=yHeader)
            .plot()
            .annotate(
                xdata=xAnno, ydata=interp(xHeader=xHeader, yHeader=yHeader).execute()
            )
        )
        return self

    def execute(self, holdOn=False):
        stop = holdOn
        # Check if the y header is in the data frame
        if self.y_header in setterInstance.df.columns:
            # Check if we need to make an annotated plot
            if "annotated" in self.flags:
                yAtX = interp(xHeader=self.x_header, yHeader=self.y_header).execute()
                self.plotterWithAnnotations(
                    xHeader=self.x_header,
                    yHeader=self.y_header,
                    xAnno=setterInstance.value.equate(),
                    yAnno=yAtX,
                )
            else:
                self.thePlotter = Plotter(
                    xHeader=setterInstance.header, yHeader=self.y_header
                ).plot()
        # Otherwise, check if the yheader is the 'all' header
        elif self.y_header == "all":
            temp = [
                item
                for item in setterInstance.df.columns
                if item != setterInstance.header
            ]
            temp2 = PlotHeadStrat(temp, self.flags)
            self.outDict = temp2.execute()
            temp2.thePlotter.show()
        # Otherwise check if the yheader is the 'pass' header
        elif self.y_header != "pass":
            self.outDict[self.y_header] = False
        # Otherwise, could not make plot and function has failed
        else:
            self.outDict[self.y_header] = False

        # Determine if it needs to return self (to be reused) or if returning complete flag
        if not stop:
            self.outDict[self.y_header] = True
            ret = self.outDict
            if self.thePlotter is not None:
                self.thePlotter.show()
        else:
            ret = self

        return ret

    def print(self):
        return f"<Header> : {self.y_header}, {self.flags}, {self.outDict}, {self.thePlotter}"


class PlotHeadStrat(OptionStrategy):
    def __init__(self, params, flags):
        super().__init__()
        self.headers = params
        self.flags = flags
        self.outDict = {}
        self.thePlotter = None

    def execute(self):
        for item in self.headers:
            temp = PlotHeaderStrat(item, self.flags).execute(holdOn=True)
        if len(self.headers) != 1:
            temp.y_header = "pass"
            self.thePlotter = temp.thePlotter
        return self.outDict

    def print(self):
        return f"<Head> : {self.headers}, {self.flags}, {self.thePlotter}"


class PlotAnnotatedStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()
        self.wasSet = True

    def execute(self):
        return {}

    def print(self):
        return f"<Annotate> : {self.wasSet}"


# TODO: Consider Merging/Implementing these on the other two strategies.
# Use the factory to do so.
class PlotPdfStrat(OptionStrategy):
    def __init__(self, params, flags=None):
        super().__init__()
        self.wasSet = True

    def execute(self):
        return {}

    def print(self):
        return f"<pdf> : {self.wasSet}"


class PlotJpegStrat(OptionStrategy):
    pass
