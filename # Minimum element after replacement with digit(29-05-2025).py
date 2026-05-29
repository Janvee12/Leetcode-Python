# ============================
# PLATFORM:
# LeetCode
# (Problem 3300 - Minimum Element After Replacement With Digit Sum)
# ============================

# ============================
# PROBLEM:
# Given an array nums,
# replace every number
# with the SUM of its digits.
#
# Return the minimum value
# after replacement.
#
# Example:
#
# Input:
# nums = [10, 12, 13, 14]
#
# Digit sums:
#
# 10 -> 1
# 12 -> 3
# 13 -> 4
# 14 -> 5
#
# Output:
# 1
# ============================

# ============================
# APPROACH:
#
# For every number:
#
# 1. Extract digits using:
#
#       n % 10
#
# 2. Add digits to sum.
#
# 3. Remove last digit:
#
#       n //= 10
#
# 4. Track minimum digit sum.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(n * d)
#
# d = number of digits
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from math import inf
from typing import List

class Solution:

    def minElement(
        self,
        nums: List[int]
    ) -> int:

        # Minimum digit sum
        res = inf

        # Traverse all numbers
        for n in nums:

            digit_sum = 0

            # Compute digit sum
            while n:

                digit_sum += n % 10

                n //= 10

            # Update minimum
            res = min(res, digit_sum)

        return res