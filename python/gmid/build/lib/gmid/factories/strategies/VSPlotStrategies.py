from gmid.factories.strategies.PlotStrategies import PlotHeaderStrat, PlotOutputAsStrat


class VSPlotHeaderStrat(PlotHeaderStrat):
    def __init__(self, params, flags):
        super().__init__(params, flags)
        self.x_header = params[1]
        self.y_header = params[0]
        if self.x_header == "all":
            self.outDict = {f"{self.x_header}": False}

        if self.y_header == "all":
            self.outDict = {f"{self.y_header}": False}

    def execute(self):
        if self.x_header != "all" and self.y_header != "all":
            self.outDict = super().execute()
        return self.outDict


class VSPlotOutputAsStrat(PlotOutputAsStrat):
    def __init__(self, params, flags):
        super().__init__(params, flags)

    def execute(self):
        return super().execute()
