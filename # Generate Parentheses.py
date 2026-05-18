# ============================
# PLATFORM:
# LeetCode (Problem 22 - Generate Parentheses)
# ============================

# ============================
# PROBLEM:
# Given an integer n,
# generate all combinations
# of well-formed parentheses.
#
# Example:
# Input:
# n = 3
#
# Output:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# ============================

# ============================
# APPROACH:
#
# Use BACKTRACKING
#
# Rules:
#
# 1. Number of opening brackets
#    cannot exceed n.
#
# 2. Number of closing brackets
#    cannot exceed opening brackets.
#
# Steps:
#
# - Add '(' if openN < n
#
# - Add ')' if closedN < openN
#
# - When:
#
#       openN == closedN == n
#
#   we found a valid combination.
#
# ============================

# ============================
# BACKTRACKING IDEA:
#
# Build string step-by-step,
# then undo choices using pop().
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(4^n / √n)
#
# Catalan Number complexity
#
# SPACE COMPLEXITY:
# O(n)
# → recursion stack
# ============================

class Solution:

    def generateParenthesis(self, n):

        # Current parentheses stack
        stack = []

        # Final answer
        res = []

        # Backtracking function
        def backtrack(openN, closedN):

            # Valid combination found
            if openN == closedN == n:

                res.append("".join(stack))

                return

            # Add opening bracket
            if openN < n:

                stack.append("(")

                backtrack(openN + 1, closedN)

                stack.pop()

            # Add closing bracket
            if closedN < openN:

                stack.append(")")

                backtrack(openN, closedN + 1)

                stack.pop()

        # Start recursion
        backtrack(0, 0)

        return res