from util import gmidTestCase
from gmid.factories.strategies.SetStrategies import * 
from gmid.settings import setterInstance

class testSetStrategies(gmidTestCase):
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

    def test_setHeaderExecutre(self):
        setHeader = SetHeadStrat("vov").execute()
        self.assertEqual("vov", setHeader)
        self.assertEqual("vov", setterInstance.header)

class testSetValueStrat(gmidTestCase):
    def __init__(self, args):
        super().__init__(args)
        self.tag = ""

    def test_setValueStrat(self):
        strat = SetValueStrat("10")
        self.assertEqual(10, strat.value)

        strat = SetValueStrat("ABC")
        self.assertEqual(10, strat.value)

        strat = SetValueStrat(10)
        self.assertEqual(10, strat.value)
        
    def test_executeValueStrat(self):
        strat = SetValueStrat(10)
        value = strat.execute()
        self.assertEqual(value, setterInstance.value)