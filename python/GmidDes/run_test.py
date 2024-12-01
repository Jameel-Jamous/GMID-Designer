import unittest

# Discover all tests in the "tests" directory
def run_all_tests():
    # The start directory is where your tests are located, here we assume they are in the "tests" folder
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover('tests')  # Discover all tests in the "tests" folder
    
    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

if __name__ == "__main__":
    run_all_tests()
