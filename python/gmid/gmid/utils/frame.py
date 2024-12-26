import pandas as pd
import pickle as pk

class DataManager():
    def __init__(self, aPath, theStatus):
        self.path = aPath
        self.status = theStatus

        