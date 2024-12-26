import pandas as pd
import os

class DFManager():
    def __init__(self):
        self.flags = {
            "VALID_PATH" : False,
            "INVALID_PATH" : False,
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
        }
        self.path = ""
        self.df = None
        self.headers = []
        


    def picklePath(self):
        return    
    
    def pickleSelf(self):
        return 
    
    def getHeaderLine(self, thePath):
        with open(thePath, 'r') as file:
            header_line = file.readline().strip() 
            file.close()
        return header_line

    # TODO: Consider changing the setting of flags not within
    #       the function callee but within function caller
    #       (ie. make it so flags are only set when a new path
    #       is 100% going to be used, not within checks. Take a
    #       look at the tests. Each test will change the flags
    #       w/o establishing the path)
    def checkValidCSV(self, thePath):
        isValidPath = self.checkValidPath(thePath)
        
        if(isValidPath):
            isEmpty = (os.path.getsize(thePath) == 0)
            if(isEmpty):
                self.flags["EMPTY_FILE"]
            else:
                hdr = self.getHeaderLine(thePath)
                if(hdr.split(",")[0] == "gmid"):
                    self.flags["VALID_FILE"]
                else:
                    self.flags["INVALID_FILE"]
        return isEmpty
    
    def checkValidPath(self, thePath : str):
        validPath = os.path.exists(thePath) and thePath.endswith(".csv")
        if(validPath):
            self.flags["VALID_PATH"] = True
            self.flags["INVALID_PATH"] = False
        else:
            self.flags["INVALID_PATH"] = True
            self.flags["VALID_PATH"] = False

        return validPath