import unittest
from util import gmidTestCase, common
from gmid.DFManager import DFManager as dfm

class testDFM(gmidTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testDFM = dfm()

    def testInit(self):
       self.assertDictEqual(self.testDFM.flags, {
            "VALID_PATH" : False,
            "INVALID_PATH" : False,
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
       })
       self.assertEqual(self.testDFM.path, "")
       self.assertIsNone(self.testDFM.df)
       self.assertEqual(self.testDFM.headers, [])
    
    def testValidPathAgainstValidPath(self):
        isValidPath = self.testDFM.checkValidPath(common["NMOS_DIR"] + "/nmos.csv")
        self.assertEqual(isValidPath, True)
        self.assertEqual(self.testDFM.flags["VALID_PATH"], True)
        self.assertEqual(self.testDFM.flags["INVALID_PATH"], False)
    
    def testValidPathAgainstInvalidPath(self):
        isValidPath = self.testDFM.checkValidPath(common["NMOS_DIR"] + "/pmos.csv")
        self.assertEqual(isValidPath, False)
        self.assertEqual(self.testDFM.flags["VALID_PATH"], False)
        self.assertEqual(self.testDFM.flags["INVALID_PATH"], True)
        isValidPath = self.testDFM.checkValidPath(common["NMOS_DIR"])
        self.assertEqual(isValidPath,False)
        self.assertEqual(self.testDFM.flags["VALID_PATH"], False)
        self.assertEqual(self.testDFM.flags["INVALID_PATH"], True)

    def testGetHeaderLine(self):
       #TODO: Implement Me 
       return
