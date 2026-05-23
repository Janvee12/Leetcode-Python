# ============================
# PLATFORM:
# LeetCode
# (Problem 27 - Remove Element)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums
# and an integer val,
# remove all occurrences of val
# in-place.
#
# Return the number of elements
# not equal to val.
#
# The first k elements of nums
# should contain the remaining elements.
#
# Order of elements may change.
#
# Example:
#
# Input:
# nums = [3,2,2,3]
# val = 3
#
# Output:
# 2
#
# nums becomes:
# [2,2,_,_]
#
# Example:
#
# Input:
# nums = [0,1,2,2,3,0,4,2]
# val = 2
#
# Output:
# 5
#
# nums becomes:
# [0,1,3,0,4,_,_,_]
# ============================

# ============================
# APPROACH:
#
# Use TWO POINTERS
#
# k -> position where
#      next valid element
#      should be placed
#
# Traverse array:
#
# - If nums[i] != val:
#
#       nums[k] = nums[i]
#       k += 1
#
# - Ignore elements equal to val
#
# Return k at the end.
#
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

    def removeElement(
        self,
        nums: List[int],
        val: int
    ) -> int:

        # Position for valid elements
        k = 0

        # Traverse array
        for i in range(len(nums)):

            # Keep non-val elements
            if nums[i] != val:

                nums[k] = nums[i]

                k += 1

        # Number of remaining elements
        return k