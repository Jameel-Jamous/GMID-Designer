# Before we can interpolate we need to have a valid data frame loaded
# into the Setter. We must pull it from the set environment variables
import os
import pickle
import pandas as pd 
from gmid.utils.SI import SI

class Setter():
    def __init__(self):
        self.__reset__()
        self.initPaths()
        self.initDf()
        self._header_ = self.load("Header")
        self._value_ = self.load("Value")
        
    def __reset__(self):
        self.df = None
        self._value_ = None
        self._header_ = ""
        self.prevHead = None
        self.prevValue = None 
        self.paths = {
            "Install" : "",
            "Data" : "",
            "Config" : "",
        }
    
    def initPaths(self):
        paths = os.getenv("GMID_PATHS").split(";")
        self.paths["Install"] = paths[0]
        self.paths["Data"] = paths[1]
        self.paths["Config"] = paths[2]
        return not (self.paths["Install"] == "" and self.paths["Data"] == "" 
                and self.paths["Config"] == "")
    
    def initDf(self):
        ret = True
        if(not self.paths["Data"] == ""):
            try:
                self.df = pd.read_csv(self.paths["Data"])
            except FileNotFoundError:
                ret = False
            except FileExistsError:
                ret = False
        return ret
       
    @property
    def header(self) -> str:
        return self._header_

    @header.setter
    def header(self, aHeader):
        self._header_ = aHeader
        with open(self.paths["Install"] + r"\pkl\header.pkl", 'wb') as file:
            pickle.dump(aHeader, file)

    @property
    def value(self) -> SI:
        return self._value_
    
    @value.setter
    def value(self, aValue):
        with open(self.paths["Install"] + r"\pkl\value.pkl", 'wb') as file:
            pickle.dump(aValue, file)
        self._value_ = aValue
    
    def load(self, what : str):
        temp = None
        if(what == "Header"):
            with open(self.paths["Install"] + r"\pkl\header.pkl", 'rb') as file:
                temp = pickle.load(file)
        elif(what == "Value"):
           with open(self.paths["Install"] + r"\pkl\value.pkl", 'rb') as file:
                temp = pickle.load(file) 
        return temp 
            
setterInstance = Setter()