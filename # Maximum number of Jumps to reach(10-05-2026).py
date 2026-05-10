# ============================
# PLATFORM:
# LeetCode (Problem 2770 - Maximum Number of Jumps to Reach the Last Index)
# ============================

# ============================
# PROBLEM:
# You are given:
# - an integer array nums
# - an integer target
#
# You start at index 0.
#
# You can jump from index i to j if:
#
#     -target <= nums[j] - nums[i] <= target
#
# Task:
# Return the maximum number of jumps needed
# to reach the last index.
#
# If it is impossible to reach the last index,
# return -1.
#
# Example:
# Input:
# nums = [1,3,6,4,1,2]
# target = 2
#
# Output:
# 3
# ============================

# ============================
# APPROACH:
#
# Dynamic Programming
#
# dp[i] =
# maximum jumps needed to reach index i
#
# Initialization:
# dp[0] = 0
# (starting point)
#
# Transition:
#
# For every pair (i, j):
#
# If:
#   abs(nums[j] - nums[i]) <= target
#
# Then:
#   dp[j] = max(dp[j], dp[i] + 1)
#
# Final answer:
# dp[n-1]
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
# → nested loops
#
# SPACE COMPLEXITY:
# O(n)
# → dp array
# ============================

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        n = len(nums)

        # dp[i] = max jumps to reach i
        dp = [-1] * n

        # Starting index
        dp[0] = 0

        # Traverse all indices
        for j in range(n):

            for i in range(j):

                # Check valid jump
                if (dp[i] != -1 and
                    -target <= nums[j] - nums[i] <= target):

                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]