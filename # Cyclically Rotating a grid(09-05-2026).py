# ============================
# PLATFORM:
# LeetCode (Problem 1914 - Cyclically Rotating a Grid)
# ============================

# ============================
# PROBLEM:
# You are given an m x n matrix (grid) and an integer k.
#
# Rotate each layer of the grid counter-clockwise by k positions.
#
# A layer means:
# - outer boundary
# - inner boundary
# - and so on...
#
# Return the rotated grid.
#
# Example:
# Input:
# grid = [
#   [40,10],
#   [30,20]
# ]
# k = 1
#
# Output:
# [
#   [10,20],
#   [40,30]
# ]
# ============================

# ============================
# APPROACH:
#
# For each layer:
#
# 1. Extract all elements of the layer
#    in clockwise traversal order.
#
# 2. Rotate the extracted list:
#       items = items[k:] + items[:k]
#
# 3. Put rotated values back into grid
#    using same traversal order.
#
# Layers processed:
# - Outer layer
# - Inner layer
# - ...
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(m * n)
# → Every element visited once
#
# SPACE COMPLEXITY:
# O(m * n)
# → Temporary storage for layers
# ============================

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])

        # Number of layers
        for layer in range(min(n // 2, m // 2)):

            items = []

            # ============================
            # Extract layer elements
            # ============================

            # Top row
            for j in range(layer, m - layer):
                items.append(grid[layer][j])

            # Right column
            for i in range(layer + 1, n - layer):
                items.append(grid[i][m - layer - 1])

            # Bottom row
            for j in range(m - layer - 2, layer - 1, -1):
                items.append(grid[n - layer - 1][j])

            # Left column
            for i in range(n - layer - 2, layer, -1):
                items.append(grid[i][layer])

            # ============================
            # Rotate layer
            # ============================

            nk = k % len(items)

            # Counter-clockwise rotation
            items = items[nk:] + items[:nk]

            # ============================
            # Put rotated values back
            # ============================

            idx = 0

            # Top row
            for j in range(layer, m - layer):
                grid[layer][j] = items[idx]
                idx += 1

            # Right column
            for i in range(layer + 1, n - layer):
                grid[i][m - layer - 1] = items[idx]
                idx += 1

            # Bottom row
            for j in range(m - layer - 2, layer - 1, -1):
                grid[n - layer - 1][j] = items[idx]
                idx += 1

            # Left column
            for i in range(n - layer - 2, layer, -1):
                grid[i][layer] = items[idx]
                idx += 1

        return grid