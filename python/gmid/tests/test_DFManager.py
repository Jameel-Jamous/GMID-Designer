import unittest
import pickle
from util import gmidTestCase, common
from gmid.DFManager import DFManager 

class testDFM(gmidTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DFM = DFManager()
        
    def testSingleton(self):
        instance2 = DFManager()
        self.assertIs(self.DFM, instance2)

    """def testReset(self):
       self.__reset__()
       self.assertDictEqual(self.flags, {
            "VALID_PATH" : False,
            "INVALID_PATH" : False,
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
       })
       self.assertEqual(self.path, "")
       self.assertIsNone(self.df)
       self.assertEqual(self.headers, [])
    
    def testValidPathAgainstValidPath(self):
        isValidPath = self.__checkValidPath__(common["NMOS_DIR"] + "/nmos.csv")
        self.assertEqual(isValidPath, True)

    def testValidPathAgainstInvalidPath(self):
        isValidPath = self.__checkValidPath__(common["NMOS_DIR"] + "/pmos.csv")
        self.assertEqual(isValidPath, False)
        isValidPath = self.__checkValidPath__(common["NMOS_DIR"])
        self.assertEqual(isValidPath,False)
    
    def testGetHeaderLine(self):
        header_line = self.__getHeaderLine__(common["NMOS_DIR"] + "/nmos.csv")
        self.assertEqual("vov,gmid", header_line)

    def testValidCSVAgainstValidCSV(self):
        flagState = self.flags
        isValidCSV = self.__checkValidCSV__(common["NMOS_DIR"] + "/nmos.csv")
        self.assertEqual(isValidCSV, "VALID_FILE")
        self.assertEqual(flagState, self.flags)

    def testValidCSVAgainstInvalidCSV(self):
        flagState = self.flags
        isValidCSV = self.__checkValidCSV__(common["SAMPLE_DIR"] + "/exponent.csv")
        self.assertEqual(isValidCSV, "INVALID_FILE")
        self.assertEqual(flagState, self.flags)

    def testValidCSVAgainstEmptyCSV(self):
        flagState = self.flags
        isValidCSV = self.__checkValidCSV__(common["SAMPLE_DIR"] + "/empty.csv")
        self.assertEqual(isValidCSV, "EMPTY_FILE")
        self.assertEqual(flagState, self.flags)

    def testSetFileFlagsWithEmpty(self):
        self.__reset__()
        self.__setFileFlags__("EMPTY_FILE")
        self.assertEqual(self.flags["VALID_FILE"], False)
        self.assertEqual(self.flags["INVALID_FILE"], False)
        self.assertEqual(self.flags["EMPTY_FILE"], True)

    def testSetFileFlagsWithValid(self):
        self.__reset__()
        self.__setFileFlags__("VALID_FILE")
        self.assertEqual(self.flags["VALID_FILE"], True)
        self.assertEqual(self.flags["INVALID_FILE"], False)
        self.assertEqual(self.flags["EMPTY_FILE"], False)

    def testSetFileFlagsWithInvalid(self):
        self.__reset__()
        self.__setFileFlags__("INVALID_FILE")
        self.assertEqual(self.flags["VALID_FILE"], False)
        self.assertEqual(self.flags["INVALID_FILE"], True)
        self.assertEqual(self.flags["EMPTY_FILE"], False)
    
    def testSetPathWithValid(self):
       isPathSet = self.setPath(common["NMOS_DIR"] + r"\nmos.csv")

       self.assertEqual(self.path, common["NMOS_DIR"] + r"\nmos.csv")

       self.assertDictEqual(self.flags, {
            "VALID_PATH" : True,
            "INVALID_PATH" : False,
            "VALID_FILE" : True,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
        })
       self.assertEqual(isPathSet, True)

    def testSetPathWithInvalid(self):
        isPathSet = self.setPath(common["SAMPLE_DIR"] + r"\exponent.csv")

        self.assertEqual(self.path, "")
        self.assertDictEqual(self.flags, {
            "VALID_PATH" : True,
            "INVALID_PATH" : False,
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : True,
        })
        self.assertEqual(isPathSet, False)

    def testSetPathWithEmpty(self):
        isPathSet = self.setPath(common["SAMPLE_DIR"] + r"\empty.csv")

        self.assertEqual(self.path, common["SAMPLE_DIR"] + r"\empty.csv")
        self.assertDictEqual(self.flags, {
            "VALID_PATH" : True,
            "INVALID_PATH" : False,
            "VALID_FILE" : False,
            "EMPTY_FILE" : True,
            "INVALID_FILE" : False,
        })
        self.assertEqual(isPathSet, True)

    def testSetPathWithInvalidPath(self):
        isPathSet = self.setPath("an/invalid/path")

        self.assertEqual(self.path, "")
        self.assertDictEqual(self.flags, {
            "VALID_PATH" : False,
            "INVALID_PATH" : True,
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
        })
        self.assertEqual(isPathSet, False)
    
    def testPicklePath(self):
        self.__reset__()
        self.setPath(common["NMOS_DIR"] + r"\nmos.csv")
        self.picklePath()

        install_path = self.__getInstallPath__() + r"\pkl\data.pkl"
        with open(install_path, "rb") as file:
            temp = pickle.load(file)
            file.close()
        
        self.assertEqual(temp, common["NMOS_DIR"] + r"\nmos.csv")        
"""        
