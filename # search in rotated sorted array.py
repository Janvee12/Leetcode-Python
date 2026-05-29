# ============================
# PLATFORM:
# LeetCode
# (Problem 33 - Search in Rotated Sorted Array)
# ============================

# ============================
# PROBLEM:
# Given a rotated sorted array
# and a target value,
#
# return the index of target.
#
# If target does not exist,
# return -1.
#
# Array contains DISTINCT values.
#
# Example:
#
# Input:
# nums = [4,5,6,7,0,1,2]
# target = 0
#
# Output:
# 4
#
# Example:
#
# Input:
# nums = [4,5,6,7,0,1,2]
# target = 3
#
# Output:
# -1
# ============================

# ============================
# APPROACH:
#
# Modified Binary Search
#
# Key Observation:
#
# At least one half
# is always sorted.
#
# Steps:
#
# 1. Find middle element.
#
# 2. Check which half is sorted:
#
#       left half
#       OR
#       right half
#
# 3. Decide whether target lies
#    inside the sorted half.
#
# 4. Move pointers accordingly.
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

    def search(
        self,
        nums: List[int],
        target: int
    ) -> int:

        # Binary search pointers
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            # Target found
            if target == nums[mid]:

                return mid

            # ====================
            # Left half is sorted
            # ====================
            if nums[l] <= nums[mid]:

                # Target NOT in left half
                if (
                    target > nums[mid]
                    or target < nums[l]
                ):

                    l = mid + 1

                else:

                    r = mid - 1

            # ====================
            # Right half is sorted
            # ====================
            else:

                # Target NOT in right half
                if (
                    target < nums[mid]
                    or target > nums[r]
                ):

                    r = mid - 1

                else:

                    l = mid + 1

        # Target not found
        return -1