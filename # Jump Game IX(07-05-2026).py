# ============================
# PLATFORM:
# LeetCode (Monotonic Stack / Array Processing)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums,
# build a new array res where each position stores
# the maximum propagated value after processing ranges.
#
# The algorithm uses a monotonic stack to:
# - maintain increasing values
# - merge ranges when current value is smaller
#
# Goal:
# Return the transformed array after range updates.
#
# NOTE:
# This is a stack-based range processing problem.
# ============================

# ============================
# APPROACH:
#
# We use a Monotonic Increasing Stack.
#
# Stack stores:
#   (value, left_index, right_index)
#
# Steps:
#
# 1. Traverse array from left → right.
#
# 2. For each element nums[i]:
#    - Initialize:
#         v = nums[i]
#         l = i
#         r = i
#
# 3. While stack top value > current value:
#    - Pop previous segment
#    - Merge ranges
#    - Keep maximum value
#
# 4. Push merged segment back into stack.
#
# 5. Finally:
#    - Fill result array using stored ranges.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# Explanation:
# - Each element is pushed once
# - Each element is popped once
#
# SPACE COMPLEXITY:
# O(n)
# → stack + result array
# ============================

from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # Result array
        res = [0] * n

        # Monotonic stack
        # (value, left_index, right_index)
        s = []

        for i in range(n):

            v = nums[i]
            l = i
            r = i

            # Merge larger previous values
            while s and s[-1][0] > nums[i]:

                lastv, lastl, lastr = s.pop()

                # Keep maximum value
                v = max(v, lastv)

                # Expand left boundary
                l = lastl

            # Push merged segment
            s.append((v, l, r))

        # Fill result array
        for v, l, r in s:
            for i in range(l, r + 1):
                res[i] = v

        return res