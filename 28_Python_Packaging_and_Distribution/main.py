"""
Packaging and Distribution in Python

This file provides a clean, professional, and structured overview of
Python packaging and distribution concepts that every serious Python
developer must understand.

Topics covered:
- pip
- requirements.txt
- pyproject.toml
- Poetry
- setuptools
- Versioning (Semantic Versioning)
"""

# ============================================================
# 1. pip (Python Package Installer)
# ============================================================
#
# pip is the default package manager for Python.
# It installs packages from the Python Package Index (PyPI).

# Common commands (run in terminal, not in code):
#
# pip install requests
# pip uninstall requests
# pip list
# pip freeze
#
# pip works with:
# - wheels (.whl)
# - source distributions (.tar.gz)

# Best practices:
# - Use virtual environments
# - Avoid installing packages globally
# - Pin dependency versions for reproducibility


# ============================================================
# 2. requirements.txt
# ============================================================
#
# requirements.txt is a plain text file listing project dependencies.
# It is commonly used with pip.

"""
Example requirements.txt:

requests==2.31.0
flask>=2.3.0
numpy~=1.26.0
"""

# Install dependencies:
# pip install -r requirements.txt

# Version specifiers:
# ==  exact version
# >=  minimum version
# <=  maximum version
# ~=  compatible release
# !=  exclude version

# Limitations:
# - No dependency resolution locking
# - No build metadata
# - Not ideal for large or complex projects


# ============================================================
# 3. pyproject.toml
# ============================================================
#
# pyproject.toml is the modern standard for Python project configuration.
# Introduced by PEP 518 and extended by PEP 621.

"""
Example pyproject.toml (basic):

[project]
name = "my_project"
version = "0.1.0"
description = "Sample Python project"
authors = [{ name = "Your Name" }]
dependencies = [
    "requests>=2.31.0"
]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
"""

# Advantages:
# - Standardized
# - Tool-agnostic
# - Supports metadata, dependencies, and build configuration
# - Required for modern packaging tools


# ============================================================
# 4. Poetry
# ============================================================
#
# Poetry is a modern dependency management and packaging tool.
# It uses pyproject.toml as its primary configuration file.

"""
Example pyproject.toml (Poetry):

[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "Sample project"
authors = ["Your Name"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"

[tool.poetry.dev-dependencies]
pytest = "^8.0.0"
"""

# Common Poetry commands:
#
# poetry install
# poetry add requests
# poetry remove requests
# poetry update
# poetry build
# poetry publish

# Advantages:
# - Dependency resolution with lock file
# - Virtual environment management
# - Reproducible builds
# - Cleaner workflow than pip + requirements.txt


# ============================================================
# 5. setuptools
# ============================================================
#
# setuptools is the traditional Python packaging library.
# It is still widely used and supported.

"""
Example setup.py:

from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
)
"""

# Modern best practice:
# - Prefer pyproject.toml over setup.py
# - setuptools is often used indirectly as a build backend

# setuptools handles:
# - Package discovery
# - Dependency declaration
# - Distribution builds (sdist, wheel)


# ============================================================
# 6. Versioning (Semantic Versioning)
# ============================================================
#
# Semantic Versioning (SemVer):
#
# MAJOR.MINOR.PATCH
#
# Example:
# 1.4.2
#
# MAJOR: incompatible API changes
# MINOR: backward-compatible features
# PATCH: backward-compatible bug fixes

# Examples:
# 1.0.0  Initial stable release
# 1.1.0  New features added
# 1.1.1  Bug fixes
# 2.0.0  Breaking changes

# Best practices:
# - Follow semantic versioning consistently
# - Document breaking changes
# - Pin versions in production
# - Use version ranges for libraries


# ============================================================
# 7. Choosing the Right Tool
# ============================================================
#
# Small scripts:
# - pip + requirements.txt
#
# Medium to large applications:
# - pyproject.toml + Poetry
#
# Libraries intended for PyPI:
# - pyproject.toml + setuptools or Poetry
#
# Enterprise environments:
# - Poetry or pip-tools with strict version locking


# ============================================================
# 8. Summary
# ============================================================
#
# - pip installs Python packages
# - requirements.txt lists dependencies for pip
# - pyproject.toml is the modern packaging standard
# - Poetry simplifies dependency and environment management
# - setuptools is the traditional packaging backend
# - Semantic versioning ensures predictable releases
#
# Proper packaging and versioning are essential for:
# - Reproducibility
# - Collaboration
# - Deployment
# - Long-term maintainability
