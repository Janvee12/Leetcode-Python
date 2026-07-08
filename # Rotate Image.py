# ============================
# PLATFORM:
# LeetCode 48
# PROBLEM:
# Rotate Image
# ============================

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left = 0
        right = len(matrix) - 1

        # Process one layer at a time
        while left < right:

            for i in range(right - left):

                top = left
                bottom = right

                # Save top-left value
                top_left = matrix[top][left + i]

                # Bottom-left -> Top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom-right -> Bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Top-right -> Bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Saved Top-left -> Top-right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1