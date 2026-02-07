"""
================================================================================
ENFORCING FAILURE WITH check=True
================================================================================

This file shows how to convert command failures into Python exceptions.
"""

import subprocess

try:
    subprocess.run(
        ['ls', '-la', 'dne'],
        check=True
    )
except subprocess.CalledProcessError as exc:
    print("Command failed!")
    print("Return code:", exc.returncode)
