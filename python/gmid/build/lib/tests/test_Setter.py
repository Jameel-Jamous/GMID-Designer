import pandas as pd
from util import gmidTestCase

from gmid.settings import setterInstance
from gmid.utils.SI import SI


class testSetter(gmidTestCase):
    def testSingleton(self):
        instance1 = setterInstance
        instance2 = setterInstance
        self.assertIs(instance1, instance2)
        self.assertEqual(instance1.header, instance2.header)

    def testInitPaths(self):
        pathsFound = setterInstance.initPaths()
        self.assertEqual(pathsFound, True)
        self.assertIsNot(setterInstance.paths["Data"], "")
        self.assertIsNot(setterInstance.paths["Install"], "")
        self.assertIsNot(setterInstance.paths["Config"], "")

    def testInitDf(self):
        wasInit = setterInstance.initDf()
        self.assertEqual(wasInit, True)
        self.assertIsNotNone(setterInstance.df)
        self.assertEqual(type(setterInstance.df), pd.DataFrame)

    def testLoadHeader(self):
        setterInstance.header = "gmid"
        storedHeader = setterInstance.load("Header")
        self.assertEqual(type(storedHeader), str, f"{storedHeader}")
        self.assertEqual(storedHeader, "gmid")
        self.assertEqual(setterInstance.header, "gmid")

    def testLoadValue(self):
        setterInstance.value = SI("1.5k")
        storedValue = setterInstance.load("Value")
        self.assertEqual(type(storedValue), SI, f"{storedValue}")
        self.assertEqual(storedValue, SI("1.5k"))
        self.assertEqual(setterInstance.value, SI("1.5k"))

    def testValueFlags(self):
        setterInstance.initDf()
        setterInstance.value = SI("10.0M")
        flags = setterInstance.valueFlag
        self.assertEqual(flags, ["OutOfBounds"])
