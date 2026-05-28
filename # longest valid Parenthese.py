# ============================
# PLATFORM:
# LeetCode
# (Problem 32 - Longest Valid Parentheses)
# ============================

# ============================
# PROBLEM:
# Given a string containing:
#
#     '(' and ')'
#
# Find the length of the
# longest valid (well-formed)
# parentheses substring.
#
# Example:
#
# Input:
# s = "(()"
#
# Output:
# 2
#
# Explanation:
# "()"
#
# Example:
#
# Input:
# s = ")()())"
#
# Output:
# 4
#
# Explanation:
# "()()"
# ============================

# ============================
# APPROACH:
#
# TWO PASS GREEDY SCAN
#
# Pass 1:
# Left → Right
#
# Count:
#
# left  -> '('
# right -> ')'
#
# Cases:
#
# 1. left == right
#       valid substring found
#
# 2. right > left
#       invalid
#       reset counters
#
# ----------------------------
#
# Pass 2:
# Right → Left
#
# Needed because:
#
# strings like:
#
# "(()"
#
# are not fully handled
# in left-to-right scan.
#
# Reset when:
#
# left > right
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:

    def longestValidParentheses(
        self,
        s: str
    ) -> int:

        # Counters
        left = 0
        right = 0

        # Maximum valid length
        max_length = 0

        # ====================
        # LEFT → RIGHT
        # ====================
        for x in s:

            if x == '(':

                left += 1

            else:

                right += 1

            # Valid substring
            if left == right:

                max_length = max(
                    max_length,
                    left + right
                )

            # Too many closing brackets
            elif right > left:

                left = right = 0

        # Reset counters
        left = right = 0

        # ====================
        # RIGHT → LEFT
        # ====================
        for x in s[::-1]:

            if x == '(':

                left += 1

            else:

                right += 1

            # Valid substring
            if left == right:

                max_length = max(
                    max_length,
                    left + right
                )

            # Too many opening brackets
            elif left > right:

                left = right = 0

        return max_length