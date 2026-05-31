# ============================
# PLATFORM:
# LeetCode
# (Problem 35 - Search Insert Position)
# ============================

# ============================
# PROBLEM:
# Given a sorted array nums
# and a target value,
#
# Return:
#
# - The index if target exists.
#
# - Otherwise the index where
#   it should be inserted to
#   keep the array sorted.
#
# Example 1:
#
# nums = [1,3,5,6]
# target = 5
#
# Output:
# 2
#
# Example 2:
#
# nums = [1,3,5,6]
# target = 2
#
# Output:
# 1
#
# Example 3:
#
# nums = [1,3,5,6]
# target = 7
#
# Output:
# 4
# ============================

# ============================
# APPROACH:
#
# Use Binary Search.
#
# If target is found:
#     return its index.
#
# Otherwise:
#     when the search ends,
#     'l' points to the
#     correct insertion index.
#
# Why?
#
# - All elements before l
#   are smaller than target.
#
# - All elements from l onward
#   are greater than target.
#
# Therefore:
#
#     return l
#
# ============================

# ============================
# DRY RUN
#
# nums = [1,3,5,6]
# target = 2
#
# l = 0, r = 3
#
# mid = 1 -> nums[1] = 3
#
# 2 < 3
# r = 0
#
# mid = 0 -> nums[0] = 1
#
# 2 > 1
# l = 1
#
# loop ends
#
# return l = 1
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def searchInsert(
        self,
        nums: List[int],
        target: int
    ) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            # Target found
            if target == nums[mid]:

                return mid

            # Search right half
            if target > nums[mid]:

                l = mid + 1

            # Search left half
            else:

                r = mid - 1

        # Correct insertion position
        return l