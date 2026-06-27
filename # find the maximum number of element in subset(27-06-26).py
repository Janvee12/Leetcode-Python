# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 3020. Find the Maximum Number of Elements in Subset
# ============================

from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        # Count frequency of every number
        fm = defaultdict(int)
        for num in nums:
            fm[num] += 1

        # Handle number 1 separately
        ones = fm[1]

        # Number of 1's must be odd
        res = ones if ones % 2 == 1 else max(0, ones - 1)

        # Try every distinct number
        for num in fm:

            if num == 1:
                continue

            total = 0
            curr = num

            # Need at least 2 occurrences
            while curr in fm and fm[curr] >= 2:
                total += 2
                curr *= curr

            # Middle element
            if curr in fm:
                total += 1
            else:
                total -= 1

            res = max(res, total)

        return res