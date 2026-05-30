# ============================
# PLATFORM:
# LeetCode
# (Problem 34 - Find First and Last Position of Element in Sorted Array)
# ============================

# ============================
# PROBLEM:
# Given a sorted array nums
# and a target value,
#
# return:
#
# [first_position, last_position]
#
# If target does not exist,
# return:
#
# [-1, -1]
#
# Example:
#
# Input:
# nums = [5,7,7,8,8,10]
# target = 8
#
# Output:
# [3,4]
#
# Example:
#
# Input:
# nums = [5,7,7,8,8,10]
# target = 6
#
# Output:
# [-1,-1]
# ============================

# ============================
# APPROACH:
#
# Use Binary Search twice.
#
# 1. Find LEFTMOST occurrence
#    of target.
#
# 2. Find RIGHTMOST occurrence
#    of target.
#
# Whenever target is found:
#
# - store index
#
# - continue searching:
#
#   left side  -> first position
#
#   right side -> last position
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

    def searchRange(
        self,
        nums: List[int],
        target: int
    ) -> List[int]:

        left = self.binSearch(
            nums,
            target,
            True
        )

        right = self.binSearch(
            nums,
            target,
            False
        )

        return [left, right]

    # ========================
    # Binary Search
    # ========================
    def binSearch(
        self,
        nums,
        target,
        leftBias
    ):

        l, r = 0, len(nums) - 1

        ans = -1

        while l <= r:

            m = (l + r) // 2

            if target > nums[m]:

                l = m + 1

            elif target < nums[m]:

                r = m - 1

            else:

                ans = m

                # Search further left
                if leftBias:

                    r = m - 1

                # Search further right
                else:

                    l = m + 1

        return ans