from gmid.factories.strategies.InterpStrategies import (
    InterpAnnotateStrat,
    InterpHeaderStrat,
    InterpHeadStrat,
)
from gmid.factories.strategies.PlotStrategies import (
    PlotAnnotatedStrat,
    PlotFiguresStrat,
    PlotHeaderStrat,
    PlotHeadStrat,
    PlotOutputAsStrat,
    PlotZoomStrat,
)
from gmid.factories.strategies.SetStrategies import SetHeadStrat, SetValueStrat
from gmid.factories.strategies.ViewStrategies import (
    ViewAllHeadersStrat,
    ViewHeadStrat,
    ViewPathStrat,
    ViewValueStrat,
)
from gmid.factories.strategies.VSPlotStrategies import (
    VSPlotHeaderStrat,
    VSPlotOutputAsStrat,
)


class MainFactory:
    @staticmethod
    def create(fact: str):
        if fact == "Interp":
            return InterpFactory
        elif fact == "Plot":
            return PlotFactory
        elif fact == "VSPlot":
            return VSPlotFactory
        elif fact == "Set":
            return SetFactory
        elif fact == "View":
            return ViewFactory
        else:
            raise ValueError("Unknown Factory Type")


class InterpFactory:
    @staticmethod
    def create(strat: str, params):
        """Factory method that returns a strategy based on the input."""
        if strat == "header":
            return InterpHeaderStrat(params)
        elif strat == "head":
            return InterpHeadStrat(params)
        elif strat == "annotated":
            return InterpAnnotateStrat(params)
        else:
            raise ValueError("Unknown Interp Strategy Type")


class PlotFactory:
    @staticmethod
    def create(strat: str, params, flags=None):
        if strat == "header":
            return PlotHeaderStrat(params, flags)
        elif strat == "zoom":
            return PlotZoomStrat(params, flags)
        elif strat == "head":
            return PlotHeadStrat(params, flags)
        elif strat == "annotated":
            return PlotAnnotatedStrat(params, flags)
        elif strat == "output_as":
            return PlotOutputAsStrat(params, flags)
        elif strat == "figures":
            return PlotFiguresStrat(params, flags)
        else:
            raise ValueError(f"Unknown Plot Strategy Type: {strat}")


class VSPlotFactory:
    @staticmethod
    def create(strat: str, params, flags):
        if strat == "yx_header":
            return VSPlotHeaderStrat(params, flags)
        elif strat == "output_as":
            return VSPlotOutputAsStrat(params, flags)
        else:
            raise ValueError(f"Unknown VSPlot Strategy Type: {strat}")


class SetFactory:
    @staticmethod
    def create(strat: str, params):
        if strat == "head":
            return SetHeadStrat(params)
        elif strat == "value_to_set":
            return SetValueStrat(params)
        else:
            raise ValueError("Unknown Set Strategy Type")


class ViewFactory:
    @staticmethod
    def create(strat: str, params):
        if strat == "using_head":
            return ViewHeadStrat(params)
        elif strat == "path":
            return ViewPathStrat(params)
        elif strat == "value":
            return ViewValueStrat(params)
        elif strat == "all_headers":
            return ViewAllHeadersStrat(params)
        else:
            raise ValueError(f"Unknown View Strategy Type: {strat}")
