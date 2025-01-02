from gmid.utils.SI import SI
from util import gmidTestCase
from gmid.settings import setterInstance

class testSI(gmidTestCase):
    def __init__(self, args):
        super().__init__(args)
        self.tag = ""

    def test_check(self):
        validity = SI().check("10.5k")
        self.assertEqual(True, validity, "failed vs. valid float & valid si: 10.5k")    
        validity1 = SI().check("10.5")
        self.assertEqual(True, validity1, "failed vs. valid float: 10.5")

        validity2 = SI().check("10aaaaaa.5k") 
        self.assertEqual(False, validity2, 
                         "failed vs. invalid float & valid si: 10aaaaaa.5k")

        validity3 = SI().check("aaaaa10.5k")
        self.assertEqual(False, validity3,
                         "failed vs. invalid float & valid si: aaaaa10.5k")
                         
        
        #validity4 go against whole dict

    def test_fromStrValid(self):
        float1 = SI().fromStr("10.5k")
        self.assertEqual(10.5e3, float1)

    def test_fromStrValid2(self):
        float2 = SI().fromStr("10.5")
        self.assertEqual(10.5, float2)
    
    def test_fromStrValid3(self):
        float3 = SI().fromStr("10aaaa.5k")
        self.assertIsNone(float3)
    
    def test_fromFloatValid(self):
        float1 = SI().fromFloat(10751)
        self.assertEqual(float1, 10751)
   
    def test_fromFloatRecursion(self):
        float1 = SI().fromFloat(1000000751)
        self.assertEqual(float1, 1000000751)
    
    def test_toStrSINotation(self):
        theSI = SI(float=1234).toStr()
        self.assertEqual("1.234k", theSI)
    
    def test_toStrENotation(self):
        theSI = SI(float=1234).toStr(e_notation=True)
        self.assertEqual("1.234e3", theSI)

    def test_toStrLong(self):
        theSI = SI(float=0.135).toStr(e_notation=True)
        self.assertEqual("1.35e-3", theSI)