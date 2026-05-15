# ============================
# PLATFORM:
# LeetCode (Problem 153 - Find Minimum in Rotated Sorted Array)
# ============================

# ============================
# PROBLEM:
# Given a sorted array that has been rotated
# between 1 and n times,
# find the minimum element.
#
# Constraints:
# - All elements are unique
# - Solution must run in O(log n)
#
# Example:
# Input:
# nums = [3,4,5,1,2]
#
# Output:
# 1
#
# Example:
# Input:
# nums = [4,5,6,7,0,1,2]
#
# Output:
# 0
# ============================

# ============================
# APPROACH:
#
# Use Binary Search
#
# Key Observation:
#
# In a rotated sorted array,
# one half is always sorted.
#
# Steps:
#
# 1. Maintain:
#       left pointer (l)
#       right pointer (r)
#
# 2. If current range is already sorted:
#
#       nums[l] < nums[r]
#
#    then nums[l] is minimum.
#
# 3. Find middle index:
#
#       m = (l + r) // 2
#
# 4. Decide search direction:
#
#    - If nums[m] >= nums[l]
#         minimum lies in right half
#
#    - Else
#         minimum lies in left half
#
# 5. Keep updating minimum answer.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(log n)
# → Binary Search
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        # Initial minimum
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:

            # If subarray is sorted
            if nums[l] < nums[r]:

                res = min(res, nums[l])

                break

            # Middle index
            m = (l + r) // 2

            # Update minimum
            res = min(res, nums[m])

            # Left portion sorted
            if nums[m] >= nums[l]:

                l = m + 1

            # Right portion sorted
            else:

                r = m - 1

        return res