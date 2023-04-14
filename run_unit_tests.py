import pytest
import sys

if __name__ == "__main__":
    retcode: int | pytest.ExitCode = pytest.main(["--mypy"])

    if retcode == pytest.ExitCode.OK:
        print(f"\n---\nYou are using Python {sys.version} btw\n---\n")
