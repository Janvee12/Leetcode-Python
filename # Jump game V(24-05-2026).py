# ============================
# PLATFORM:
# LeetCode
# (Problem 1340 - Jump Game V)
# ============================

# ============================
# PROBLEM:
# You are given:
#
#     arr -> heights
#     d   -> maximum jump distance
#
# From index i,
# you can jump:
#
# - left
# - right
#
# Conditions:
#
# 1. Distance <= d
#
# 2. arr[j] < arr[i]
#
# 3. Cannot jump over
#    an element >= arr[i]
#
# Task:
# Return maximum number
# of indices you can visit.
#
# Example:
#
# Input:
# arr = [6,4,14,6,8,13,9,7,10,6,12]
# d = 2
#
# Output:
# 4
# ============================

# ============================
# APPROACH:
#
# DFS + MEMOIZATION (DP)
#
# Let:
#
# dp[i] =
# maximum jumps starting from i
#
# For every index:
#
# - Explore left up to distance d
# - Explore right up to distance d
#
# Stop exploration if:
#
#     arr[j] >= arr[i]
#
# because jumping beyond
# becomes impossible.
#
# Recurrence:
#
# dp[i] =
# 1 + max(dfs(valid neighbors))
#
# ============================

# ============================
# WHY MEMOIZATION?
#
# Without memoization:
# repeated DFS calls occur.
#
# dp stores already computed results.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * d)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from typing import List

class Solution:

    def maxJumps(
        self,
        arr: List[int],
        d: int
    ) -> int:

        n = len(arr)

        # Memoization array
        dp = [0] * n

        # DFS function
        def dfs(i):

            # Already computed
            if dp[i]:

                return dp[i]

            # At least current index
            ans = 1

            # ====================
            # Check LEFT
            # ====================
            for j in range(
                i - 1,
                max(-1, i - d - 1),
                -1
            ):

                # Cannot jump further
                if arr[j] >= arr[i]:

                    break

                ans = max(ans, 1 + dfs(j))

            # ====================
            # Check RIGHT
            # ====================
            for j in range(
                i + 1,
                min(n, i + d + 1)
            ):

                # Cannot jump further
                if arr[j] >= arr[i]:

                    break

                ans = max(ans, 1 + dfs(j))

            # Store answer
            dp[i] = ans

            return ans

        # Compute maximum among all starts
        return max(dfs(i) for i in range(n))