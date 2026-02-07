"""
================================================================================
THREADED HTTP IMAGE DOWNLOADER — ThreadPoolExecutor
================================================================================

This example demonstrates CONCURRENT image downloading using
ThreadPoolExecutor with blocking HTTP requests.

IMPORTANT:
- Same requests library
- Same download logic
- Same file-writing logic
- Only the EXECUTION MODEL changes

This file proves:
✔ Blocking I/O can be overlapped
✔ Threads shine for I/O-bound tasks
✔ Performance improves WITHOUT AsyncIO

================================================================================
WHAT THIS EXAMPLE TEACHES
================================================================================

1. How ThreadPoolExecutor overlaps blocking I/O
2. Why threads work well for network-bound workloads
3. How executor.map() manages thread lifecycle
4. Why order of completion becomes non-deterministic
5. How much faster concurrency can be — even with bugs

================================================================================
"""

import time
import requests
import concurrent.futures


# ------------------------------------------------------------------------------
# IMAGE URLS (INTENTIONALLY LEFT AS-IS)
# ------------------------------------------------------------------------------
# NOTE:
# -----
# Two URLs are accidentally concatenated due to missing commas.
# This is NOT fixed intentionally to prove:
#
# - Concurrency does NOT hide logical bugs
# - Threading does NOT validate data correctness
# - The program still overlaps I/O correctly
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
start = time.perf_counter()


# ------------------------------------------------------------------------------
# DOWNLOAD FUNCTION (BLOCKING)
# ------------------------------------------------------------------------------
def download_image(img_url: str) -> None:
    """
    Downloads a single image synchronously.

    Even though this function is BLOCKING,
    multiple instances will run CONCURRENTLY
    in different threads.
    """
    img_bytes = requests.get(img_url).content

    img_name = img_url.split('/')[3]
    img_name = f'23_Python_Concurrency_and_Parallelism_Processes/02_Threading/images/{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloaded')


# ------------------------------------------------------------------------------
# THREAD POOL EXECUTION
# ------------------------------------------------------------------------------
# executor.map():
# - Submits all tasks
# - Runs them concurrently
# - Waits for completion implicitly
# ------------------------------------------------------------------------------
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


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
photo-1507143550189-fed454f93097.jpg downloaded
photo-1513938709626-03361168cc03.jpg downloaded
photo-1541698444083-023c97d3f4b6https:.jpg downloaded
photo-1504198453319-5ce911bafcdehttps:.jpg downloaded
...
Finished in: ~8.41 seconds
"""


# ==============================================================================
# IMPORTANT OBSERVATIONS
# ==============================================================================

"""
WHY IS THIS MUCH FASTER?

Because:
✔ Network I/O overlaps
✔ Threads wait independently
✔ CPU stays busy scheduling threads
✔ Total time ≈ slowest requests, not sum
"""


"""
WHY IS OUTPUT ORDER RANDOM?

Because:
✔ Threads finish when their I/O completes
✔ Completion order ≠ submission order
✔ Concurrency is non-deterministic by nature
"""


"""
WHY ARE BUGGY FILENAMES STILL PRESENT?

Because:
✔ Threading improves execution, not correctness
✔ Logic bugs survive concurrency
✔ Performance ≠ correctness
"""


# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================

"""
✔ ThreadPoolExecutor is ideal for I/O-bound tasks
✔ Blocking libraries still benefit from threading
✔ Concurrency drastically reduces wall-clock time
✔ Threading scales better than synchronous code
✔ AsyncIO is NOT required yet
"""
