import pandas as pd
import os
import click
import pickle
from gmid.utils.singleton import singleton
from functools import wraps

@singleton
class DFManager():
    def __init__(self):
        self.__reset__()
    
    def __reset__(self):
        self._instance = None
        self.flags = {
            "VALID_FILE" : False,
            "EMPTY_FILE" : False,
            "INVALID_FILE" : False,
        }
        self.df = None
        self.headers = ['vov', 'gmid'] 


    def openDF(self):
        return 
    
    def dynamicAddOptions(self, func, hasArgs=True):
        if(self.headers != []):
            for name in self.headers:
                def decorator(f):
                    @click.option(f'--{name}', type=float if hasArgs else None, help=f'Header for \'{name}\' data')
                    @wraps(f)
                    def wrapper(*args, **kwargs):
                        return f(*args, **kwargs)
                    return wrapper
                func = decorator(func)
            return func

"""    def setPath(self, aPath):
        isValidPath = self.__checkValidPath__(aPath)
        
        if(isValidPath):
            self.flags["VALID_PATH"] = True
            self.flags["INVALID_PATH"] = False

            fileType = self.__checkValidCSV__(aPath)
            self.__setFileFlags__(fileType)
            if(self.flags["VALID_FILE"] or self.flags["EMPTY_FILE"]):
                self.path = aPath
        else:
            self.flags["VALID_PATH"] = False
            self.flags["INVALID_PATH"] = True

        return (isValidPath and (self.flags["VALID_FILE"] or self.flags["EMPTY_FILE"]))

    def __setFileFlags__(self, type):
        if(type == "EMPTY_FILE"):
            self.flags["VALID_FILE"] = False
            self.flags["INVALID_FILE"] = False
            self.flags["EMPTY_FILE"] = True
        elif(type == "INVALID_FILE"):
            self.flags["VALID_FILE"] = False
            self.flags["INVALID_FILE"] = True
            self.flags["EMPTY_FILE"] = False
        elif(type == "VALID_FILE"):
            self.flags["VALID_FILE"] = True
            self.flags["INVALID_FILE"] = False
            self.flags["EMPTY_FILE"] = False
        else:
            self.flags["VALID_FILE"] = False
            self.flags["INVALID_FILE"] = False
            self.flags["EMPTY_FILE"] = False

    def picklePath(self):
        # Save pickled data path to install path
        install_path = self.__getInstallPath__()
        with open((install_path + r"\pkl\data.pkl"), "wb") as file:
            pickle.dump(self.path, file)
            file.close()
    
    def pickleSelf(self):
        return 
   
    def __getInstallPath__(self):
        return os.getenv("GMIDDesigner_Path")

    def __getHeaderLine__(self, thePath):
        header_line = ""
        # Assuming the file is already valid and not empty
        with open(thePath, 'r', encoding="utf-8-sig") as file:
                header_line = file.readline().strip()
                file.close()
        return header_line

    def __checkValidCSV__(self, thePath : str):
        ret = ""
        isValidPath = self.__checkValidPath__(thePath)

        if(isValidPath):
            isEmpty = (os.path.getsize(thePath) == 0)
            if(isEmpty):
                ret = "EMPTY_FILE"
            else:
                hdr = self.__getHeaderLine__(thePath)
                if(hdr.split(",")[0] == "vov"):
                    ret = "VALID_FILE"    
                else:
                    ret = "INVALID_FILE"
        else:
            ret = "INVALID_PATH"

        return ret
    
    def __checkValidPath__(self, thePath : str):
        return os.path.exists(thePath) and thePath.endswith(".csv")
"""
    