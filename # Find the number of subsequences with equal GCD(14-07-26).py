# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Find the Number of Subsequences With Equal GCD
# ============================

from typing import List
from functools import cache
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10**9 + 7

        # dp(index, gcd_first, gcd_second)
        @cache
        def dp(index, gcd_first, gcd_second):

            # All elements have been processed
            if index == len(nums):
                return 1 if gcd_first == gcd_second else 0

            total = 0

            # Skip the current element
            total = (total + dp(index + 1, gcd_first, gcd_second)) % MOD

            # Add the current element to the first subsequence
            total = (
                total
                + dp(index + 1, gcd(gcd_first, nums[index]), gcd_second)
            ) % MOD

            # Add the current element to the second subsequence
            total = (
                total
                + dp(index + 1, gcd_first, gcd(gcd_second, nums[index]))
            ) % MOD

            return total

        # Exclude the case where both subsequences are empty
        return (dp(0, 0, 0) - 1) % MOD