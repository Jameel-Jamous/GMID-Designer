"""
This tests both: the stratigies and the Interpolator.
"""

from util import gmidTestCase

from gmid.plotter import Plotter


class testPlotter(gmidTestCase):
    def testFormatHeader(self):
        plotterObj = Plotter(xHeader="gmid", yHeader="vov")
        result = plotterObj.formatHeader("gmOverid")
        self.assertEqual(result, "$g_{m}/i_{d}$ [S/A]")

    def testFormatHeaderVOV(self):
        plotterObj = Plotter(xHeader="gmid", yHeader="vov")
        result = plotterObj.formatHeader("vov")
        self.assertEqual(result, "$v_{ov}$ [V]")

    def testFormatHeaderCGSOVERCDS(self):
        plotterObj = Plotter(xHeader="gmid", yHeader="vov")
        result = plotterObj.formatHeader("cgsOvercds")
        self.assertEqual(result, "$c_{gs}/c_{ds}$ [F/F]")
