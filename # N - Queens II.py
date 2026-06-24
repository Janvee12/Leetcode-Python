# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 52. N-Queens II
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an integer n, return the
# number of distinct solutions to
# the n-queens puzzle.
#
# Unlike N-Queens I, we only need
# the count of solutions, not the
# actual board configurations.
#
# ============================

class Solution:
    def totalNQueens(self, n: int) -> int:

        # Columns already occupied
        col = set()

        # Main diagonals (r + c)
        posDiag = set()

        # Anti-diagonals (r - c)
        negDiag = set()

        res = 0

        def backtrack(r):
            nonlocal res

            # All queens placed successfully
            if r == n:
                res += 1
                return

            # Try placing queen in every column
            for c in range(n):

                # Queen attacks another queen
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

                # Backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)

        return res