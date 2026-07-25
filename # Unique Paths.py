# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Unique Paths
# ============================

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Initialize the last row with 1s
        row = [1] * n

        # Build the DP table from bottom to top
        for _ in range(m - 1):

            new_row = [1] * n

            # Fill the current row from right to left
            for col in range(n - 2, -1, -1):
                new_row[col] = new_row[col + 1] + row[col]

            row = new_row

        return row[0]