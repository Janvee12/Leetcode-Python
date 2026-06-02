# ============================
# PLATFORM:
# LeetCode
# (Problem 37 - Sudoku Solver)
# ============================

# ============================
# PROBLEM
# ============================
#
# Given a partially filled
# 9 x 9 Sudoku board,
# fill all empty cells.
#
# Rules:
#
# 1. Each row contains
#    digits 1-9 exactly once.
#
# 2. Each column contains
#    digits 1-9 exactly once.
#
# 3. Each 3x3 box contains
#    digits 1-9 exactly once.
#
# Empty cells are represented
# by ".".
#
# Modify the board in-place.
#
# ============================

# ============================
# APPROACH
# ============================
#
# BACKTRACKING
#
# For every empty cell:
#
# Try digits:
#
#     1 -> 9
#
# If a digit is valid:
#
#     place it
#
#     recursively solve
#     remaining board
#
# If recursion fails:
#
#     remove digit
#
#     try next digit
#
# If all cells are filled:
#
#     solution found
#
# ============================

from typing import List

class Solution:

    def solveSudoku(
        self,
        board: List[List[str]]
    ) -> None:

        # ====================
        # Store used digits
        # ====================

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # ====================
        # Initialize sets
        # ====================

        for i in range(9):
            for j in range(9):

                if board[i][j] != ".":

                    num = board[i][j]

                    rows[i].add(num)
                    cols[j].add(num)

                    box_index = (
                        (i // 3) * 3
                        + j // 3
                    )

                    boxes[box_index].add(num)

        # ====================
        # Backtracking
        # ====================

        def solve():

            for i in range(9):

                for j in range(9):

                    # Find empty cell
                    if board[i][j] == ".":

                        box_index = (
                            (i // 3) * 3
                            + j // 3
                        )

                        # Try digits 1..9
                        for num in "123456789":

                            if (
                                num not in rows[i]
                                and num not in cols[j]
                                and num not in boxes[box_index]
                            ):

                                # Place digit
                                board[i][j] = num

                                rows[i].add(num)
                                cols[j].add(num)
                                boxes[box_index].add(num)

                                # Recurse
                                if solve():
                                    return True

                                # Backtrack
                                board[i][j] = "."

                                rows[i].remove(num)
                                cols[j].remove(num)
                                boxes[box_index].remove(num)

                        # No valid digit
                        return False

            # Board solved
            return True

        solve()