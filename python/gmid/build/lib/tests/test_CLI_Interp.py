from util import gmidTestCase

from gmid.commands.interp import main as interpMain
from gmid.commands.setter import main as setterMain
from gmid.settings import setterInstance
from gmid.utils.SI import SI


class testCLIInterp(gmidTestCase):
    def testInterpDefaultInRange(self):
        self.cli.invoke(setterMain, ["1.0"])
        executed = self.cli.invoke(interpMain, ["vov"])
        self.assertEqual("For 'gmid' = 1.0:\n\n\t'vov' = 2.0\n", executed.output)
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value)

    def testInterpDefaultAll(self):
        self.cli.invoke(setterMain, ["1.0"])
        executed = self.cli.invoke(interpMain, ["all"])
        self.assertEqual(
            "For 'gmid' = 1.0:\n\n\t'vov' = 2.0, 'jd' = 3.0\n", executed.output
        )
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value)

    def testInterpAnotherInRange(self):
        self.cli.invoke(setterMain, ["10.0", "-h", "vov"])
        executed = self.cli.invoke(interpMain, ["gmid"])
        self.assertEqual("For 'vov' = 10.0:\n\n\t'gmid' = 9.0\n", executed.output)
        self.assertEqual("vov", setterInstance.header)
        self.assertEqual(SI("10.0"), setterInstance.value)

    def testInterpAnotherAll(self):
        self.cli.invoke(setterMain, ["10.0", "-h", "vov"])
        executed = self.cli.invoke(interpMain, ["all"])
        self.assertEqual(
            "For 'vov' = 10.0:\n\n\t'gmid' = 9.0, 'jd' = 11.0\n", executed.output
        )
        self.assertEqual("vov", setterInstance.header)
        self.assertEqual(SI("10.0"), setterInstance.value)

    def testInterpNotAllManual(self):
        self.cli.invoke(setterMain, ["1.0"])
        executed = self.cli.invoke(interpMain, ["jd", "-h", "vov"])
        self.assertEqual(
            "For 'gmid' = 1.0:\n\n\t'vov' = 2.0, 'jd' = 3.0\n", executed.output
        )
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1"), setterInstance.value)

    def testInterpNotAllOneInvalid(self):
        self.cli.invoke(setterMain, ["1.0"])
        executed = self.cli.invoke(interpMain, ["hello", "-h", "vov"])
        self.assertEqual(
            "'hello' is not a selectable header. Please use 'gmid view' to see selectable headers.\n",
            executed.output,
        )

    def testInterpNotAllInvalid(self):
        self.cli.invoke(setterMain, ["1.0"])
        executed = self.cli.invoke(interpMain, ["hello", "-h", "blob"])
        self.assertEqual(
            "'hello' is not a selectable header. Please use 'gmid view' to see selectable headers.\n",
            executed.output,
        )

    def testInterpEmpty(self):
        executed = self.cli.invoke(interpMain, [])
        self.assertEqual(
            "Usage: interp [OPTIONS] HEADER\nTry 'interp --help' for help.\n\nError: Missing argument 'HEADER'.\n",
            executed.output,
        )

    """Deprecated    
    def testInterpDefaultNotInRange(self):
        self.cli.invoke(setterMain, ["1.0M"])
        executed = self.cli.invoke(interpMain, ["vov"])
        self.assertEqual(
            "For gmid = 1.0M:\n\nvov = 17.0\nWARNING: The set value used for interpolation was out of range. The resulting interpolated value MAY not be accurate.\n",
            executed.output,
        )
        self.assertEqual("gmid", setterInstance.header)
        self.assertEqual(SI("1.0M"), setterInstance.value)
        """
