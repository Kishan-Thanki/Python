"""
Security Basics in Python

This file provides a clean, professional, and structured overview of
essential security concepts every Python developer must understand.

Topics covered:
- Input validation
- Secrets handling
- Hashing
- Encryption basics
- Avoiding eval and exec
"""

# ============================================================
# 1. Input Validation
# ============================================================
#
# Input validation ensures that user-provided data is safe,
# expected, and well-formed before processing.

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError("Age out of valid range")
    return age

try:
    validate_age(25)
    validate_age("25")
except Exception as e:
    print(e)

# Best practices:
# - Validate type, range, and format
# - Reject invalid input early
# - Never trust user input


# ============================================================
# 2. Secrets Handling
# ============================================================
#
# Secrets include passwords, API keys, tokens, and credentials.
# They should never be hardcoded in source code.

import os

# Recommended: use environment variables
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    print("API_KEY not set")

# Avoid:
# API_KEY = "hardcoded-secret"

# Best practices:
# - Use environment variables
# - Use secret managers (AWS Secrets Manager, Vault, etc.)
# - Never commit secrets to version control


# ============================================================
# 3. Hashing
# ============================================================
#
# Hashing is a one-way operation.
# Common use case: storing passwords securely.

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed = hash_password("my_secure_password")
print(hashed)

# For real applications, use stronger password hashing:
# - bcrypt
# - argon2
# - scrypt

# Never store plain-text passwords.

# ============================================================
# 4. Avoiding eval and exec
# ============================================================
#
# eval and exec execute arbitrary code.
# Using them with user input leads to severe security vulnerabilities.

# Dangerous example (DO NOT USE):
# user_input = "__import__('os').system('rm -rf /')"
# eval(user_input)

# Safe alternative examples:

# Mapping commands explicitly
def calculate(operation, a, b):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else None
    }
    return operations.get(operation)

print(calculate("add", 10, 5))

# Use ast.literal_eval for safe evaluation of literals
import ast

safe_data = ast.literal_eval("[1, 2, 3]")
print(safe_data)

# Best practices:
# - Never use eval or exec on user input
# - Prefer explicit logic and safe parsers
# - Use ast.literal_eval only for trusted literals


# ============================================================
# 5. Summary
# ============================================================
#
# - Validate all user input
# - Keep secrets out of source code
# - Hash passwords, never store them directly
# - Avoid eval and exec entirely
#
# Security is not optional.
# Secure code is a fundamental responsibility of every Python developer.
