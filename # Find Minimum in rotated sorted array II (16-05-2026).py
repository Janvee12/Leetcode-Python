# ============================
# PLATFORM:
# LeetCode (Problem 154 - Find Minimum in Rotated Sorted Array II)
# ============================

# ============================
# PROBLEM:
# Given a rotated sorted array nums
# that may contain duplicates,
# return the minimum element.
#
# Example:
# Input:
# nums = [2,2,2,0,1]
#
# Output:
# 0
#
# Example:
# Input:
# nums = [1,3,5]
#
# Output:
# 1
# ============================

# ============================
# APPROACH:
#
# Use Modified Binary Search
#
# Key Observation:
#
# - One side of the array is sorted.
# - Duplicates make comparison harder.
#
# Steps:
#
# 1. Handle edge cases:
#    - single element
#    - already sorted array
#
# 2. Use two pointers:
#       l = left
#       r = right
#
# 3. Remove duplicate values from edges
#    to avoid ambiguity.
#
# 4. Find middle index.
#
# 5. Compare nums[mid] with nums[r]:
#
#    - nums[mid] > nums[r]
#         minimum lies in right half
#
#    - otherwise
#         minimum lies in left half
#
# 6. Continue until l == r.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Average Case:
# O(log n)
#
# Worst Case:
# O(n)
# → because of duplicates
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        # Edge case:
        # only one element
        if len(nums) == 1:

            return nums[0]

        # Array already sorted
        if nums[0] < nums[-1]:

            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:

            # Skip duplicate values from left
            while l < r and nums[l] == nums[l + 1]:

                l += 1

            # Skip duplicate values from right
            while l < r and nums[r] == nums[r - 1]:

                r -= 1

            # Middle index
            mid = (l + r) // 2

            # Minimum lies in right half
            if nums[mid] > nums[r]:

                l = mid + 1

            # Minimum lies in left half
            else:

                r = mid

        return nums[l]