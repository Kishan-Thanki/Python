"""
================================================================================
CAPTURING stdout AND stderr
================================================================================

Demonstrates capturing command output into Python.
"""

import subprocess

p1 = subprocess.run(
    ['ls', '-la'],
    capture_output=True,
    text=True
)

print("STDOUT:")
print(p1.stdout)

print("STDERR:")
print(p1.stderr)
