# C++ Practice

A small C++17 project for practicing input, output, variables, and functions.

## Requirements

Install the VS Code C/C++ extension and an MSYS2 UCRT64 toolchain. In the MSYS2 UCRT64 terminal, run:

```sh
pacman -S --needed make mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb
```

The VS Code build task expects `g++` to be on `PATH`. The debugger configuration expects GDB at `C:/msys64/ucrt64/bin/gdb.exe`.

## Build and run

In the MSYS2 UCRT64 terminal:

```sh
make
./main.exe
```

Or press `Ctrl+Shift+B` to build.

## Debug

Open this folder in VS Code, set a breakpoint in `main.cpp`, and press `F5`. Enter two numbers in the console window when prompted.

The build task currently compiles `main.cpp`. Update `.vscode/tasks.json` when you add more source files.
