# Daily Coding Problem 243
# Given an array of numbers A and an integer k, your task is to split
# N into k partitions such that the maximum sum of any partition is minimized
# Return this sum.

# Input array to f
A = [5, 1, 2, 7, 3, 4]

memo = {}

def f(start, k):
    if k == 1:
        if A[start:] != []:
            return sum(A[start:])
        else:
            return None
    mins = []
    for i in range(1, len(A) - start):
        if (start + i, k) not in memo:
            memo[(start + i, k)] = f(start + i, k - 1)
        rest = memo[(start + i, k)]
        if rest is None:
            continue
        mins.append(max(sum(A[start:start + i]), rest))
    if mins == []:
        return None
    return min(mins)

import time
t = time.time()
print f(0, 3)
print "Took %s seconds" % (time.time() - t)
