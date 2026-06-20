# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 48. Rotate Image
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an n × n matrix,
# rotate the image by 90°
# clockwise.
#
# The rotation must be done
# in-place.
#
# Do not create another matrix.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Rotate layer by layer.
#
# For every layer:
#
# top
# right
# bottom
# left
#
# Perform a 4-way swap.
#
# Each element moves:
#
# left   → top
# bottom → left
# right  → bottom
# top    → right
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n²)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything.
        Modify matrix in-place.
        """

        left = 0
        right = len(matrix) - 1

        # Process every layer
        while left < right:

            for i in range(right - left):

                top = left
                bottom = right

                # Save top-left value
                top_left = matrix[top][left + i]

                # Left -> Top
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom -> Left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Right -> Bottom
                matrix[bottom][right - i] = matrix[top + i][right]

                # Top -> Right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1