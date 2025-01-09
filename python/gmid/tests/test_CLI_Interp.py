import unittest
from util import gmidTestCase
from gmid.settings import setterInstance
from gmid.commands.setter import main as setterMain
from gmid.commands.interp import main as interpMain
from gmid.utils.SI import SI

class testCLIInterp(gmidTestCase):
    def testInterpDefaultInRange(self):
        self.cli.invoke(setterMain)
        executed = self.cli.invoke(interpMain, ['vov'])
        self.assertEqual("\'gmid\' set to \'1.0\' was \'1.5k\'\n", executed.output)
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value) 
       