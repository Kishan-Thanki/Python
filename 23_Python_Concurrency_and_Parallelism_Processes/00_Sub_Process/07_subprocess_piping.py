"""
================================================================================
PIPING OUTPUT BETWEEN SUBPROCESSES — subprocess.run
================================================================================

This example demonstrates how to manually PIPE the output of one external
command into another using Python's subprocess module.

Shell equivalent:
-----------------
cat output.txt | grep -n test

Instead of relying on shell pipes (|), Python explicitly:
1. Captures stdout from one process
2. Passes it as stdin to another process

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. How to capture stdout from a subprocess
2. How to pass captured output as input to another subprocess
3. How subprocess replaces shell pipelines safely
4. Why explicit piping is preferred in Python
5. How text flows between OS-level processes

================================================================================
"""

import subprocess


# ------------------------------------------------------------------------------
# FIRST PROCESS: READ FILE CONTENT
# ------------------------------------------------------------------------------
# Equivalent to:
#   cat output.txt
#
# - capture_output=True captures stdout
# - text=True converts bytes -> str
# ------------------------------------------------------------------------------
p1 = subprocess.run(
    ['cat', '23_Python_Concurrency_and_Parallelism_Processes/00_Sub_Process/output.txt'],
    capture_output=True,
    text=True
)

# Display the raw file content
print("---- FILE CONTENT ----")
print(p1.stdout)


# ------------------------------------------------------------------------------
# SECOND PROCESS: FILTER CONTENT USING grep
# ------------------------------------------------------------------------------
# Equivalent to:
#   grep -n test
#
# - input=p1.stdout sends previous stdout to stdin
# - grep reads from stdin instead of a file
# ------------------------------------------------------------------------------
p2 = subprocess.run(
    ['grep', '-n', 'test'],
    capture_output=True,
    text=True,
    input=p1.stdout
)

# Display filtered lines with line numbers
print("---- FILTERED OUTPUT ----")
print(p2.stdout)
