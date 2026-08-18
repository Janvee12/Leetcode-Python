# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Unique Paths II
# ============================

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # Initialize DP array
        dp = [0] * cols
        dp[cols - 1] = 1

        # Traverse the grid from bottom-right to top-left
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):

                # Obstacle blocks all paths
                if grid[row][col]:
                    dp[col] = 0

                # Add paths from the right cell
                elif col + 1 < cols:
                    dp[col] = dp[col] + dp[col + 1]

        return dp[0]