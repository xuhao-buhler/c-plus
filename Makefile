CXXFLAGS ?= -std=c++17 -Wall -Wextra -g

.PHONY: all
all: main.exe

main.exe: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@