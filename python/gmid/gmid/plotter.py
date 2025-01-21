import json
import re

import matplotlib.pyplot as plt
import numpy as np

from gmid.settings import setterInstance

# TODO: l is used for inductance(H) and length (m). How implement?
supported_units = {
    "g": "S",  # Conductance
    "r": "\Omega",  # Resistance
    "i": "A",  # Current
    "v": "V",  # Volatage
    "c": "F",  # Capacitance
    "L": "H",  # Inductance
    "/": "/",
    "j": "A/m",
    "w": "m",
    "l": "m",
    "1": "1",
}

# TODO: Implement more robust label formattings using this.
# Example v_{gs}-v_{th}
supported_symbols = {  # Deliminter Symbols
    "Plus": "+",
    "Minus": "-",
    "Over": "/",
    "By": "*",
    "Multiply": "*",
    "Times": "*",
    "Delta": "\Delta",
}


class Annotater:
    """Creates Annotation in Optimum Quadrant"""

    def __init__(self, x_col, y_col, cfg, ylim=None, xlim=None):
        self.__reset__()
        self.x_col = x_col
        self.y_col = y_col
        self.cfg = cfg
        self.ylim = ylim
        self.xlim = xlim

        self.prec = self.cfg["precision"]

    def __reset__(self):
        self.pos = ()  # xPos, yPos
        self.prec = 0
        self.usingQuad = 0
        self.x_col = None
        self.y_col = None
        self.cfg = {}  # Annotation configuration
        self.ylim = ()  # min, max
        self.xlim = ()  # min, max
        self.dicts = {
            "Area": {},
            "Length": {},
            "Count": {},
        }

    def dx(self):
        """Returns xmax-xmin"""
        return self.xlim[1] - self.xlim[0]

    def dy(self):
        """Returns ymax - ymin"""
        return self.ylim[1] - self.ylim[0]

    def getAlign(self):
        if self.usingQuad == 1 or self.usingQuad == 4:
            halign = "left"
            valign = "center"
        else:
            halign = "right"
            valign = "center"
        return halign, valign

    def annotate(self, xData: float, yData: float):
        """Adds the annotation to current plt. The main entry point"""
        xPos, yPos = self.getPos(xData, yData)
        halign, valign = self.getAlign()
        print(xPos, yPos)
        print(self.dx(), self.dy())
        plt.axvline(
            x=xData,
            ymin=0,
            ymax=1,
            color=self.cfg["lineColor"],
            linestyle=self.cfg["lineStyle"],
            linewidth=self.cfg["lineWidth"],
            marker="None",
        )
        plt.axhline(
            y=yData,
            xmin=0,
            xmax=1,
            color=self.cfg["lineColor"],
            linestyle=self.cfg["lineStyle"],
            linewidth=self.cfg["lineWidth"],
            marker="None",
        )

        plt.text(
            x=xPos,
            y=yPos,
            s=f"({self.format(xData)},{self.format(yData)})",
            fontsize=self.cfg["fontSize"],
            fontfamily=self.cfg["fontFamily"],
            horizontalalignment=halign,
            verticalalignment=valign,
        )

        return self

    def initDicts(self, xData, xmin, xmax, yData, ymin, ymax):
        """Initializes the decision dicts"""
        # Compute Areas
        areasOfEachQuad = {
            1: abs(xmax - xData) * abs(ymax - yData),
            2: abs(xData - xmin) * abs(ymax - yData),
            3: abs(xData - xmin) * abs(yData - ymin),
            4: abs(xmax - xData) * abs(yData - ymin),
        }
        self.dicts["Area"] = areasOfEachQuad

        # Count Points
        pointsInEachQuad = {
            1: np.sum((self.x_col > xData) & (self.y_col > yData)),
            2: np.sum((self.x_col < xData) & (self.y_col > yData)),
            3: np.sum((self.x_col < xData) & (self.y_col < yData)),
            4: np.sum((self.x_col > xData) & (self.y_col < yData)),
        }
        self.dicts["Count"] = pointsInEachQuad

        # Get Lenghts
        lengthOfEachQuad = {
            1: abs(xmax - xData),
            2: abs(xData - xmin),
            3: abs(xData - xmin),
            4: abs(xmax - xData),
        }
        self.dicts["Length"] = lengthOfEachQuad

        return

    def format(self, data):
        return (
            f"{data:.{self.prec}f}".rstrip("0").rstrip(".")
            if isinstance(data, float)
            else str(data)
        )

    def sortDicts(self, xData, yData):
        self.initDicts(
            xData=xData,
            yData=yData,
            xmin=self.xlim[0],
            ymin=self.ylim[0],
            xmax=self.xlim[1],
            ymax=self.ylim[1],
        )

        # Sort Area by Max
        self.dicts["Area"] = self.sort(self.dicts["Area"], reverse=True)
        largestAreas = [
            list(self.dicts["Area"].keys())[0],
            list(self.dicts["Area"].keys())[1],
        ]

        # Sort Count by Least
        self.dicts["Count"] = self.sort(self.dicts["Count"])
        leastCounts = [
            list(self.dicts["Count"].keys())[0],
            list(self.dicts["Count"].keys())[1],
        ]

        # Sort Length by Max
        self.dicts["Length"] = self.sort(self.dicts["Length"], reverse=True)
        largestLengths = [
            list(self.dicts["Length"].keys())[0],
            list(self.dicts["Length"].keys())[1],
        ]

        # Return a trimed sorted list of all
        return largestAreas, leastCounts, largestLengths

    def sort(self, theDict: {}, reverse=False):
        temp = dict(sorted(theDict.items(), key=lambda item: item[1], reverse=reverse))
        return temp

    def getBestQuad(self, xData, yData):
        largestAreas, leastCounts, largestLengths = self.sortDicts(xData, yData)

        # Compare the LA & LC and LC & LL
        ofLargestAndLeastQuad = set(largestAreas) & set(leastCounts)
        ofLongestAndLeastQuad = set(largestLengths) & set(leastCounts)

        if len(ofLargestAndLeastQuad) != 0 and len(ofLongestAndLeastQuad) != 0:
            # Check which quadrant has the least counted by looking for the smallest index
            ofLargestAndLeastQuad = list(ofLargestAndLeastQuad)[0]
            ofLongestAndLeastQuad = list(ofLongestAndLeastQuad)[0]
            idx0 = leastCounts.index(ofLargestAndLeastQuad)
            idx1 = leastCounts.index(ofLongestAndLeastQuad)
            if idx0 < idx1:
                bestQuad = leastCounts[idx0]
            else:
                bestQuad = leastCounts[idx1]
        elif not ofLargestAndLeastQuad:
            bestQuad = list(ofLongestAndLeastQuad)[0]
        elif not ofLongestAndLeastQuad:
            bestQuad = list(ofLargestAndLeastQuad)[0]

        self.usingQuad = bestQuad
        print(f"{bestQuad} : {yData}")
        return bestQuad

    def computeAdjustments(self, x, y):
        x = self.dx() * self.cfg["xSpace"]
        y = self.dy() * self.cfg["ySpace"]
        return x, y

    def getPos(self, xData, yData):
        xAdj, yAdj = self.computeAdjustments(xData, yData)
        print(xAdj, yAdj)
        mapping = {
            1: (
                xData + xAdj,
                yData + yAdj,
            ),
            2: (
                xData - xAdj,
                yData + yAdj,
            ),
            3: (
                xData - xAdj,
                yData - yAdj,
            ),
            4: (
                xData + xAdj,
                yData - yAdj,
            ),
        }
        return mapping[self.getBestQuad(xData, yData)]

    def setLims(self, xlim, ylim):
        self.ylim = ylim
        self.xlim = xlim
        return self


# TODO: See PlotStratigies.
class Plotter:
    def __init__(self, xHeader, yHeader, **kwargs):
        # Store headers and options that were passed in
        self.x_header = xHeader
        self.y_header = yHeader
        self.opt = dict(kwargs)
        # FIXME: THIS IS A TEMPORARY FIX!
        # To fix: Change ALL instances of 'gmid' to 'gmOverid'
        if xHeader == "gmid":
            self.x_header = "gmOverID"
        if yHeader == "gmid":
            self.y_header = "gmOverID"

        if xHeader != "all":
            # Store the data needed from the df
            self.x_col = setterInstance.df[xHeader]
            self.y_col = setterInstance.df[yHeader]

            # Read the .json file to establish corresponding configs
            with open(setterInstance.paths["Config"], "r") as file:
                self.cfg = json.load(file)
            self.plParams = self.cfg["plotParameters"]
            self.fgParams = self.cfg["figureParameters"]
            self.anParams = self.cfg["annotationParameters"]
            self.establishParams()
            self.pltTup = plt.subplots()

            # Init Annotater
            self.annotater = Annotater(
                x_col=self.x_col,
                y_col=self.y_col,
                cfg=self.anParams,
            )

    def establishParams(self):
        plt.rcParams.update(
            {
                "lines.linewidth": self.plParams["lineWidth"],
                "lines.color": self.plParams["lineColor"],
                "lines.linestyle": self.plParams["lineStyle"],
                "lines.marker": self.plParams["markStyle"],
                "lines.markerfacecolor": self.plParams["markColor"],
                "lines.markersize": self.plParams["markSize"],
                "text.usetex": self.plParams["useTex"],
                "font.family": self.plParams["fontFamily"],
                "font.size": self.plParams["fontSize"],
                "axes.labelsize": self.plParams["labelSize"],
                "xtick.labelsize": self.plParams["tickLabelSize"],
                "ytick.labelsize": self.plParams["tickLabelSize"],
                "figure.autolayout": True,  # Ensuring the figure layout adjusts to content
            }
        )
        return self

    def plot(self):
        self.pltTup[1].plot(
            self.x_col,
            self.y_col,
            color=self.plParams["lineColor"],
        )

        """
        if self.opt["usingLog"][0]:
            if self.opt["usingLog"][1] == "X":
                plt.xscale("log")
            elif self.opt["usingLog"][1] == "Y":
                plt.yscale("log")
        """

        if self.plParams["useTex"]:
            self.pltTup[1].set_xlabel(f"{self.formatHeader(self.x_header)}")
            self.pltTup[1].set_ylabel(f"{self.formatHeader(self.y_header)}")
        else:
            self.pltTup[1].set_xlabel(f"{self.x_header}")
            self.pltTup[1].set_ylabel(f"{self.y_header}")

        return self

    def show(self):
        print(f"Displaying '{self.y_header}' vs. '{self.x_header}'")
        print("Close (Ctrl-C) the window to proceed.")
        #       print(plt.rcParams)
        plt.show()

    def annotate(self, xdata: float, ydata: float):
        self.annotater.setLims(
            xlim=self.pltTup[1].get_xlim(),
            ylim=self.pltTup[1].get_ylim(),
        ).annotate(xData=xdata, yData=ydata)
        return self

    def formatHeader(self, aHeader: str):
        aList = re.findall(r"([a-zA-z]+)Over([a-zA-z]+)", aHeader)
        aList = [item for sublist in aList for item in sublist]
        aList.insert(1, "Over")
        if len(aList) == 1:
            aList = [aHeader]
        units = self.getUnits(aList)
        # Take the first letter and underscore the rest
        outstr = "$"
        for item in aList:
            if item != "Over":
                temp = item[0] + "_{" + item[1:] + "}"
            else:
                temp = "/"
            outstr += temp
        outstr += "$"
        return outstr + units

    def getUnits(self, aList: list):
        temp = []
        outstr = " ["
        for item in aList:
            if item != "Over":
                temp.append(item.lower()[0])
            else:
                temp.append("/")
        for item in temp:
            outstr += supported_units[item]
        outstr += "]"
        return outstr
