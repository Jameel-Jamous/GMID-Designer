import src.blocks as bl
import unittest as ut

class TestToken(ut.TestCase):
    def testInit(self):
        aToken = bl.Token("IDENTIFIER", "x")
        self.assertEqual(aToken.kind, "IDENTIFIER", "Token: kind not initialized properly")
        self.assertEqual(aToken.value, "x", "Token: value not initialized properly")
    
    def testReprAndToStr(self):
        aToken = bl.Token("IDENTIFIER", "x")
        self.assertEqual(aToken.toStr(), "Token(IDENTIFIER, 'x')", "Token: repr/toStr outputs incorrectly") 