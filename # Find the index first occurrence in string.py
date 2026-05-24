# ============================
# PLATFORM:
# LeetCode
# (Problem 28 - Find the Index of the First Occurrence in a String)
# ============================

# ============================
# PROBLEM:
# Given two strings:
#
#     haystack
#     needle
#
# Return the index of the
# first occurrence of needle
# inside haystack.
#
# If needle is not found,
# return -1.
#
# Example:
#
# Input:
# haystack = "sadbutsad"
# needle = "sad"
#
# Output:
# 0
#
# Example:
#
# Input:
# haystack = "leetcode"
# needle = "leeto"
#
# Output:
# -1
# ============================

# ============================
# APPROACH:
#
# BRUTE FORCE / SLIDING WINDOW
#
# Steps:
#
# 1. Traverse every possible
#    starting index in haystack.
#
# 2. Extract substring of
#    length len(needle).
#
# 3. Compare with needle.
#
# 4. If equal:
#       return index
#
# 5. If never found:
#       return -1
#
# ============================

# ============================
# TIME COMPLEXITY:
# O((n - m) * m)
#
# n = len(haystack)
# m = len(needle)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:

    def strStr(
        self,
        haystack: str,
        needle: str
    ) -> int:

        # Empty needle case
        if needle == "":

            return 0

        # Traverse possible positions
        for i in range(
            len(haystack) + 1 - len(needle)
        ):

            # Match substring
            if haystack[i : i + len(needle)] == needle:

                return i

        # Not found
        return -1