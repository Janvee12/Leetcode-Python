# ============================
# PLATFORM:
# LeetCode (Problem 20 - Valid Parentheses)
# ============================

# ============================
# PROBLEM:
# Given a string s containing:
#
#     '(', ')', '{', '}', '[' and ']'
#
# determine if the input string is valid.
#
# A string is valid if:
#
# 1. Open brackets are closed
#    by the same type of brackets.
#
# 2. Open brackets are closed
#    in the correct order.
#
# 3. Every closing bracket
#    has a matching opening bracket.
#
# Example:
# Input:
# s = "()[]{}"
#
# Output:
# True
#
# Example:
# Input:
# s = "(]"
#
# Output:
# False
# ============================

# ============================
# APPROACH:
#
# Use STACK data structure.
#
# Steps:
#
# 1. Create mapping:
#
#       closing -> opening
#
# 2. Traverse characters:
#
#    a) If opening bracket:
#          push into stack
#
#    b) If closing bracket:
#          check stack top
#
#          - if matches:
#                pop
#
#          - otherwise:
#                invalid
#
# 3. At the end:
#
#    - empty stack → valid
#    - non-empty stack → invalid
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# → stack storage
# ============================

class Solution:

    def isValid(self, s: str) -> bool:

        # Stack for opening brackets
        stack = []

        # Mapping:
        # closing bracket -> opening bracket
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Traverse string
        for c in s:

            # If closing bracket
            if c in closeToOpen:

                # Check top of stack
                if stack and stack[-1] == closeToOpen[c]:

                    stack.pop()

                else:
                    return False

            # Opening bracket
            else:

                stack.append(c)

        # Valid if stack is empty
        return True if not stack else False