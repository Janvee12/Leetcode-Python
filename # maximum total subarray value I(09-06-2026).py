# ============================
# PLATFORM:
# LeetCode / Coding Problem
# (Max Total Value)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given an array nums and an integer k.
#
# You need to compute:
#
#   (maximum element - minimum element) * k
#
# ============================
# APPROACH:
# ============================
#
# Instead of sorting (O(n log n)),
# we simply find:
#
#   max element
#   min element
#
# Then apply formula.
#
# ============================

from typing import List
from math import inf

class Solution:

    def maxTotalValue(self, nums: List[int], k: int) -> int:

        # ============================
        # STEP 1: Initialize
        # ============================
        mx, mn = -inf, inf

        # ============================
        # STEP 2: Find max and min
        # ============================
        for n in nums:
            mx = max(mx, n)
            mn = min(mn, n)

        # ============================
        # STEP 3: Apply formula
        # ============================
        return (mx - mn) * k