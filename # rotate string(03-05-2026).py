# ============================
# PLATFORM:
# LeetCode (Problem 796 - Rotate String)
# ============================

# ============================
# PROBLEM:
# Given two strings s and goal, return True if and only if
# s can become goal after some number of rotations.
#
# A rotation means:
# Move the first character of s to the end.
#
# Example:
# Input: s = "abcde", goal = "cdeab"
# Output: True
#
# Input: s = "abcde", goal = "abced"
# Output: False
# ============================

# ============================
# APPROACH:
#
# 1. Check all possible rotations of string s.
# 2. For each rotation:
#    - Move first character to end
#    - Compare with goal
# 3. If any rotation matches → return True
# 4. Otherwise → return False
#
# NOTE:
# Total rotations needed = length of string
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
# → n rotations and each comparison takes O(n)
#
# SPACE COMPLEXITY:
# O(n)
# → new string created during rotation
# ============================

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # If lengths differ, impossible
        if len(s) != len(goal):
            return False

        n = len(s)

        for _ in range(n):

            # Check if current rotation matches
            if s == goal:
                return True

            # Rotate string (move first char to end)
            s = s[1:] + s[0]

        return False


# ============================
# OPTIMIZED APPROACH (Important Trick):
#
# If goal is a rotation of s,
# then goal must be a substring of (s + s)
#
# Example:
# s = "abcde"
# s+s = "abcdeabcde"
# goal = "cdeab" → exists inside
#
# TIME: O(n)
# ============================

class SolutionOptimized:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)