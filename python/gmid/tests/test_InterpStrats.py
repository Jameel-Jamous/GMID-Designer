import unittest
from util import gmidTestCase
from gmid.factories.strategies.InterpStrategies import InterpHeaderStrat, InterpAnnotateStrat, InterpHeadStrat
from gmid.settings import setterInstance
from gmid.utils.SI import SI

class testInterpHeaderStrategies(gmidTestCase):
    def testExecute(self):
        # Ensure setter is set correctly 
        # Make sure you are testing this class using
        # 'nmos2.csv'
        setterInstance.header = "gmid" 
        setterInstance.value = SI("1")
        interpValue = InterpHeaderStrat("vov").execute()
        self.assertEqual(type(interpValue), float)
        self.assertEqual(interpValue, 2)
       
    def testDiffHeader(self):
        setterInstance.header = "vov"
        setterInstance.value = SI("2") 
        interpValue = InterpHeaderStrat("gmid").execute()
        self.assertEqual(type(interpValue), float)
        self.assertEqual(interpValue, 1)        

    def testHeaderNotThere(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        interpValue = InterpHeaderStrat("jd").execute()
        self.assertIsNone(interpValue)

class testInterpHeadStrategies(gmidTestCase):
    def testExecute(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        headers = ("vov", "gmovergds", "cdsovercgs")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), list)
        self.assertEqual(interped, [2, 3, 4])
    
    def testDiffHeader(self):
        setterInstance.header = "vov"
        setterInstance.value = SI("2")
        headers = ("gmid", "gmovergds", "cdsovercgs")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), list)
        self.assertEqual(interped, [1, 3, 4])

    def testHeadersNotThere(self):
        setterInstance.header = "gmid"
        setterInstance.value = SI("1")
        headers = ("jd", "something", "another")
        interped = InterpHeadStrat(headers).execute()
        self.assertEqual(type(interped), list)
        self.assertEqual(interped, [None, None, None])