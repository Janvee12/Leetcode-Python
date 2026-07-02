# ============================
# PLATFORM:
# LeetCode 3286
# PROBLEM:
# Find a Safe Walk Through a Grid
# ============================

from typing import List
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m, n = len(grid), len(grid[0])

        # best[r][c] = Maximum health remaining
        # when reaching cell (r,c)
        best = [[-1] * n for _ in range(m)]

        # Health after entering the starting cell
        start_health = health - grid[0][0]

        # Cannot even stand on the first cell
        if start_health <= 0:
            return False

        best