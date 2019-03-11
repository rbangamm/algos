# DCP 152
# Given two lists; one of nums and the other of their respective probabilities,
# create a distribution for these numbers based on their corresponding probabilities.
# E.g [1, 2, 3, 4] and [0.1, 0.5, 0.2, 0.2]. 1 should appear 10% of the time, 
# 2 50% of the time, etc. This is my solution with O(n) time complexity and O(1) space
# complexity.
import random

def distribution(nums, probs):
    for i in range(len(probs)):
        if i == 0:
            continue
        probs[i] += probs[i - 1]
        
    r = random.random()
    for i in range(len(nums)):
        if r <= probs[i]:
            return nums[i]

print distribution([1,2,3,4], [0.1, 0.5, 0.2, 0.2])
