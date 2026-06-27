# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 54. Spiral Matrix
# ============================

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        # Boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # Traverse Left → Right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse Top → Bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if matrix still remains
            if not (left < right and top < bottom):
                break

            # Traverse Right → Left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse Bottom → Top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res