# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Spiral Matrix
# ============================

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        # Define the boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Traverse the matrix in spiral order
        while left < right and top < bottom:

            # Traverse from left to right
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1

            # Traverse from top to bottom
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])
            right -= 1

            # Check if there is any row or column left
            if not (left < right and top < bottom):
                break

            # Traverse from right to left
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][col])
            bottom -= 1

            # Traverse from bottom to top
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

        return result