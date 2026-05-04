# ============================
# PLATFORM:
# LeetCode (Problem 48 - Rotate Image)
# ============================

# ============================
# PROBLEM:
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# IMPORTANT:
# - You must rotate the matrix in-place.
# - Do NOT use extra matrix.
#
# Example:
# Input:
# [
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ]
#
# Output:
# [
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]
# ============================

# ============================
# APPROACH:
#
# We rotate the matrix layer by layer.
#
# Steps:
# 1. Use two pointers:
#    l = left boundary
#    r = right boundary
#
# 2. For each layer:
#    - Rotate elements in groups of 4
#
# 3. For each position:
#    Perform 4-way swap:
#
#    top ← left ← bottom ← right ← top
#
# 4. Move inward:
#    l += 1
#    r -= 1
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
# → Each element is visited once
#
# SPACE COMPLEXITY:
# O(1)
# → In-place rotation
# ============================

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l = 0
        r = len(matrix) - 1

        while l < r:

            for i in range(r - l):

                top = l
                bottom = r

                # Save top-left
                topLeft = matrix[top][l + i]

                # Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Move to inner layer
            l += 1
            r -= 1


# ============================
# 🔥 ALTERNATIVE METHOD (VERY POPULAR):
#
# Step 1: Transpose matrix
# Step 2: Reverse each row
#
# Example:
# Transpose:
# [1 2 3]      [1 4 7]
# [4 5 6]  →   [2 5 8]
# [7 8 9]      [3 6 9]
#
# Reverse rows:
# [7 4 1]
# [8 5 2]
# [9 6 3]
# ============================

class SolutionAlt:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()