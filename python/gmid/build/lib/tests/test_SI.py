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

    def test_fromStrValidExpPos(self):
        aFloat = SI().fromStr("10.5k")
        self.assertTupleEqual((10.5, 'k'), aFloat)

    def test_fromStrValidExp0(self):
        aFloat = SI().fromStr("10.5")
        self.assertTupleEqual((10.5, ''), aFloat)

    def test_fromStrValidPosNumPosExp(self):
        aFloat = SI().fromStr("105m")
        self.assertTupleEqual((105, 'm'), aFloat)
   
    def test_fromStrValidNegNumPosExp(self):
        aFloat = SI().fromStr("-10.5k")
        self.assertTupleEqual((-10.5, 'k'), aFloat)
    
    def test_fromStrValidZero(self):
        aFloat = SI().fromStr("0")
        self.assertTupleEqual((0, ''), aFloat)
    
    def test_fromStrValidMin(self):
        aFloat = SI().fromStr("1")
        self.assertTupleEqual((1, ''), aFloat)
    
    def test_fromStrValidMax(self):
        aFloat = SI().fromStr("999")
        self.assertTupleEqual((999, ''), aFloat)

    def test_fromStrValidPosNumPosExp(self):
        aFloat = SI().fromStr("10500")
        self.assertTupleEqual((10.5, 'k'), aFloat)
    
    def test_fromStrValidPosNumNegExp(self):
        aFloat = SI().fromStr("0.000105")
        self.assertTupleEqual((105, 'u'), aFloat)

    def test_fromStrInvalid(self):
        aFloat = SI().fromStr("10aaaa.5k")
        self.assertIsNone(aFloat)
    
    def test_fromFloatValidPosNumPosExp(self):
        aFloat = SI().fromFloat(10751)
        self.assertTupleEqual((10.751, 'k'), aFloat)
    
    def test_fromFloatValidNegNumPosExp(self):
        aFloat = SI().fromFloat(-10500)
        self.assertTupleEqual((-10.5, 'k'), aFloat)
    
    def test_fromFloatValidNegNumNegExp(self):
        aFloat = SI().fromFloat(-0.000105)
        self.assertTupleEqual((-105, 'u'), aFloat)

    def test_fromFloatValidRecursionPosExp(self):
        aFloat = SI().fromFloat(1000000751)
        self.assertTupleEqual((1.000000751, 'G'), aFloat)
    
    def test_fromFloatValidPosNumNegExp(self):
        aFloat = SI().fromFloat(0.105)
        self.assertTupleEqual((105, 'm'), aFloat)

    def test_fromFloatValidRecursionNegExp(self):
        aFloat = SI().fromFloat(0.000000105)
        self.assertTupleEqual((105, 'n'), aFloat)

    def test_fromFloatValidZero(self):
        aFloat = SI().fromFloat(0)
        self.assertTupleEqual((0, ''), aFloat)

    def test_fromFloatValidMin(self):
        aFloat = SI().fromFloat(1)
        self.assertTupleEqual((1, ''), aFloat)

    def test_fromFloatValidMax(self):
        aFloat = SI().fromFloat(999)
        self.assertTupleEqual((999, ''), aFloat)
 
    def test_toStrPosNumPosExp(self):
        aStr = SI(float=12345).toStr()
        self.assertEqual("12.345k", aStr)
    
    def test_toStrPosNumNegExp(self):
        aStr = SI(float=0.12345).toStr()
        self.assertEqual("123.45m", aStr)
    
    def test_toStrNegNumPosExp(self):
        aStr = SI(float=-12345).toStr()
        self.assertEqual("-12.345k", aStr)
    
    def test_toStrNegNumNegExp(self):
        aStr = SI(float=-0.12345).toStr()
        self.assertEqual("-123.45m", aStr)
    
    def test_toStrZero(self):
        aStr = SI(float=0).toStr()
        self.assertEqual("0", aStr)
    
    def test_toStrPosNumPosExpENotation(self):
        aStr = SI(float=12345).toStr(True)
        self.assertEqual("12.345e3", aStr)
    
    def test_toStrPosNumNegExp(self):
        aStr = SI(float=0.12345).toStr(True)
        self.assertEqual("123.45e-3", aStr)
    
    def test_toStrNegNumPosExp(self):
        aStr = SI(float=-12345).toStr(True)
        self.assertEqual("-12.345e3", aStr)
    
    def test_toStrNegNumNegExp(self):
        aStr = SI(float=-0.12345).toStr(True)
        self.assertEqual("-123.45e-3", aStr)    
    
    def test_addable(self):
        num1 = SI(float=999)
        num2 = SI(float=1)
        self.assertEqual(1000, num1 + num2)
    
    def test_subtractable(self):
        num1 = SI(float=1000)
        num2 = SI(float=1)
        self.assertEqual(999, num1 - num2)
    
    def test_multiplicable(self):
        num1 = SI(float=10)
        num2 = SI(float=100)
        self.assertEqual(1000, num1 * num2)
    
    def test_divisable(self):
        num1 = SI(float=10000)
        num2 = SI(float=10)
        self.assertEqual(1000, num1 / num2)
   
    def test_comparableEQ(self):
        num1 = SI(float=100)
        num2 = SI(float=100)
        self.assertEqual(True, num1 == num2)

    def test_comparableGT(self):
        num1 = SI(float=100)
        num2 = SI(float=10)
        self.assertEqual(True, num1 > num2)

    def test_comparableLT(self):
        num1 = SI(float=10)
        num2 = SI(float=100)
        self.assertEqual(True, num1 < num2)

    def test_comparableGE(self):
        num1 = SI(float=100)
        num2 = SI(float=100)
        self.assertEqual(True, num1 >= num2)

    def test_comparableLE(self):
        num1 = SI(float=100)
        num2 = SI(float=100)
        self.assertEqual(True, num1 <= num2)