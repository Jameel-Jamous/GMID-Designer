"""
This tests both: the stratigies and the Interpolator.
"""

from util import gmidTestCase

from gmid.factories.strategies.InterpStrategies import (
    InterpHeaderStrat,
    InterpHeadStrat,
)
from gmid.settings import setterInstance
from gmid.utils.SI import SI


class testInterpHeaderStrategies(gmidTestCase):
    def testExecute(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        interpValue = InterpHeaderStrat("vov").execute()
        self.assertEqual(type(interpValue), dict)
        self.assertEqual(interpValue, {"vov": 2.0})

    def testDiffHeader(self):
        setterInstance.header = "vov"
        setterInstance.value = SI("2")
        interpValue = InterpHeaderStrat("gmid").execute()
        self.assertEqual(type(interpValue), dict)
        self.assertEqual(interpValue, {"gmid": 1.0})

    def testHeaderNotThere(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        interpValue = InterpHeaderStrat("cdsovercgs").execute()
        self.assertEqual(type(interpValue), dict)
        self.assertEqual(interpValue, {"Invalid": "cdsovercgs"})


class testInterpHeadStrategies(gmidTestCase):
    def testExecute(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        headers = ("vov", "jd")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), dict)
        self.assertEqual(interped, {"vov": 2.0, "jd": 3.0})

    def testDiffHeader(self):
        setterInstance.header = "vov"
        setterInstance.value = SI("2")
        headers = ("gmid", "jd")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), dict)
        self.assertEqual(interped, {"gmid": 1, "jd": 3})

    def testHeadersNotThere(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        headers = ("cdsovercgs", "something", "another")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), dict)
        self.assertEqual(interped, {"Invalid": "another"})
