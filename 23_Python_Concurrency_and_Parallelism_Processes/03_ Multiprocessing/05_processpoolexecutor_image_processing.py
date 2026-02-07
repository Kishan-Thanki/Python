"""
================================================================================
PARALLEL IMAGE PROCESSING — ProcessPoolExecutor (REAL-WORLD EXAMPLE)
================================================================================

This example demonstrates how to use multiprocessing to speed up
CPU-intensive image processing tasks using Python's ProcessPoolExecutor.

We perform the following operations on each image:
✔ Load image from disk
✔ Apply Gaussian blur (CPU heavy)
✔ Resize (thumbnail)
✔ Save processed image to output directory

This is a **classic multiprocessing use-case** because:
✔ Image processing is CPU-bound
✔ GIL does NOT block multiprocessing
✔ Each task is independent
✔ Workload can be distributed across cores

================================================================================
DIRECTORY STRUCTURE EXPECTED
================================================================================

project/
│
├── images/          # Input images (.jpg)
├── processed/       # Output images (auto-created)
└── this_script.py

================================================================================
"""

import time
import os
import concurrent.futures
from PIL import Image, ImageFilter


# ------------------------------------------------------------------------------
# RESOLVE SCRIPT & IMAGE DIRECTORIES
# ------------------------------------------------------------------------------
# Ensures paths work regardless of where the script is run from
# ------------------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))

img_dir = os.path.join(script_dir, 'images')
processed_dir = os.path.join(script_dir, 'processed')


# ------------------------------------------------------------------------------
# COLLECT IMAGE FILES
# ------------------------------------------------------------------------------
# Safely read all .jpg files from the images directory
# ------------------------------------------------------------------------------
try:
    img_files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')]
    img_paths = [os.path.join(img_dir, f) for f in img_files]
except FileNotFoundError:
    print(f"ERROR: Could not find folder: {img_dir}")
    print("Make sure your 'images' folder is in the same directory as this script.")
    exit()


# ------------------------------------------------------------------------------
# IMAGE PROCESSING FUNCTION (RUNS IN CHILD PROCESSES)
# ------------------------------------------------------------------------------
def process_image(img_path: str) -> str:
    """
    Applies image processing steps:
    - Gaussian blur
    - Resize thumbnail
    - Save processed image

    This function is executed in a SEPARATE PROCESS.

    Arguments:
    ----------
    img_path : str : absolute path to the image file

    Returns:
    --------
    str : status message
    """
    size = (1200, 1200)
    filename = os.path.basename(img_path)

    # Safety check
    if not os.path.exists(img_path):
        return f"{filename} -> Skipped (Not Found)"

    try:
        img = Image.open(img_path)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)

        # Ensure output directory exists
        os.makedirs(processed_dir, exist_ok=True)

        save_path = os.path.join(processed_dir, filename)
        img.save(save_path)

        return f"{filename} processed..."

    except Exception as e:
        return f"Failed {filename}: {e}"


# ------------------------------------------------------------------------------
# MAIN FUNCTION (PARENT PROCESS)
# ------------------------------------------------------------------------------
def main():
    """
    Distributes image processing tasks across multiple processes
    using ProcessPoolExecutor.
    """
    start = time.perf_counter()

    print(f"Found {len(img_paths)} images to process...")

    # Create a pool of worker processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # map() distributes work automatically
        results = executor.map(process_image, img_paths)

        # Results are returned in submission order
        for result in results:
            print(result)

    finished = time.perf_counter()
    print(f"Finished in: {round(finished - start, 2)} seconds")


# ------------------------------------------------------------------------------
# REQUIRED ENTRY POINT FOR MULTIPROCESSING
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


# ==============================================================================
# KEY OBSERVATIONS
# ==============================================================================

"""
1. WHY MULTIPROCESSING?
   - Image filtering & resizing are CPU-bound
   - Threads would be blocked by the GIL
   - Processes bypass the GIL entirely

2. WHY ProcessPoolExecutor?
   - Automatically manages worker processes
   - Safer and cleaner than multiprocessing.Process
   - Scales based on available CPU cores

3. WHY executor.map()?
   - Simplifies task submission
   - Preserves input order
   - Blocks until all tasks are completed

4. REAL-WORLD IMPACT:
   - Large image batches process significantly faster
   - Total time ≈ slowest batch handled by pool
"""
