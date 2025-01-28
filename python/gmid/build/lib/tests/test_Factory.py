import unittest
from util import gmidTestCase, common
from gmid.factories.Factory import MainFactory, InterpFactory, PlotFactory, VSPlotFactory, SetFactory, ViewFactory
from gmid.factories.strategies.InterpStrategies import InterpHeaderStrat, InterpAnnotateStrat, InterpHeadStrat

class testFactory(gmidTestCase):
    def test_create_interp(self):
        result = MainFactory.create("Interp")
        self.assertIs(result, InterpFactory, 
                      self.tag + "failed to create InterpFactory")
    
    def test_create_plot(self):
        result = MainFactory.create("Plot")
        self.assertIs(result, PlotFactory,
                      self.tag + "failed to create PlotFactory")

    def test_create_vsplot(self):
        result = MainFactory.create("VSPlot")
        self.assertIs(result, VSPlotFactory, 
                      self.tag + "failed to create VSPlotFactory")

    def test_create_set(self):
        result = MainFactory.create("Set")
        self.assertIs(result, SetFactory, 
                      self.tag + "failed to create SetFactory")
                      
    def test_create_view(self):
        result = MainFactory.create("View")
        self.assertIs(result, ViewFactory, 
                      self.tag + "failed to create ViewFactory")
'''
class testInterpFactory(gmidTestCase):
    def test_create_header(self):
        result = InterpFactory.create("header", None)
        self.assertIs(result, InterpHeaderStrat(None))

    def test_create_head(self): 
        result = InterpFactory.create("head", None)
        self.assertIs(result, InterpHeadStrat(None))

    def test_create_annotated(self):        
        result = InterpFactory.create("annotated", None)
        self.assertIs(result, InterpAnnotateStrat(None))
'''

if __name__ == "__main__":
    unittest.main()