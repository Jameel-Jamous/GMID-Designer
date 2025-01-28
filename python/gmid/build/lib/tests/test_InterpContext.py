from util import gmidTestCase

from gmid.contexts.InterpOptionContext import InterpOptionContext
from gmid.factories.strategies.InterpStrategies import (
    InterpHeaderStrat,
    InterpHeadStrat,
)
from gmid.settings import setterInstance
from gmid.utils.SI import SI


class testInterpHeaderStrategies(gmidTestCase):
    def testOutputHoldingCorrectly(self):
        ctxt = InterpOptionContext(None, {})
        ctxt.options = {"header": "vov"}
        ctxt.toStrategy()
        self.assertIsNotNone(ctxt.strategies)
        ctxt.execute()
        self.assertEqual(ctxt.output, [{"vov": 2.0}])

        ctxt.output = []
        ctxt.strategies = []
        ctxt.options = {"head": ("vov", "jd")}
        ctxt.toStrategy()
        self.assertIsNotNone(ctxt.strategies)
        ctxt.execute()
        self.assertEqual(ctxt.output, [{"jd": 3.0, "vov": 2.0}])

        ctxt.output = []
        ctxt.strategies = []
        ctxt.options = {"head": ("vov", "jd"), "header": "gmid"}
        ctxt.toStrategy()
        self.assertIsNotNone(ctxt.strategies)
        ctxt.execute()
        self.assertEqual(ctxt.output, [{"jd": 3.0, "vov": 2.0}, {"gmid": 1.0}])

    def testPrint(self):
        ctxt = InterpOptionContext(None, {})
        ctxt.options = {"head": ("vov", "jd"), "header": "gmid"}
        ctxt.toStrategy()
        self.assertIsNotNone(ctxt.strategies)
        ctxt.execute()
        self.assertEqual(ctxt.output, [{"jd": 3.0, "vov": 2.0}, {"gmid": 1.0}])
        outtputted = ctxt.print()
        self.assertEqual(
            outtputted, "For 'vov' = 2.0:\n\n\t'gmid' = 1.0, 'vov' = 2.0, 'jd' = 3.0"
        )

        ctxt.output = []
        ctxt.strategies = []
        ctxt.options = {"head": ("blob", "jd"), "header": "gmid"}
        ctxt.toStrategy()
        self.assertIsNotNone(ctxt.strategies)
        ctxt.execute()
        self.assertEqual(ctxt.output, [{"Invalid": "blob", "jd": 3.0}, {"gmid": 1.0}])
        outtputted = ctxt.print()
        self.assertEqual(
            outtputted,
            "'blob' is not a selectable header. Please use 'gmid view' to see selectable headers.",
        )
