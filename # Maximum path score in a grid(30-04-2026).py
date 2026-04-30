# ============================
# PLATFORM:
# LeetCode (Dynamic Programming - 3D Grid DP)
# ============================

# ============================
# PROBLEM (LeetCode - Maximum Path Score with K Constraints):
#
# You are given a grid of size n x m and an integer k.
#
# You start at cell (0, 0) and want to reach (n-1, m-1).
#
# You can only move:
#   → Right
#   ↓ Down
#
# Each cell contains an integer value.
#
# Constraint:
# - You are allowed to include at most k non-zero cells in your path.
#
# Goal:
# Return the maximum sum of values you can collect on a valid path.
# If it is not possible to reach the destination, return -1.
#
# ============================
# NOTE:
# This is a variant of "Maximum Path Sum in Grid" using 3D DP.
# ============================

# ============================
# APPROACH:
#
# We use Dynamic Programming (3D DP):
#
# dp[i][j][c] = maximum sum to reach cell (i, j)
#               using c non-zero cells so far.
#
# Steps:
# 1. Initialize dp with -infinity.
# 2. Set dp[0][0][0] = 0.
# 3. Traverse grid.
# 4. From each cell, try moving right and down.
# 5. If next cell is non-zero, increase count c by 1.
# 6. Only update if c ≤ k.
# 7. Final answer = max(dp[n-1][m-1][0..k])
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * m * k)
#
# SPACE COMPLEXITY:
# O(n * m * k)
# ============================

from math import inf
from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        n = len(grid)
        m = len(grid[0])

        dp = [[[-inf] * (k + 1) for _ in range(m)] for _ in range(n)]

        dp[0][0][0] = 0

        for i in range(n):
            for j in range(m):
                for c in range(k + 1):

                    if dp[i][j][c] == -inf:
                        continue

                    # Move Down
                    if i + 1 < n:
                        val = grid[i + 1][j]
                        nc = c + (1 if val != 0 else 0)

                        if nc <= k:
                            dp[i + 1][j][nc] = max(
                                dp[i + 1][j][nc],
                                dp[i][j][c] + val
                            )

                    # Move Right
                    if j + 1 < m:
                        val = grid[i][j + 1]
                        nc = c + (1 if val != 0 else 0)

                        if nc <= k:
                            dp[i][j + 1][nc] = max(
                                dp[i][j + 1][nc],
                                dp[i][j][c] + val
                            )

        ans = max(dp[n - 1][m - 1])

        return ans if ans != -inf else -1