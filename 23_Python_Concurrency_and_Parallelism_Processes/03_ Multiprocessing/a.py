# ============================================================
# 6. multiprocessing Pool
# ============================================================
#
# Pools manage a fixed number of worker processes.
# They simplify distributing work across CPU cores.

from multiprocessing import Pool, cpu_count

def cube(n):
    return n ** 3

if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        results = pool.map(cube, [1, 2, 3, 4, 5])
        print(results)