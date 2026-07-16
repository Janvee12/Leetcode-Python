# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# GCD Sum of Prefix Maximums
# ============================

from typing import List
from math import gcd


class Solution:
    def gcdSum(self, nums: List[int]) -> int:

        n = len(nums)

        # Store prefix maximums and corresponding GCD values
        prefix_max = [nums[0]] * n
        prefix_gcd = [nums[0]] * n

        # Compute prefix maximum and GCD for each position
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
            prefix_gcd[i] = gcd(nums[i], prefix_max[i])

        # Sort the GCD values
        prefix_gcd.sort()

        # Pair smallest and largest values
        total = 0
        for i in range(n // 2):
            total += gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])

        return total