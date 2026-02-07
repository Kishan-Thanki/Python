"""
================================================================================
RUNNING EXTERNAL COMMANDS IN PYTHON — subprocess.run
================================================================================

This module introduces subprocess at a CONCEPTUAL level.

Unlike threading or asyncio, subprocess focuses on:
- Spawning OS-level processes
- Executing external commands
- Communicating via stdout / stderr
- Reading exit codes

================================================================================
WHEN TO USE subprocess
================================================================================

Use subprocess when you need to:

✔ Call shell/system commands (ls, grep, curl, git, ffmpeg, etc.)
✔ Interact with non-Python tools
✔ Capture stdout / stderr
✔ Check exit codes
✔ Integrate Python with system-level workflows

================================================================================
IMPORTANT CONCEPTS
================================================================================

1. subprocess.run() spawns a NEW process
2. stdout, stderr, and return codes are explicit
3. Errors do NOT raise exceptions by default
4. Failure is reported as DATA, not crashes
5. check=True converts failures into exceptions
"""

import subprocess
