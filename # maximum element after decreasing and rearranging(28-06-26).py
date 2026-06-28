# ============================
# PLATFORM:
# LeetCode 1846
# PROBLEM:
# Maximum Element After Decreasing and Rearranging
# ============================

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(
        self,
        arr: List[int]
    ) -> int:

        # Sort the array
        arr.sort()

        prev = 0

        for n in arr:
            # Current element can be at most prev + 1
            prev = min(prev + 1, n)

        return prev