import unittest
from click.testing import CliRunner

class gmidTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cli = CliRunner()
        self.tag = ""

common = {
    "NOIMP" : "Test Not Yet Implemented",
    "EXIT" : "Exitted with error_code: ",
}