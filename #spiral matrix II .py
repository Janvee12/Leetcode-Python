# ============================
# PLATFORM:
# LeetCode 59
# PROBLEM:
# Spiral Matrix II
# ============================

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Create an n x n matrix filled with 0
        mat = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1

        val = 1

        while left <= right:

            # Left → Right
            for c in range(left, right + 1):
                mat[top][c] = val
                val += 1
            top += 1

            # Top → Bottom
            for r in range(top, bottom + 1):
                mat[r][right] = val
                val += 1
            right -= 1

            # Right → Left
            for c in range(right, left - 1, -1):
                mat[bottom][c] = val
                val += 1
            bottom -= 1

            # Bottom → Top
            for r in range(bottom, top - 1, -1):
                mat[r][left] = val
                val += 1
            left += 1

        return mat