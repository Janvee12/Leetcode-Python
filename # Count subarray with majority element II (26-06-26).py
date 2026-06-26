# ============================
# PLATFORM:
# LeetCode Contest
# PROBLEM:
# Count Majority Subarrays
# OPTIMIZED SOLUTION
# ============================

from typing import List

class Solution:
    def countMajoritySubarrays(
        self,
        nums: List[int],
        target: int
    ) -> int:

        n = len(nums)

        # Frequency of balances
        freq = [0] * (2 * n + 1)

        # Prefix sum of frequencies
        acc = [0] * (2 * n + 1)

        # Initial balance = 0 shifted by n
        freq[n] = 1
        acc[n] = 1

        bal = n
        res = 0

        for num in nums:

            # Target contributes +1
            if num == target:
                bal += 1

            # Non-target contributes -1
            else:
                bal -= 1

            freq[bal] += 1

            acc[bal] = acc[bal - 1] + freq[bal]

            res += acc[bal - 1]

        return res