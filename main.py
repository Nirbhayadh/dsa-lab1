from random import sample
from search import linear_search, binary_search
from time import time_ns


def run(n):
    data = [i for i in range(1, n+1)]
    start_time = time_ns()
    binary_search(data, data[-1], 0, n-1)
    end_time = time_ns()
    time_taken = end_time - start_time
    return time_taken


if __name__ == "__main__":
    for i in range(10000000, 100000001, 10000000):
        print(f"Number of sample data: {i}, Time Taken: {run(i)} nanosecond")


# def run(n):
#     data = sample(range(1, n+1), n)
#     start_time = time_ns()
#     l = linear_search(data, data[-1])

#     end_time = time_ns()

#     time_taken = end_time - start_time
#     return time_taken


# if __name__ == "__main__":
#     for i in range(1000000, 10000001, 1000000):
#         print(f"Number of sample data: {i}, Time Taken: {run(i)} nanosecond")
