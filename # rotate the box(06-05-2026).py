# ============================
# PLATFORM:
# LeetCode (Problem 1861 - Rotating the Box)
# ============================

# ============================
# PROBLEM:
# You are given a box represented as a 2D grid:
#   '#' → stone
#   '*' → obstacle
#   '.' → empty space
#
# Rules:
# 1. Stones fall to the right due to gravity (until blocked by obstacle or wall).
# 2. After applying gravity, rotate the box 90° clockwise.
#
# Return the final rotated box.
#
# Example:
# Input:
# [["#",".","*","."],
#  ["#","#","*","."]]
#
# Output:
# [[".","#"],
#  ["#","#"],
#  ["*","*"],
#  [".","."]]
# ============================

# ============================
# APPROACH:
#
# Step 1: Simulate gravity (right side)
# - Traverse each row from right → left
# - Keep pointer 'i' = position where next stone will fall
#
# Cases:
# - '#' (stone):
#     → move to position 'i'
#     → decrement i
#
# - '*' (obstacle):
#     → place obstacle directly
#     → reset i = position before obstacle
#
# Step 2: Rotate matrix
# - New matrix size = COLS x ROWS
# - Mapping:
#     res[new_row][new_col] = original[row][col]
#     → res[c][ROWS - r - 1]
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(m * n)
# → traverse each cell once
#
# SPACE COMPLEXITY:
# O(m * n)
# → result matrix
# ============================

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        ROWS, COLS = len(box), len(box[0])

        # Result matrix after rotation
        res = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):

            i = COLS - 1  # position where stone will fall

            for c in reversed(range(COLS)):

                if box[r][c] == "#":
                    # place stone at correct position after gravity
                    res[i][ROWS - r - 1] = "#"
                    i -= 1

                elif box[r][c] == "*":
                    # place obstacle directly
                    res[c][ROWS - r - 1] = "*"
                    # reset pointer before obstacle
                    i = c - 1

        return res