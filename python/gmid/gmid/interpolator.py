import numpy as np

from gmid.settings import setterInstance
from gmid.utils.SI import SI


class Interpolator:
    def __init__(self, yHeader: str, xHeader="gmid"):
        self.reset()
        if self.validHeader(xHeader):
            self.x_header = xHeader

        if self.validHeader(yHeader):
            self.y_header = yHeader

    def reset(self):
        self.x_header = ""
        self.y_header = ""
        self.bounds = ()

    def validHeader(self, header):
        return True if header in setterInstance.df.columns.tolist() else False

    def execute(self):
        if self.y_header == "" or self.x_header == "":
            ret = None
        else:
            # Check if xp and fp are increasing
            xp_sort, fp_sort = zip(
                *sorted(
                    zip(
                        setterInstance.df[self.x_header],
                        setterInstance.df[self.y_header],
                    )
                )
            )
            ret = float(
                np.interp(
                    x=setterInstance.value.equate(),
                    xp=xp_sort,
                    fp=fp_sort,
                )
            )
        return ret
