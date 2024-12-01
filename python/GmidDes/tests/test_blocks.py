import unittest
import io
import sys
from src.blocks import Option, Menu

sys.path.append('../src/')

class TestOption(unittest.TestCase):
    def test_init(self):
        def anAction():
            return "This is a test function"
        
        anOption = Option("Test Option", anAction)
        self.assertEqual(anOption.name, "Test Option", "Option: names not initialized correctly")
        self.assertEqual(anOption.actionCB, anAction, "Option: action callback not initialzed correctly")

    def test_execute(self):
        def anAction():
            return "This is a test function"

        anOption = Option("Test Option", anAction)
        ret = anOption.execute()
        self.assertEqual(ret, "This is a test function", "Option: function not executed correctly")
    
    def test_execute_w_side_effects(self):
        results_list = []

        def anAction():
            results_list.append("This action appends a list")

        option = Option("Test Option", anAction)
        option.execute()
        
        self.assertEqual(results_list, ["This action appends a list"], "Option: execute did not produce the expected side effect")

class TestMenu(unittest.TestCase):
    def test_init(self):
        aMenu = Menu("Main Menu")
        self.assertEqual(aMenu.title, "Main Menu", "Menu: title not initialized correctly")
        self.assertEqual(aMenu.options, {}, "Menu: option dictionary not initialized correctly")
    
    def test_add_option(self):
        aMenu = Menu("Main Menu")

        def optionOne():
            return "This is option 1"
        
        option_1 = Option("Option1", optionOne)
        aMenu.add_option("A", option_1) 
        
        self.assertEqual(aMenu.options["A"], option_1, "Menu: options not stored correctly")

    def test_display(self):
        aMenu = Menu("Main Menu")

        def optionOne():
            return "This is option 1"
        
        option_1 = Option("Option1", optionOne)
        aMenu.add_option("A", option_1) 

        def optionTwo():
            return "This is option 2"
        
        option_2 = Option("Option2", optionTwo)
        aMenu.add_option("B", option_2) 

        # Rewrite Output Buffer
        out = io.StringIO()
        sys.stdout = out
        aMenu.display()
        captured = out.getvalue()
        out.flush
        print("\nMain Menu")
        print("A. Option1")
        print("B. Option2")
        captured2 = out.getvalue()
        sys.stdout = sys.__stdout__
        self.assertIn(captured, captured2, "Menu: display is missing options")
    
    def test_execute(self): 
        aMenu = Menu("Main Menu")

        def optionOne():
            return "This is option 1"
        
        option_1 = Option("Option1", optionOne)
        aMenu.add_option("A", option_1) 

        def optionTwo():
            return "This is option 2"
        
        option_2 = Option("Option2", optionTwo)
        aMenu.add_option("B", option_2) 
        
        resultA = aMenu.execute("A")
        resultB = aMenu.execute("B")   
        resultC = aMenu.execute("C")
        self.assertEqual(resultA, "This is option 1", "Menu: Selected option not executable")
        self.assertEqual(resultB, "This is option 2", "Menu: Selected option not executable") 
        self.assertIsNone(resultC, "Menu: Executed an option that was not instanced")

if __name__ == '__main__':
    unittest.main()