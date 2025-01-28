import json
import math
import re
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from gmid.interpolator import Interpolator as interp
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

    def __init__(self, x_col, y_col, cfg, ax, ylim=None, xlim=None):
        self.__reset__()
        self.x_col = x_col
        self.y_col = y_col
        self.cfg = cfg
        self.ylim = ylim
        self.xlim = xlim
        self.ax = ax
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
        #print(xPos, yPos)
        #print(self.dx(), self.dy())
        self.ax.axvline(
            x=xData,
            ymin=0,
            ymax=1,
            color=self.cfg["lineColor"],
            linestyle=self.cfg["lineStyle"],
            linewidth=self.cfg["lineWidth"],
            marker="None",
        )
        self.ax.axhline(
            y=yData,
            xmin=0,
            xmax=1,
            color=self.cfg["lineColor"],
            linestyle=self.cfg["lineStyle"],
            linewidth=self.cfg["lineWidth"],
            marker="None",
        )

        self.ax.text(
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
        # CompuFe Areas
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
        #print(f"{bestQuad} : {yData}")
        return bestQuad

    def computeAdjustments(self, x, y):
        x = self.dx() * self.cfg["xSpace"]
        y = self.dy() * self.cfg["ySpace"]
        return x, y

    def getPos(self, xData, yData):
        xAdj, yAdj = self.computeAdjustments(xData, yData)
        #print(xAdj, yAdj)
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


class Plotter:
    def __init__(self, xHeader=None, yHeader=None, **kwargs):
        self.x_header = xHeader
        self.y_headers = []
        self.options = dict(kwargs)
        self.flags = {}

        if setterInstance.paths["Config"]:
            self.__loadConfig__(setterInstance.paths["Config"])
        else:
            self.flags["Config"] = False

        self._numOfPlots_ = 0
        self._pltTup_ = ()

    def __process__(self, someOptions):
        return someOptions

    def __loadConfig__(self, aPath):
        with open(aPath, "r") as file:
            self.cfg = json.load(file)
        self.plParams = self.cfg["plotParameters"]
        self.fgParams = self.cfg["figureParameters"]
        self.anParams = self.cfg["annotationParameters"]
        self.__establishParams__()
        self.flags["Config"] = True

    def __establishParams__(self):
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

    @property
    def numOfPlots(self):
        return self._numOfPlots_

    @numOfPlots.setter
    def numOfPlots(self, num):
        self._numOfPlots_ = num

    @property
    def xHeader(self):
        return self.x_header

    @xHeader.setter
    def xHeader(self, aHeader: str):
        if aHeader == "gmid":
            self.x_header = "gmOverID"
        elif aHeader is None or aHeader not in setterInstance.df.columns:
            self.x_header = aHeader
        elif aHeader == "all":
            self.flags["all"] = True
            self.x_header = aHeader
        else:
            self.x_header = aHeader

    @property
    def yHeaders(self):
        return self.y_headers

    @yHeaders.setter
    def yHeaders(self, someHdr):
        if all(hdrs in someHdr for hdrs in setterInstance.df.columns):
            self.y_headers = someHdr
        else:
            self.y_headers = []

    def append(self, aHeader):
        if aHeader == "gmid":
            self.flags["yHeader"] = True
            self.y_headers.append("gmOverID")
        elif aHeader is None or aHeader not in setterInstance.df.columns:
            self.flags.update({"yHeader": False})
        else:
            self.flags["yHeader"] = True
            self.y_headers.append(aHeader)

    @property
    def xData(self):
        return self.x_col

    @xData.setter
    def xData(self, theData: []):
        self.x_col = theData

    @property
    def yData(self):
        return self.x_col

    @yData.setter
    def yData(self, theData: []):
        self.y_col = theData

    def __saveAs__(self, filename, format):
        plt.savefig(filename.with_suffix(f".{format}"), format=f"{format}")
        print(f"Plot saved as: {filename}.{format}")

    def formatTo(self, format: str):
        if "figures" in self.options:
            for yHdr in self.y_headers:
                filename = setterInstance.paths["Output"] / Path(
                    f"{yHdr}VS{self.x_header}"
                )
                self.__saveAs__(filename, format)
        else:
            filename = setterInstance.paths["Output"] / Path("Output")
            self.__saveAs__(filename, format)
        print("Done.")

        return self

    def zoom(self, ax, xMin: float, xMax: float):
        prevMin, prevMax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        per = float((xMax - xMin) / (prevMax - prevMin))
        newX = (xMin, xMax)
        newY = (per * ymin, per * ymax)
        #print(f"precentage : {per}")
        return [newX, newY]

    def annotate(self, ax, yHdr):
        Annotater(
            x_col=setterInstance.df[self.x_header],
            y_col=setterInstance.df[yHdr],
            cfg=self.anParams,
            ax=ax,
        ).setLims(
            xlim=ax.get_xlim(),
            ylim=ax.get_ylim(),
        ).annotate(
            xData=setterInstance.value.equate(),
            yData=interp(xHeader=self.x_header, yHeader=yHdr).execute(),
        )
        return self

    def increment(self):
        self._numOfPlots_ += 1

    def _computeLayout_(self):
        if "figures" not in self.options and self.numOfPlots > 1:
            # Fix to two plots per row and n cols
            ncols = 2
            nrows = math.ceil((self.numOfPlots / ncols))
        else:
            nrows = 1
            ncols = 1

        return int(nrows), int(ncols)

    def _plotting_(self, ax, yHdr):
        ax.plot(
            setterInstance.df[self.x_header],
            setterInstance.df[yHdr],
            color=self.plParams["lineColor"],
        )

        if "zoom" in self.options:
            newLim = self.zoom(ax, self.options["zoom"][0], self.options["zoom"][1])
            ax.set_xlim(newLim[0][0], newLim[0][1], auto=True)
            ax.set_ylim(newLim[1][0], newLim[1][1], auto=True)

        if "annotate" in self.options:
            self.annotate(ax, yHdr)

        if self.plParams["useTex"]:
            if self.x_header == "gmid":
                temp = "gmOverID"
            else:
                temp = self.x_header

            if yHdr == "gmid":
                temp2 = "gmOverID"
            else:
                temp2 = yHdr

            ax.set_xlabel(f"{self.formatHeader(temp)}")
            ax.set_ylabel(f"{self.formatHeader(temp2)}")
        else:
            ax.set_xlabel(f"{self.x_header}")
            ax.set_ylabel(f"{yHdr}")

    def plot(self):
        if "figures" in self.options:
            for yHdr in self.y_headers:
                fig = plt.figure(
                    figsize=(self.fgParams["figSizeX"], self.fgParams["figSizeY"]),
                    dpi=self.fgParams["DPI"],
                    layout=self.fgParams["layoutEngine"],
                )
                ax = plt.gca()
                self._plotting_(ax, yHdr)
        else:
            fig = plt.figure(
                figsize=(self.fgParams["figSizeX"], self.fgParams["figSizeY"]),
                dpi=float(self.fgParams["DPI"]),
                layout=self.fgParams["layoutEngine"],
            )
            nrows, ncols = self._computeLayout_()
            for idx, yHdr in enumerate(self.y_headers):
                if idx == self.numOfPlots - 1 and self.numOfPlots % 2 == 1:
                    ax = fig.add_subplot(nrows, ncols, (idx + 1, idx + 2))
                else:
                    ax = fig.add_subplot(nrows, ncols, idx + 1)
                self._plotting_(ax, yHdr)

        return self

    def show(self):
        print(f"Displaying '{self.y_headers}' vs. '{self.x_header}'")
        print("Close (Ctrl-C) the window to proceed.")
        if "output_as" in self.options:
            self.formatTo(self.options["output_as"])
        else:
            plt.show()

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


plotterInstance = Plotter()
