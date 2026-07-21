# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Spiral Matrix II
# ============================

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define the boundaries
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        current = 1

        # Fill the matrix in spiral order
        while left <= right:

            # Fill the top row
            for col in range(left, right + 1):
                matrix[top][col] = current
                current += 1
            top += 1

            # Fill the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = current
                current += 1
            right -= 1

            # Fill the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = current
                current += 1
            bottom -= 1

            # Fill the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = current
                current += 1
            left += 1

        return matrix