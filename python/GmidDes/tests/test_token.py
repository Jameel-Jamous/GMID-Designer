import unittest.test
from src.token import *
import unittest
import io
import sys

sys.path.append('../src/')

#class TestToken(unittest.TestCase):
   #def testInit(self):
import code

def simple_repl():
    print("Welcome to your custom Python REPL!")
    print("Type 'exit' to quit.")
    while True:
        try:
            # Read input from the user
            user_input = input(">>> ")
            
            # Exit the REPL loop
            if user_input.lower() in {'exit', 'quit'}:
                print("Exiting REPL. Goodbye!")
                break
            
            # Evaluate the input as Python code
            result = eval(user_input)
            
            # Print the result
            if result is not None:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

# Run the REPL shell
simple_repl()
        