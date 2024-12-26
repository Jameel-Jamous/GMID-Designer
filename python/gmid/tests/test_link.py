import unittest
from util import gmidTestCase, common
from gmid.commands.link import main

class testLink():
    # Checks that a 'link' has been established between the CLI and the user data
    def testPathIsSet(self):
        path_that_exists = common["NMOS_DIR"]
        result = self.cli.invoke(main, [path_that_exists])
        self.assertEqual(result.exit_code, 0, "testLink.testPathIsSet: " + common["EXIT"])
        self.assertEqual(result.output, True)

   
        