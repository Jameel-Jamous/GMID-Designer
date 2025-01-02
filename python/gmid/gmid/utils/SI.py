supported_si = {
    'P' : 15,
    'T' : 12,
    'G' : 9,
    'M' : 6,
    'k' : 3,
    '_' : 0,
    'm' : -3,
    'u' : -6,
    'n' : -9,
    'p' : -12,
    'f' : -15,
}

class SI():
    def __init__(self, str=None, float=None):
        self.__reset__()
        if(str is not None and float is None):
            self.__equated__ = self.fromStr(str)
        elif(str is None and float is not None):
            self.__equated__ = self.fromFloat(float)

        
    def __reset__(self):
        self.__value__ = None
        self.__siUnit__ = '' 
        self.__emptyUnit__ = True
        self.__equated__ = None 
    
    # interface
    @property
    def value(self):
        return self.__value__

    @property 
    def siUnit(self):
        return self.__siUnit__
    
    @property 
    def equated(self):
        return self.__equated__

    ### Overloads 
    # add comaparison
    def __add__(self, other) :
        if(isinstance(other, SI) and not None):
            sum = self.equated() + other.equated()
        return sum 
    
    def __sub__(self, other):
        if(isinstance(other, SI) and not None):
            sum = self.equated() - other.equated()
        return sum
    
    def __mul__(self, other):
        if(isinstance(other, SI) and not None):
            sum = self.equated() * other.equated()
        return sum

    def __truediv__(self, other):
        if(isinstance(other, SI) and not None):
            sum = self.equated() / other.equated()
        return sum
    # add subtractable 
    def __eq__(self, other):
        if(isinstance(other, SI) and not None):
            sum = self.equated() == other.equated()
        return sum
    
    ### helpers
    def fromStr(self, aStr : str):
        valid = self.check(aStr)
        ret = None
        if(valid):
            if(not self.__emptyUnit__):
                self.__siUnit__ = aStr[-1]
                self.__value__ = float(aStr[:-1])
            else:
                self.__siUnit__ = '_'
                self.__value__ = float(aStr)
            ret = self.equate()
        return ret 

    def check(self, aStr : str):
        validUnit = False
        validValue = False
        if(aStr[::-1][0].isalpha()):
            if(not aStr[::-1][1].isalpha()):
                validUnit = True
                self.__emptyUnit__ = False
                if(self.__isfloat__(aStr[:-1])):
                    validValue = True
        elif(aStr[::-1][0].isnumeric()):
            self.__emptyUnit__ = True
            if(self.__isfloat__(aStr)):
                validUnit = False
                validValue = True
        return ((self.__emptyUnit__ or validUnit) and validValue)
    
    def equate(self) -> float:
        return self.__value__ * (10 ** supported_si[self.__siUnit__])

    def fromFloat(self, aFloat : float, __iter__=0): 
        splitFloat = str(aFloat).split('.')
        if(splitFloat[0] > 0):
            temp = aFloat / 1e3
        elif(splitFloat[0] < 0):
            #TODO: Implement THis
            return
        n = __iter__ + 1 
        if(int(str(temp).split('.')[0]) <= 999):
            self.__value__ = temp  
            reverse = {value : key for key, value in supported_si.items()}
            self.__siUnit__ = reverse[n*3] 
            return self.equate()
        else:
            return self.fromFloat(temp, n)

    def toStr(self, e_notation=False):
        if(e_notation):
            theStr = str(self.__value__) + "e" + str(supported_si[self.__siUnit__])
        else:
            theStr = str(self.__value__) + self.__siUnit__
        return theStr 

    def __isfloat__(self, aStr : str):

        ret = False
        try:
            float(aStr)
        except ValueError:
            ret = False
        else:
            ret = True
        return ret

    
    

