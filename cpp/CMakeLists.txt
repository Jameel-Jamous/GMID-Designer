cmake_minimum_required(VERSION 3.16)
project(MyProject)

enable_testing()
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(src)
add_subdirectory(tests)

include(GNUInstallDirs)
