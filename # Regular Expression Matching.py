# ============================
# PLATFORM:
# LeetCode (Problem 10 - Regular Expression Matching)
# ============================

# ============================
# PROBLEM:
# Given a string s and a pattern p, implement regular expression matching
# with support for:
#
# '.' → matches any single character
# '*' → matches zero or more of the preceding element
#
# The matching should cover the entire string.
#
# Example:
# Input: s = "aa", p = "a*"
# Output: True
#
# Input: s = "ab", p = ".*"
# Output: True
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: False
# ============================

# ============================
# APPROACH:
#
# We use recursion (DFS).
#
# Define:
# dfs(i, j) → returns True if s[i:] matches p[j:]
#
# Steps:
# 1. Base Case:
#    - If both string and pattern are fully matched → True
#    - If pattern ends but string not → False
#
# 2. Check current match:
#    match = (s[i] == p[j] or p[j] == '.')
#
# 3. If next character in pattern is '*':
#    Two choices:
#    a) Skip "x*" → dfs(i, j+2)
#    b) Use it if match → dfs(i+1, j)
#
# 4. If no '*':
#    - Move both pointers if match
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(2^(m+n)) in worst case (without memoization)
#
# OPTIMIZED (with memoization):
# O(m * n)
#
# SPACE COMPLEXITY:
# O(m * n) recursion + memo
# ============================

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)   # memoization to optimize
        def dfs(i, j):

            # Base case
            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            # Check current match
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Handle '*'
            if (j + 1) < len(p) and p[j + 1] == "*":
                return (
                    dfs(i, j + 2) or        # skip "x*"
                    (match and dfs(i + 1, j))  # use "x*"
                )

            # Normal match
            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)