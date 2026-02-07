"""
================================================================================
ERROR HANDLING — return codes & stderr
================================================================================

This example INTENTIONALLY FAILS to show how subprocess reports errors.
"""

import subprocess

p1 = subprocess.run(
    ['ls', '-la', 'dne'],  # Non-existent directory
    capture_output=True,
    text=True
)

# Exit code: 0 = success, non-zero = failure
print("Return Code:")
print(p1.returncode)

print("\nStandard Error:")
print(p1.stderr)
