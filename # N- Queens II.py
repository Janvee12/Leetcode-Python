# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 52. N-Queens II
# ============================

class Solution:
    def totalNQueens(self, n: int) -> int:

        # Stores occupied columns
        col = set()

        # Stores positive diagonals (row + col)
        posDiag = set()

        # Stores negative diagonals (row - col)
        negDiag = set()

        # Total number of solutions
        res = 0

        def backtrack(r):
            nonlocal res

            # All queens placed successfully
            if r == n:
                res += 1
                return

            # Try placing queen in every column
            for c in range(n):

                # Position is unsafe
                if (c in col or
                    (r + c) in posDiag or
                    (r - c) in negDiag):
                    continue

                # Place queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Move to next row
                backtrack(r + 1)

                # Remove queen (Backtrack)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)

        return res