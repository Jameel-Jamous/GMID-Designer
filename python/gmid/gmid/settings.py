import os
import pickle
from pathlib import Path

import pandas as pd

from gmid.utils.SI import SI

# TODO: Currently when a path is not available, python exceptions
# are thrown meaning incomprehesive error messages. Make sure the
# code doesnt break when a path is not set.


# TODO: Consider adding another method that checks whether or not
# a valid config file is set and being used.
class Setter:
    def __init__(self):
        self.__reset__()
        self.hasValidPath = self.initPaths()
        self.hasValidDF = self.initDf()

        try:
            self._header_ = self.load("Header")
        except EOFError:
            self.header = "gmid"
        try:
            self._value_ = self.load("Value")
        except EOFError:
            self.value = None
        # self.valueFlag = self.getValueFlags(self._value_)

    def __reset__(self):
        self.df = None
        self._value_ = None
        self._header_ = ""
        self.prevHead = None
        self.prevValue = None
        self.paths = {
            "Install": "",
            "Data": "",
            "Config": "",
        }
        self.hasValidDF = False
        self.hasValidDF = False
        self.valueFlag = []

    def initPaths(self):
        if os.name == "posix":
            delim = ":"
        else:
            delim = ";"
        paths = os.getenv("GMID_PATHS")
        if paths is None:
            raise FileNotFoundError
        else:
            paths = paths.split(delim)
            self.paths["Install"] = Path(paths[0])
            self.paths["Data"] = Path(paths[1])
            self.paths["Config"] = Path(paths[2])
        # NOTE: Regarding the TOP TODO, this might be a potential
        # area looking into
        return not (
            self.paths["Install"] == ""
            and self.paths["Data"] == ""
            and self.paths["Config"] == ""
        )

    def initDf(self):
        ret = True
        if not self.paths["Data"] == "":
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
        if aHeader in self.df.columns:
            with open(self.paths["Install"] / "pkl" / "header.pkl", "wb") as file:
                pickle.dump(aHeader, file)

    @property
    def value(self) -> SI:
        return self._value_

    @value.setter
    def value(self, aValue):
        with open(self.paths["Install"] / "pkl" / "value.pkl", "wb") as file:
            pickle.dump(aValue, file)
        self._value_ = aValue
        self.valueFlag = []
        self.valueFlag = self.getValueFlags(aValue)

    def load(self, what: str):
        temp = None
        if what == "Header":
            with open(self.paths["Install"] / "pkl" / "header.pkl", "rb") as file:
                temp = pickle.load(file)
        elif what == "Value":
            with open(self.paths["Install"] / "pkl" / "value.pkl", "rb") as file:
                temp = pickle.load(file)
        return temp

    def getValueFlags(self, value):
        ret = []
        if not self.valueInBounds(value):
            ret.append("OutOfBounds")
        return ret

    def valueInBounds(self, value):
        ret = False
        if self.hasValidDF and self._header_:
            bounds = (self.df[self._header_].iloc[0], self.df[self._header_].iloc[-1])
            ret = value > bounds[0] and value < bounds[1]
        return ret


setterInstance = Setter()
