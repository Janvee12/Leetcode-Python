# ============================
# PLATFORM:
# LeetCode (Problem 1674 - Minimum Moves to Make Array Complementary)
# ============================

# ============================
# PROBLEM:
# You are given an array nums of even length n
# and an integer limit.
#
# In one move, you can:
# - Change any number in nums to any value in [1, limit]
#
# Goal:
# Make the array complementary:
# For every pair (nums[i], nums[n-1-i]),
# their sum must be the same.
#
# Task:
# Return the minimum number of moves required.
#
# ============================
# EXAMPLE:
# Input:
# nums = [1,2,4,3], limit = 4
#
# Output:
# 1
# ============================

# ============================
# APPROACH:
#
# We process pairs:
#     (a, b) = (nums[i], nums[n-i-1])
#
# For each pair:
# we analyze possible sums:
#
# 1 move range contribution:
#     [min(a,b)+1, max(a,b)+limit]
#
# 0 move contribution:
#     sum = a + b
#
# --------------------------------
# Use DIFFERENCE ARRAY:
#
# diff[x] → change in cost at sum x
#
# We:
# - decrease cost in valid range
# - track exact sum frequencies
#
# Then compute prefix to find:
# minimum moves for each possible sum
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + limit)
#
# SPACE COMPLEXITY:
# O(limit)
# ============================

from collections import defaultdict
import sys
from typing import List

class Solution:

    def minMoves(self, nums: List[int], limit: int) -> int:

        ssum = defaultdict(int)   # count of exact pair sums
        diff = defaultdict(int)   # difference array for range updates

        n = len(nums)

        # Process pairs
        for i in range(n // 2):

            a = nums[i]
            b = nums[n - i - 1]

            mmin = min(a, b)
            mmax = max(a, b)

            # Range where 1 move is enough
            left = mmin + 1
            right = mmax + limit

            # Update difference array
            diff[left] -= 1
            diff[right + 1] += 1

            # Count current exact sum (0 move case)
            ssum[a + b] += 1

        ans = sys.maxsize
        cur = n  # initially all pairs need 2 moves

        # Try all possible target sums
        for s in range(2, max(ssum) + 1):

            cur += diff[s]

            # total operations needed
            ans = min(ans, cur - ssum[s])

        return ans