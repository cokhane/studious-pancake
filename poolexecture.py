# from concurrent.futures import ProcessPoolExecutor, as_completed
# import math, os
#
# def heavy(n):
#     # simulate CPU work
#     s = 0
#     for i in range(10_000_00):
#         s += math.sin(i + n)
#     return n, s, os.getpid()
#
# if __name__ == "__main__":  # required on Windows/macOS for process pools
#     with ProcessPoolExecutor() as pool:  # defaults to os.cpu_count() workers
#         futures = [pool.submit(heavy, i) for i in range(8)]
#         for fut in as_completed(futures):
#             print(fut.result())


def heavy():
    for i in range(10_000_00):
        a = 1 + 1

    return True
print(heavy())