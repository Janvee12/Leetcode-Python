# ============================
# PLATFORM:
# LeetCode
# (Problem 36 - Valid Sudoku)
# ============================

# ============================
# PROBLEM
# ============================
#
# Determine whether a
# 9 × 9 Sudoku board is valid.
#
# Rules:
#
# 1. Each row must contain
#    digits 1-9 without repeats.
#
# 2. Each column must contain
#    digits 1-9 without repeats.
#
# 3. Each 3 × 3 sub-box must
#    contain digits 1-9
#    without repeats.
#
# Note:
#
# Only the filled cells need
# to be validated.
#
# '.' represents an empty cell.
#
# ============================

# ============================
# APPROACH
# ============================
#
# Use three hash maps:
#
# rows[r]
#     -> digits seen in row r
#
# cols[c]
#     -> digits seen in column c
#
# squares[(r//3, c//3)]
#     -> digits seen in the
#        corresponding 3×3 box
#
# For every filled cell:
#
# 1. Check if digit already
#    exists in:
#
#    - current row
#    - current column
#    - current box
#
# 2. If yes:
#
#       return False
#
# 3. Otherwise insert digit
#    into all three sets.
#
# If traversal completes,
# board is valid.
#
# ============================

from typing import List
import collections

class Solution:

    def isValidSudoku(
        self,
        board: List[List[str]]
    ) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):

            for c in range(9):

                value = board[r][c]

                if value == ".":

                    continue

                # Duplicate found
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[(r // 3, c // 3)]
                ):

                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)

        return True