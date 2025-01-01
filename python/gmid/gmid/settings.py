
class Setter():
    def __init__(self):
        self.__reset__()

    def __reset__(self):
        self.df = None
        self.value = None
        self.header = ""
        
setterInstance = Setter()