# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Shift 2D Grid
# ============================

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows, cols = len(grid), len(grid[0])

        # Convert a 2D position to a 1D index
        def position_to_index(row, col):
            return row * cols + col

        # Convert a 1D index back to a 2D position
        def index_to_position(index):
            return [index // cols, index % cols]

        # Initialize the shifted grid
        result = [[0] * cols for _ in range(rows)]

        # Place each element in its new position
        for row in range(rows):
            for col in range(cols):

                new_index = (position_to_index(row, col) + k) % (rows * cols)
                new_row, new_col = index_to_position(new_index)

                result[new_row][new_col] = grid[row][col]

        return result