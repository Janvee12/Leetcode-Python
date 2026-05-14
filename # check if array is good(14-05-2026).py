# ============================
# PLATFORM:
# LeetCode (Problem 2784 - Check if Array is Good)
# ============================

# ============================
# PROBLEM:
# You are given an integer array nums.
#
# An array is considered "good" if:
# - It contains all integers from 1 to n-1 exactly once
# - And contains exactly one extra occurrence of number n-1
#   (i.e., the maximum number appears twice)
#
# Task:
# Return True if the array is good, otherwise False.
#
# ============================
# EXAMPLE:
# Input:
# nums = [1,2,3,3]
#
# Output:
# True
# ============================

# ============================
# APPROACH:
#
# 1. Sort the array.
#
# 2. Expected sequence check:
#    - First n-1 elements should be:
#          1, 2, 3, ..., n-1
#
# 3. Last element should be:
#          n-1 (duplicate of last valid number)
#
# 4. If any mismatch occurs → return False
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
# → sorting
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def isGood(self, nums: List[int]) -> bool:

        nums.sort()
        n = len(nums)

        expected = 1

        # Check first n-1 elements
        for i in range(n - 1):

            if nums[i] != expected:
                return False

            expected += 1

        # Last element must match n-1
        return nums[-1] == n - 1