# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Sorted GCD Pair Queries
# ============================

from typing import List
import bisect


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        # Find the maximum value in the array
        max_value = max(nums)

        # Frequency array
        frequency = [0] * (max_value + 1)
        for num in nums:
            frequency[num] += 1

        # Count how many numbers are divisible by each value
        for divisor in range(1, max_value + 1):
            for multiple in range(divisor * 2, max_value + 1, divisor):
                frequency[divisor] += frequency[multiple]

        # Count pairs for each divisor
        for divisor in range(1, max_value + 1):
            frequency[divisor] = (
                frequency[divisor] * (frequency[divisor] - 1)
            ) // 2

        # Inclusion-Exclusion to get exact GCD counts
        for divisor in range(max_value, 0, -1):
            for multiple in range(divisor * 2, max_value + 1, divisor):
                frequency[divisor] -= frequency[multiple]

        # Prefix sum of GCD counts
        for i in range(1, max_value + 1):
            frequency[i] += frequency[i - 1]

        result = []

        # Answer each query using binary search
        for query in queries:
            gcd_value = bisect.bisect_left(frequency, query + 1)
            result.append(gcd_value)

        return result