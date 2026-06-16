# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 44. Wildcard Matching
# ============================

# ============================
# PROBLEM:
#
# Given:
#   s = input string
#   p = pattern
#
# Pattern Rules:
#
# '?' → Matches exactly one character
#
# '*' → Matches any sequence
#       (including empty sequence)
#
# Return:
#   True  -> if pattern matches string
#   False -> otherwise
#
# ============================

# ============================
# APPROACH:
#
# Dynamic Programming
#
# dp[i][j] =
# True if first i characters of s
# match first j characters of p
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(m × n)
#
# SPACE COMPLEXITY:
# O(m × n)
# ============================

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        # dp[i][j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns starting with *
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Case 1: '*'
                if p[j - 1] == '*':
                    dp[i][j] = (
                        dp[i - 1][j] or
                        dp[i][j - 1]
                    )

                # Case 2: '?' or exact match
                elif (
                    p[j - 1] == '?' or
                    s[i - 1] == p[j - 1]
                ):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]