import unittest
from util import gmidTestCase
from gmid.commands.hello import main 

class testHello(gmidTestCase):
    def test_hello(self):
        result = self.cli.invoke(main)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Hello World", result.output)
    
if __name__ == "__main__":
    unittest.main()