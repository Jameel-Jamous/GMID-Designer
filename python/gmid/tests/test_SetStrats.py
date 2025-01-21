from util import gmidTestCase
from gmid.factories.strategies.SetStrategies import * 
from gmid.settings import setterInstance
from gmid.utils.SI import SI

class testSetHeaderStrategies(gmidTestCase):
    def __init__(self, args):
        super().__init__(args)
        self.tag = ""

    def test_setHeadStrat(self):
        strat = SetHeadStrat("jd")
        self.assertEqual("jd", strat.header,
                         self.tag + 
                         "failed to initialize HeadStrat against non-empty arg")

        strat2 = SetHeadStrat("")
        self.assertEqual("", strat2.header,
                         self.tag + 
                         "failed to initialize empty HeadStrat against empty string arg")

        strat3 = SetHeadStrat(None)
        self.assertEqual(None , strat3.header,
                         self.tag + 
                         "failed to initialize empty HeadStrat against empty None Arg")

    def test_setHeaderExecute(self):
        setHeader = SetHeadStrat("vov").execute()
        self.assertEqual("vov", setHeader)
        self.assertEqual("vov", setterInstance.header)

class testSetValueStrat(gmidTestCase):
    def __init__(self, args):
        super().__init__(args)
        self.tag = ""

    def test_setValueStratFromString(self):
        strat = SetValueStrat("10")
        self.assertEqual(SI, type(strat.value))
        self.assertEqual(10, strat.value.equated)
         
    def test_setValueStratInvalid(self):
        strat = SetValueStrat("ABC")
        self.assertEqual(SI, type(strat.value))
        self.assertEqual(None, strat.value.equated)

    def test_setValueStratFromFloat(self):
        strat = SetValueStrat(10)
        self.assertEqual(SI, type(strat.value))
        self.assertEqual(10, strat.value.equated)
        
    def test_executeValueStrat(self):
        strat = SetValueStrat(10e3)
        value = strat.execute()
        self.assertEqual(value, setterInstance.value)
        self.assertEqual(10e3, value.equated)