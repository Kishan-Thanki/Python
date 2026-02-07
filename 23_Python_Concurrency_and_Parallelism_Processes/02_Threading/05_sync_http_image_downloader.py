"""
================================================================================
SYNCHRONOUS HTTP IMAGE DOWNLOADER (CLEAN BASELINE)
================================================================================

This example demonstrates a CORRECT and CLEAN implementation of a
SYNCHRONOUS image downloader using blocking HTTP requests.

This file acts as the **baseline performance reference** for all future
concurrent and AsyncIO-based implementations.

IMPORTANT:
- No bugs
- No missing commas
- No tricks
- No concurrency
- Pure synchronous I/O

This file should be READ and UNDERSTOOD before moving forward.

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. How synchronous HTTP requests behave in real life
2. Why network I/O dominates execution time
3. Why execution time grows linearly
4. Why correctness does NOT equal scalability
5. The real motivation behind concurrency and AsyncIO

================================================================================
"""

import time
import requests


# ------------------------------------------------------------------------------
# IMAGE URLS (CLEAN & CORRECT)
# ------------------------------------------------------------------------------
# These URLs are intentionally processed ONE BY ONE.
#
# For each image:
# - A network request is made
# - The program WAITS for the response
# - The image is written to disk
#
# No overlap occurs.
# ------------------------------------------------------------------------------
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-03361168cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


# ------------------------------------------------------------------------------
# START TIMER
# ------------------------------------------------------------------------------
# We measure TOTAL wall-clock time.
# ------------------------------------------------------------------------------
start = time.perf_counter()


# ------------------------------------------------------------------------------
# SYNCHRONOUS DOWNLOAD LOOP
# ------------------------------------------------------------------------------
for img_url in img_urls:

    # --------------------------------------------------------------------------
    # BLOCKING NETWORK REQUEST
    # --------------------------------------------------------------------------
    # requests.get() blocks until:
    # - Connection completes
    # - Server responds
    # - Entire response body is downloaded
    # --------------------------------------------------------------------------
    img_bytes = requests.get(img_url).content

    # --------------------------------------------------------------------------
    # FILE NAME EXTRACTION
    # --------------------------------------------------------------------------
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'

    # --------------------------------------------------------------------------
    # BLOCKING FILE WRITE
    # --------------------------------------------------------------------------
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloaded')


# ------------------------------------------------------------------------------
# STOP TIMER
# ------------------------------------------------------------------------------
finished = time.perf_counter()


# ------------------------------------------------------------------------------
# PRINT TOTAL EXECUTION TIME
# ------------------------------------------------------------------------------
print(f"Finished in: {round(finished - start, 2)} seconds")


# ==============================================================================
# OBSERVED OUTPUT (EXAMPLE)
# ==============================================================================

"""
photo-1516117172878-fd2c41f4a759.jpg downloaded
photo-1532009324734-20a7a5813719.jpg downloaded
...
photo-1549692520-acc6669e2f0c.jpg downloaded
Finished in: ~14.17 seconds
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY DOES THIS TAKE ~14 SECONDS?

Because:
✔ Each image is downloaded sequentially
✔ Network latency dominates execution
✔ Requests DO NOT overlap
✔ CPU waits idle during network I/O
✔ Total time ≈ sum of individual request times
"""


"""
IS THIS CODE BAD?

NO.

✔ It is correct
✔ It is readable
✔ It is simple
✔ It is deterministic

But it does NOT scale.
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ Synchronous HTTP I/O blocks execution
✔ Correctness does not imply performance
✔ Network-bound programs require concurrency
✔ This is the baseline for all improvements
"""
