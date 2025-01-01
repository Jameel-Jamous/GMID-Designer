from util import gmidTestCase
from gmid.settings import setterInstance

class testSetter(gmidTestCase):
    def testSingleton(self):
        instance1 = setterInstance
        instance2 = setterInstance
        instance2.header = "Not None"
        self.assertIs(instance1, instance2)
        self.assertEqual(instance1.header, instance2.header)
        