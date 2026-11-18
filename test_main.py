import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def executable(tmp_path_factory):
    project_dir = Path(__file__).parent
    executable = tmp_path_factory.mktemp("build") / "main.exe"

    print("Compiling main.cpp...")
    subprocess.run(
        ["g++", "-std=c++17", str(project_dir / "main.cpp"), "-o", str(executable)],
        check=True,
    )
    print("Compilation completed.")

    return executable


def test_selects_addition(executable):
    print("Testing addition (choice 0)...")
    result = subprocess.run(
        [str(executable)],
        input="0\n2 3\n",
        text=True,
        capture_output=True,
        check=False,
    )
    print(result.stdout, end="")

    assert result.returncode == 0
    assert result.stdout == (
        "Choose operation (0 for addition, 1 for subtraction): "
        "Enter two numbers: Their sum is 5\n"
    )
    assert result.stderr == ""


def test_selects_subtraction(executable):
    print("Testing subtraction (choice 1)...")
    result = subprocess.run(
        [str(executable)],
        input="1\n7 2\n",
        text=True,
        capture_output=True,
        check=False,
    )
    print(result.stdout, end="")

    assert result.returncode == 0
    assert result.stdout == (
        "Choose operation (0 for addition, 1 for subtraction): "
        "Enter two numbers: Their difference is 5\n"
    )
    assert result.stderr == ""