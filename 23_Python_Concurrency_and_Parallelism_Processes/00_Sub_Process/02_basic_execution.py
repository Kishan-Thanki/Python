"""
================================================================================
BASIC COMMAND EXECUTION — subprocess.run
================================================================================

This file demonstrates the MOST BASIC usage of subprocess.run().
"""

import subprocess

# Executes command and waits for completion
# stdout and stderr are NOT captured
# Errors do NOT raise exceptions
subprocess.run(['ls', '-la'])
