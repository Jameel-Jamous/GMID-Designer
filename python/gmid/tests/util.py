import unittest
from click.testing import CliRunner

class gmidTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cli = CliRunner()

common = {
    "NMOS_DIR" : r"C:\Users\Jameel\Desktop\GMIDDesigner\python\sample_data\test\nmos",
    "PMOS_DIR" : "../../sampple_data/test/pmos",
    "NOIMP" : "Test Not Yet Implemented",
    "EXIT" : "Exitted with error_code: ",
}