include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.12.1.zip)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(test_math test_math.cpp)
target_include_directories(test_math PRIVATE ${PROJECT_SOURCE_DIR}/src)
target_link_libraries(test_math PRIVATE gtest_main mymath)

include(GoogleTest)
gtest_discover_tests(test_math)
