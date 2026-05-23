# ============================
# PLATFORM:
# LeetCode
# (Problem 1752 - Check if Array Is Sorted and Rotated)
# ============================

# ============================
# PROBLEM:
# Given an array nums,
# return True if the array
# was originally sorted
# in non-decreasing order
# and then rotated.
#
# Otherwise return False.
#
# Rotation means:
# moving some front elements
# to the back.
#
# Example:
#
# Input:
# nums = [3,4,5,1,2]
#
# Output:
# True
#
# Original sorted array:
# [1,2,3,4,5]
#
# Rotated array:
# [3,4,5,1,2]
#
# Example:
#
# Input:
# nums = [2,1,3,4]
#
# Output:
# False
# ============================

# ============================
# APPROACH:
#
# Key Idea:
#
# A sorted rotated array
# can have at most ONE place
# where:
#
#     nums[i] > nums[i+1]
#
# Example:
#
# [3,4,5,1,2]
#          ^
#
# Only one decreasing point.
#
# Steps:
#
# 1. Traverse circularly.
#
# 2. Count consecutive
#    non-decreasing elements.
#
# 3. If count reaches N,
#    array is valid.
#
# ============================

# ============================
# ALTERNATIVE SIMPLE IDEA:
#
# Count drops:
#
# if nums[i] > nums[(i+1)%N]
#
# drops += 1
#
# Valid if drops <= 1
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def check(self, nums: List[int]) -> bool:

        N = len(nums)

        # Current sorted streak
        count = 1

        # Traverse circularly
        for i in range(1, 2 * N):

            # Non-decreasing order
            if nums[(i - 1) % N] <= nums[i % N]:

                count += 1

            else:

                count = 1

            # Entire array fits condition
            if count == N:

                return True

        # Single element array
        return N == 1