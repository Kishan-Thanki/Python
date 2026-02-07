"""
Testing in Python

This file provides a clean, professional, and structured overview of
testing in Python, covering both built-in and third-party tools.

Topics covered:
- unittest
- pytest
- Fixtures
- Mocking
- Parameterized tests
- Coverage
"""

# ============================================================
# 1. Why Testing Matters
# ============================================================
#
# Testing ensures that:
# - Code behaves as expected
# - Bugs are caught early
# - Refactoring is safe
# - Systems remain stable over time
#
# Good tests are:
# - Repeatable
# - Isolated
# - Fast
# - Deterministic


# ============================================================
# 2. unittest (Standard Library)
# ============================================================
#
# unittest is Python’s built-in testing framework.
# It follows the xUnit style used in many languages.

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

# Tests are usually run with:
# python -m unittest test_file.py


# ============================================================
# 3. pytest (Third-Party Framework)
# ============================================================
#
# pytest is a popular testing framework that emphasizes simplicity.
# It uses plain assert statements and minimal boilerplate.

def subtract(a, b):
    return a - b

def test_subtract_basic():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(3, 5) == -2

# pytest automatically discovers tests prefixed with "test_"
# Run with:
# pytest


# ============================================================
# 4. Fixtures
# ============================================================
#
# Fixtures provide setup and teardown logic for tests.
# They help reuse test data and isolate test environments.

import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_sample_data_name(sample_data):
    assert sample_data["name"] == "Alice"

def test_sample_data_age(sample_data):
    assert sample_data["age"] == 30

# Fixtures can have scopes:
# function, class, module, session


# ============================================================
# 5. Mocking
# ============================================================
#
# Mocking replaces real objects with fake ones to isolate behavior.
# Commonly used to mock:
# - Network calls
# - Database access
# - External APIs
# - Time-dependent logic

from unittest.mock import Mock, patch

def fetch_data(api_client):
    return api_client.get("/data")

def test_fetch_data_with_mock():
    mock_client = Mock()
    mock_client.get.return_value = {"status": "ok"}

    result = fetch_data(mock_client)

    mock_client.get.assert_called_once_with("/data")
    assert result["status"] == "ok"

# Using patch to mock functions or objects
@patch("time.sleep")
def test_sleep_is_mocked(mock_sleep):
    import time
    time.sleep(5)
    mock_sleep.assert_called_once_with(5)


# ============================================================
# 6. Parameterized Tests
# ============================================================
#
# Parameterized tests allow running the same test logic
# with multiple input sets.

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-2, -3, -5),
    ],
)
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected

# This avoids duplicated test functions and improves readability.


# ============================================================
# 7. Coverage
# ============================================================
#
# Coverage measures how much of your code is executed by tests.
# It helps identify untested paths.

# Install coverage:
# pip install coverage

# Run tests with coverage:
# coverage run -m pytest
# coverage report
# coverage html

# Coverage types:
# - Line coverage
# - Branch coverage
# - Path coverage

# High coverage does NOT guarantee bug-free code,
# but low coverage almost guarantees missing tests.


# ============================================================
# 8. Best Practices
# ============================================================
#
# - Write tests alongside code
# - Test behavior, not implementation details
# - Keep tests small and focused
# - Avoid shared state between tests
# - Mock external dependencies
# - Run tests automatically (CI pipelines)


# ============================================================
# 9. unittest vs pytest
# ============================================================
#
# unittest:
# - Built-in
# - Class-based
# - More boilerplate
#
# pytest:
# - Third-party
# - Function-based
# - Powerful fixtures
# - Cleaner syntax
#
# pytest is generally preferred for modern Python projects.


# ============================================================
# 10. Summary
# ============================================================
#
# - unittest is Python’s standard testing framework
# - pytest provides a simpler and more expressive approach
# - Fixtures manage setup and teardown
# - Mocking isolates dependencies
# - Parameterized tests reduce duplication
# - Coverage identifies untested code paths
#
# Strong testing practices are essential for
# building reliable, maintainable, and scalable systems.
