from gmid.utils.SI import SI
from gmid.settings import setterInstance
import numpy as np

class Interpolator():
    def __init__(self, yHeader : str, xHeader="gmid"):
        self.reset()
        if(self.validHeader(xHeader)):
            self.x_header = xHeader 
        
        if(self.validHeader(yHeader)):
            self.y_header = yHeader
      
    def reset(self):
        self.x_header = ""
        self.y_header = ""

    def validHeader(self, header):
        return True if header in setterInstance.df.columns.tolist() else False

    def execute(self):
        if(self.y_header == "" or self.x_header == ""):
            ret = None
        else:
            ret = float(np.interp(setterInstance.value.equate(), 
                        setterInstance.df[self.x_header],
                        setterInstance.df[self.y_header]))
        return ret 