from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


def _read_source_version() -> str:
    pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
    in_project = False
    try:
        lines = pyproject.read_text(encoding="utf-8").splitlines()
    except OSError:
        return "0+unknown"
    for line in lines:
        stripped = line.strip()
        if stripped == "[project]":
            in_project = True
            continue
        if in_project and stripped.startswith("["):
            break
        if in_project and stripped.startswith("version"):
            return stripped.split("=", 1)[1].strip().strip('"')
    return "0+unknown"


try:
    __version__ = version("openhack")
except PackageNotFoundError:
    __version__ = _read_source_version()

VERSION = __version__
