supported_si = {
    "P": 15,
    "T": 12,
    "G": 9,
    "M": 6,
    "k": 3,
    "": 0,
    "m": -3,
    "u": -6,
    "n": -9,
    "p": -12,
    "f": -15,
}


class SI:
    """A Class to represent floatint point numbers as
    a number using SI notation"""

    def __init__(self, str=None, float=None):
        self.__reset__()
        if str is not None and float is None:
            self.fromStr(str)
        elif str is None and float is not None:
            self.fromFloat(float)

        if self.__value__ is not None and self.__siUnit__ is not None:
            self.__equated__ = self.equate()

    def __reset__(self):
        self.__value__ = None
        self.__siUnit__ = ""
        self.__emptyUnit__ = True
        self.__equated__ = None

    def __isfloat__(self, aStr: str):

        ret = False
        try:
            float(aStr)
        except ValueError:
            ret = False
        else:
            ret = True
        return ret

    ### Interface
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
    def __add__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ + other.__equated__
        return sum

    def __sub__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ - other.__equated__
        return sum

    def __mul__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ * other.__equated__
        return sum

    def __truediv__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ / other.__equated__
        return sum

    def __eq__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ == other.__equated__
        elif isinstance(other, float) and not None:
            sum = self.__equate__ == other
        else:
            sum = None
        return sum

    def __gt__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ > other.__equated__
        elif (isinstance(other, float) or isinstance(other, int)) and not None:
            sum = self.__equated__ > other
        else:
            sum = None
        return sum

    def __lt__(self, other):
        if isinstance(other, SI) and not None:
            sum = self.__equated__ < other.__equated__
        elif (isinstance(other, float) or isinstance(other, int)) and not None:
            sum = self.__equated__ < other
        else:
            sum = None
        return sum

    def __ge__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __str__(self):
        return self.toStr()

    ### Helpers
    def fromStr(self, aStr: str):
        valid = self.check(aStr)
        ret = None
        if valid:
            if not self.__emptyUnit__:
                self.__siUnit__ = aStr[-1]
                self.__value__ = float(aStr[:-1])
            else:
                self.__siUnit__ = ""
                self.__value__ = float(aStr)

            if abs(self.__value__) > 999 or abs(self.__value__) < 1:
                ret = self.fromFloat(self.__value__)
            else:
                ret = (self.__value__, self.__siUnit__)
        return ret

    def fromFloat(self, aFloat: float, __iter__=0):
        if abs(aFloat) > 999:
            return self.fromFloat(aFloat / 1e3, __iter__ + 3)
        elif abs(aFloat) < 1 and abs(aFloat) > 0:
            return self.fromFloat(aFloat * 1e3, __iter__ - 3)
        else:
            self.__value__ = round(aFloat, 10)
            reverse = {value: key for key, value in supported_si.items()}
            self.__siUnit__ = reverse[__iter__]
            return (self.__value__, self.__siUnit__)

    def toStr(self, e_notation=False):
        if e_notation:
            theStr = str(self.__value__) + "e" + str(supported_si[self.__siUnit__])
        else:
            theStr = str(self.__value__) + self.__siUnit__
        return theStr

    def check(self, aStr: str):
        validUnit = False
        validValue = False
        # Check if there is a unit
        if aStr[::-1][0].isalpha():
            # Check if there is a supported si unit
            if not aStr[::-1][1].isalpha():
                validUnit = True
                self.__emptyUnit__ = False
                if self.__isfloat__(aStr[:-1]):
                    validValue = True
        # Check if there is no unit
        elif aStr[::-1][0].isnumeric():
            self.__emptyUnit__ = True
            if self.__isfloat__(aStr):
                validUnit = False
                validValue = True
        return (self.__emptyUnit__ or validUnit) and validValue

    def equate(self) -> float:
        return self.__value__ * (10 ** supported_si[self.__siUnit__])

