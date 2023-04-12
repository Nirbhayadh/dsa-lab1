import math
from time import time_ns


# def linear_search(values, target, index):
#     if index == len(values):
#         return -1
#     if (values[index] == target):
#         return index
#     return linear_search(values, target, index+1)

def linear_search(data, target):
    for i in range(len(data)):
        if (data[i] == target):
            return i
    return -1


def binary_search(values, target, p, q):
    if (p > q):
        return -1
    m = math.floor((p+q)/2)
    if (values[m] == target):
        return m
    elif (values[m] < target):
        return binary_search(values, target, m+1, q)
    else:
        return binary_search(values, target, p, m-1)





