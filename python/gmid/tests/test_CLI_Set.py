import unittest
from util import gmidTestCase
from gmid.settings import setterInstance
from gmid.commands.setter import main
from gmid.utils.SI import SI

class testCLISet(gmidTestCase):
    def testSetMain(self):
        executed = self.cli.invoke(main, ['1'])
        self.assertEqual("\'gmid\' set to \'1.0\' was \'1.5k\'\n", executed.output)
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value) 
    
    def testSetMainFromOther(self):
        self.cli.invoke(main, ['1'])
        executed = self.cli.invoke(main, ['2'])
        self.assertEqual("\'gmid\' set to \'2.0\' was \'1.0\'\n", executed.output)
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("2"), setterInstance.value) 
    
    def testSetOther(self):
        executed = self.cli.invoke(main, ['1', '-h', 'vov'])
        self.assertEqual(f"\'vov\' set to \'1.0\'\n", executed.output)
        self.assertEqual("vov", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value)
    
    def testSetOtherFromOther(self):
        self.cli.invoke(main, ['1', '-h', 'vov'])
        executed = self.cli.invoke(main, ['2', '-h', 'vov'])
        self.assertEqual("\'vov\' set to \'2.0\' was \'1.0\'\n", executed.output)
        self.assertEqual("vov", setterInstance.header)
        self.assertEqual(SI("2"), setterInstance.value) 
        