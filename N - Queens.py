# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# N-Queens
# ============================

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # Track occupied columns and diagonals
        columns = set()
        positive_diagonal = set()
        negative_diagonal = set()

        result = []
        board = [["."] * n for _ in range(n)]

        # Backtracking function
        def backtrack(row):

            # All queens are placed successfully
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in every column
            for col in range(n):

                if (
                    col in columns
                    or (row + col) in positive_diagonal
                    or (row - col) in negative_diagonal
                ):
                    continue

                # Place the queen
                columns.add(col)
                positive_diagonal.add(row + col)
                negative_diagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                # Remove the queen (Backtrack)
                columns.remove(col)
                positive_diagonal.remove(row + col)
                negative_diagonal.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result