add_test([=[MathTest.AddPositiveNumbers]=]  /home/jam/Desktop/GMID-Designer/cpp/build/bin/test_math [==[--gtest_filter=MathTest.AddPositiveNumbers]==] --gtest_also_run_disabled_tests)
set_tests_properties([=[MathTest.AddPositiveNumbers]=]  PROPERTIES WORKING_DIRECTORY /home/jam/Desktop/GMID-Designer/cpp/build/tests SKIP_REGULAR_EXPRESSION [==[\[  SKIPPED \]]==])
set(  test_math_TESTS MathTest.AddPositiveNumbers)
