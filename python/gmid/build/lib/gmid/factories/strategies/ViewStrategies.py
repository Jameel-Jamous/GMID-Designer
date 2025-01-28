from gmid.factories.strategies.OptionStrategy import OptionStrategy
from gmid.settings import setterInstance

# TODO: See View.py


class ViewHeadStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.header = ""

    def execute(self):
        self.header = setterInstance.header
        return

    def print(self):
        return f"Using Header: {self.header}\n"


class ViewAllHeadersStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.headers = []

    def execute(self):
        if setterInstance.df is not None:
            self.headers = setterInstance.df.columns
        else:
            self.headers = [""]
        return

    def print(self):
        return f"Selectable Headers: {', '.join(item for item in self.headers)}\n"


class ViewValueStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.value = None

    def execute(self):
        self.value = setterInstance.value
        return

    def print(self):
        return f"Using Value: {self.value}\n"


class ViewPathStrat(OptionStrategy):
    def __init__(self, params):
        super().__init__()
        self.paths = {}

    def execute(self):
        for key, path in setterInstance.paths.items():
            if not path.exists():
                self.paths[key + " (Does Not Exist)"] = path
            elif path.as_posix() == ".":
                self.paths[key + " (Not Set)"] = path
            else:
                self.paths[key] = path
        return

    def print(self):
        maxKeyWidth = max(len(str(key)) for key in self.paths.keys())
        output = "Using Paths:\n"
        for key, path in self.paths.items():
            output += f"\t{key:<{maxKeyWidth}} : {str(path)}\n"
        return output
