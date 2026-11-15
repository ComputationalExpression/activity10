"""Checks for Activity 10 that read your code and run your own tests.

A good test fails when the code it tests is wrong. To check that, these
checks make a copy of your src/tune.py with one method broken on purpose, so
that it skips its work and returns None, then run your tests/test_my_tune.py on
that copy. If your tests still pass, they did not notice the broken method.
"""

import ast
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TUNE = ROOT / "src" / "tune.py"
MINE = ROOT / "tests" / "test_my_tune.py"
DECISION = re.compile(r"^\s*#\s*copilot\s*:\s*(accepted|edited|rejected)", re.IGNORECASE)
METHODS = ["__init__", "add", "length", "frequencies", "highest", "describe"]


def functions(path):
    """Return each top-level function, and each method of each class, in a file."""
    found = []
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.FunctionDef):
            found.append(node)
        if isinstance(node, ast.ClassDef):
            found += [n for n in node.body if isinstance(n, ast.FunctionDef)]
    return found


def has_decision(lines, function):
    """Return True when a # Copilot: comment sits just above the def or inside the function."""
    start = function.lineno - 2
    while start > 0 and lines[start].strip() == "":
        start -= 1
    return any(DECISION.match(line) for line in lines[start:function.end_lineno])


def my_tests():
    """Return the test functions in tests/test_my_tune.py that contain an assert."""
    return [
        f for f in functions(MINE)
        if f.name.startswith("test") and any(isinstance(n, ast.Assert) for n in ast.walk(f))
    ]


def run_my_tests(source_folder):
    """Run tests/test_my_tune.py with tune imported from source_folder; return pytest's result."""
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(MINE), "-q", "-p", "no:cacheprovider",
         "-o", f"pythonpath={source_folder}", "-o", "testpaths=tests"],
        cwd=ROOT, capture_output=True, text=True, timeout=60,
    )


def broken(method):
    """Return the source of src/tune.py with method's body replaced by return None."""
    tree = ast.parse(TUNE.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method:
            node.body = [ast.Return(value=ast.Constant(value=None))]
    return ast.unparse(tree)


def test_copilot_decisions():
    lines = TUNE.read_text(encoding="utf-8").splitlines()
    methods = {f.name: f for f in functions(TUNE)}
    missing = [name for name in METHODS if name not in methods]
    assert not missing, f"src/tune.py is missing the method(s) {missing}: please keep each method from the starter"
    unmarked = [name for name in METHODS if not has_decision(lines, methods[name])]
    assert not unmarked, (
        f"found no '# Copilot: accepted', '# Copilot: edited' or '# Copilot: rejected' for {unmarked} "
        "in src/tune.py: put one on the line above each def"
    )
    mine = my_tests()
    test_lines = MINE.read_text(encoding="utf-8").splitlines()
    marked = [f.name for f in mine if has_decision(test_lines, f)]
    assert len(marked) >= 5, (
        f"found a '# Copilot:' comment above {len(marked)} of your tests in tests/test_my_tune.py: "
        "please mark each of the five tests you write"
    )


@pytest.mark.timeout(60)
def test_my_tests_pass():
    mine = my_tests()
    assert len(mine) >= 6, (
        f"found {len(mine)} test functions with an assert in tests/test_my_tune.py: "
        "please write one for each method, five more besides the example"
    )
    result = run_my_tests(ROOT / "src")
    passed = result.returncode == 0
    assert passed, (
        "your tests in tests/test_my_tune.py do not all pass on your Tune class. Run "
        "uv run pytest tests/test_my_tune.py and read the last lines:\n" + result.stdout[-1500:]
    )


@pytest.mark.timeout(120)
@pytest.mark.parametrize("method", ["add", "length", "frequencies", "highest", "describe"])
def test_my_tests_notice(method):
    ready = run_my_tests(ROOT / "src").returncode == 0 and len(my_tests()) >= 6
    assert ready, (
        "first make your own tests pass on your Tune class: run uv run pytest tests/test_my_tune.py"
    )
    with tempfile.TemporaryDirectory() as folder:
        (Path(folder) / "tune.py").write_text(broken(method), encoding="utf-8")
        caught = run_my_tests(folder).returncode != 0
    assert caught, (
        f"your tests still all pass when {method}() is broken so that it skips its work and returns None. "
        f"Please add an assert that checks what {method}() returns or keeps"
    )
