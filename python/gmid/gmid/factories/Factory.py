from gmid.factories.strategies.InterpStrategies import InterpAnnotateStrat, InterpHeaderStrat, InterpHeadStrat
from gmid.factories.strategies.PlotStrategies import PlotHeaderStrat, PlotPdfStrat, PlotJpegStrat, PlotHeadStrat
from gmid.factories.strategies.VSPlotStrategies import VSPlotHeaderStrat, VSPlotPdfStrat, VSPlotJpegStrat
from gmid.factories.strategies.SetStrategies import SetHeadStrat, SetValueStrat
from gmid.factories.strategies.ViewStrategies import ViewHeadStrat, ViewPathStrat, ViewVarListStrat, ViewVarStrat

class MainFactory():
    @staticmethod
    def create(fact : str):
        if(fact == "Interp"):
            return InterpFactory
        elif(fact == "Plot"):
            return PlotFactory
        elif(fact == "VSPlot"):
            return VSPlotFactory
        elif(fact == "Set"):
            return SetFactory
        elif(fact == "View"):
            return ViewFactory
        else:
            raise ValueError("Unknown Factory Type")

class InterpFactory():
    @staticmethod
    def create(strat : str, params):
        """Factory method that returns a strategy based on the input."""
        if(strat == "header"):
            return InterpHeaderStrat(params)
        elif(strat == "head"):
            return InterpHeadStrat(params)
        elif(strat == "annotated"):
            return InterpAnnotateStrat(params)
        else:
            raise ValueError("Unknown Interp Strategy Type")

class PlotFactory():
    @staticmethod
    def create(strat : str, params):
        if(strat == "header"):
            return PlotHeaderStrat(params)
        elif(strat == "pdf"):
            return PlotPdfStrat(params)
        elif(strat == "jpeg"):
            return PlotJpegStrat(params)
        elif(strat == "head"):
            return PlotHeadStrat(params)
        else:
            raise ValueError("Unknown Plot Strategy Type")

class VSPlotFactory():
    @staticmethod
    def create(strat : str, params):
        if(strat == "header"):
            return VSPlotHeaderStrat(params)
        elif(strat == "pdf"):
            return VSPlotPdfStrat(params)
        elif(strat == "jpeg"):
            return VSPlotJpegStrat(params)
        else:
            raise ValueError("Unknown VSPlot Strategy Type")

class SetFactory():
    @staticmethod
    def create(strat : str, params):
        if(strat == "header"):
            return SetHeadStrat(params)
        elif(strat == "pdf"):
            return SetValueStrat(params)
        else:
            raise ValueError("Unknown Set Strategy Type")

class ViewFactory():
    @staticmethod
    def create(strat : str, params):
        if(strat == "head"):
            return ViewHeadStrat(params)
        elif(strat == "path"):
            return ViewPathStrat(params)
        elif(strat == "var"):
            return ViewVarStrat(params)
        elif(strat == "var_list"):
            return ViewVarListStrat(params)
        else:
            raise ValueError("Unknown View Strategy Type")