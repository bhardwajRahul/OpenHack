from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent


def read_project_version() -> str:
    in_project = False
    for line in (ROOT / "pyproject.toml").read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "[project]":
            in_project = True
            continue
        if in_project and stripped.startswith("["):
            break
        if in_project and stripped.startswith("version"):
            return stripped.split("=", 1)[1].strip().strip('"')
    raise RuntimeError("Unable to read project.version from pyproject.toml")


setup(
    name="openhack",
    version=read_project_version(),
    description=(
        "File-based, scenario-first workspace for source-guided whitebox "
        "security review."
    ),
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "jsonschema>=4.18",
        "PyYAML>=6.0",
    ],
    extras_require={
        "dev": [
            "ruff>=0.6",
            "mypy>=1.10",
            "types-jsonschema",
        ],
    },
    entry_points={
        "console_scripts": [
            "openhack=openhack.cli:main",
        ],
    },
)
