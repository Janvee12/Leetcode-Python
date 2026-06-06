# ============================
# PLATFORM:
# LeetCode
# (Left and Right Difference)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given an array nums.
#
# For each index i, compute:
#
#   |sum(left of i) - sum(right of i)|
#
# where:
# - left = elements before i
# - right = elements after i
#
# Return the result array.
#
# ============================
# APPROACH:
# ============================
#
# Instead of recomputing sums
# again and again (O(n²)),
# we use prefix sums idea.
#
# Steps:
#
# 1. Compute total sum → right side initially
#
# 2. Maintain:
#    left sum (starts 0)
#    right sum (starts total)
#
# 3. For each index:
#    - remove current from right
#    - compute difference
#    - add previous element to left
#
# ============================

from typing import List

class Solution:

    def leftRightDifference(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = []

        left = 0
        right = sum(nums)

        for i in range(n):

            # remove current element from right side
            right -= nums[i]

            # compute absolute difference
            res.append(abs(left - right))

            # add current element to left side
            left += nums[i]

        return res