# ============================
# PLATFORM:
# LeetCode (Problem 15 - 3Sum)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums,
# return all unique triplets [nums[i], nums[j], nums[k]]
# such that:
#
#     nums[i] + nums[j] + nums[k] == 0
#
# Conditions:
# - i, j, k must be different indices
# - Result should not contain duplicate triplets
#
# Example:
# Input:
# nums = [-1,0,1,2,-1,-4]
#
# Output:
# [[-1,-1,2],[-1,0,1]]
# ============================

# ============================
# APPROACH:
#
# 1. Sort the array.
#
# 2. Fix one number nums[i].
#
# 3. Use Two Pointers:
#    - left = i + 1
#    - right = n - 1
#
# 4. Calculate:
#       total = nums[i] + nums[left] + nums[right]
#
# 5. Cases:
#    - total > 0 → move right pointer left
#    - total < 0 → move left pointer right
#    - total == 0 → valid triplet found
#
# 6. Skip duplicate values to avoid repeated triplets.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
#
# - Sorting: O(n log n)
# - Two pointer traversal: O(n^2)
#
# SPACE COMPLEXITY:
# O(1)
# → excluding output array
# ============================

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        # Step 1: Sort array
        nums.sort()

        # Step 2: Fix first number
        for i, a in enumerate(nums):

            # Skip duplicate values
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = a + nums[l] + nums[r]

                # Need smaller sum
                if total > 0:
                    r -= 1

                # Need larger sum
                elif total < 0:
                    l += 1

                # Found valid triplet
                else:

                    res.append([a, nums[l], nums[r]])

                    l += 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res