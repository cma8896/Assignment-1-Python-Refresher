# Cade Anderson
# fib.py

import functools
from functools import lru_cache
import time
import matplotlib.pyplot as plt

time_data = []


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished in {run_time:.8f}s: {func.__name__}({args[0]}) -> {value}")

        time_data.append(run_time)

        return value

    return wrapper_timer


@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)

    plt.plot(time_data, color="b")
    plt.title("Fibonacci Execution Time")
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Time in seconds")
    plt.grid(True)
    plt.savefig("fibonacci_times.png")
    plt.show()
