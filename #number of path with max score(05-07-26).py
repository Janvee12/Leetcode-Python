# ============================
# PLATFORM:
# LeetCode 1301
# PROBLEM:
# Number of Paths with Max Score
# ============================

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [maximum score from (i,j) to S,
        #             number of paths with that score]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]

        # Base Case: Start from 'S'
        dp[n - 1][n - 1] = [0, 1]

        # Traverse from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Skip Start and blocked cells
                if board[i][j] in "SX":
                    continue

                # Cell value
                val = 0 if board[i][j] == 'E' else int(board[i][j])

                best = -1
                ways = 0

                # Down, Right, Diagonal
                for ni, nj in (
                    (i + 1, j),
                    (i, j + 1),
                    (i + 1, j + 1)
                ):

                    if ni >= n or nj >= n:
                        continue

                    score, cnt = dp[ni][nj]

                    if score == -1:
                        continue

                    if score > best:
                        best = score
                        ways = cnt

                    elif score == best:
                        ways = (ways + cnt) % MOD

                if best != -1:
                    dp[i][j] = [best + val, ways]

        if dp[0][0][0] == -1:
            return [0, 0]

        return [
            dp[0][0][0],
            dp[0][0][1] % MOD
        ]