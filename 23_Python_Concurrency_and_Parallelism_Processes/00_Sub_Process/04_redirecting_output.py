"""
================================================================================
REDIRECTING OUTPUT TO A FILE
================================================================================

Instead of storing output in memory, redirect it to disk.
"""

import subprocess

with open('output.txt', 'w') as f:
    subprocess.run(
        ['ls', '-la'],
        stdout=f,
        text=True
    )

print("Output written to output.txt")
