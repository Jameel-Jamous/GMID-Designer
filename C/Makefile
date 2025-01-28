# Compiler settings
CC = gcc
CXX = g++
CFLAGS = -Wall -g
CXXFLAGS = -Wall -g -std=c++11
LDFLAGS = -lCppUTest  # Link to CppUTest

# Directories
SRCDIR = src
INCDIR = include
TESTDIR = tests
CPPINCDIR = /usr/include  # Adjust if necessary based on where CppUTest is installed
CPPLIBDIR = /usr/lib     # Adjust for your system's library path, typically /usr/lib or /usr/lib/x86_64-linux-gnu

# Files
SOURCES = $(SRCDIR)/cli.c
OBJECTS = $(SOURCES:.c=.o)
TESTS = $(TESTDIR)/test_main.cpp $(TESTDIR)/test_fail.cpp
TEST_EXEC = bin/test_main

# Targets
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(TARGET)

tests: $(TEST_EXEC)
	./$(TEST_EXEC)

$(TEST_EXEC): $(TESTS) $(SRCDIR)/cli.c
	$(CXX) $(CXXFLAGS) -I$(CPPINCDIR) $(TESTS) -o $(TEST_EXEC) $(LDFLAGS) -L$(CPPLIBDIR)

clean:
	rm -f $(TARGET) $(OBJECTS) $(TEST_EXEC)
