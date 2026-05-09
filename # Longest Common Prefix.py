# ============================
# PLATFORM:
# LeetCode (Problem 14 - Longest Common Prefix)
# ============================

# ============================
# PROBLEM:
# Given an array of strings strs,
# return the longest common prefix among all strings.
#
# If there is no common prefix,
# return an empty string "".
#
# Example:
# Input:
# strs = ["flower", "flow", "flight"]
#
# Output:
# "fl"
#
# Example:
# Input:
# strs = ["dog", "racecar", "car"]
#
# Output:
# ""
# ============================

# ============================
# APPROACH:
#
# 1. Take the first string as reference.
#
# 2. Traverse each character index of first string.
#
# 3. Compare that character with all other strings.
#
# 4. If:
#    - index exceeds any string length
#    OR
#    - characters do not match
#
#    → return current prefix.
#
# 5. Otherwise add character to result.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * m)
#
# n = number of strings
# m = length of smallest prefix
#
# SPACE COMPLEXITY:
# O(1)
# → excluding output string
# ============================

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Store common prefix
        res = ""

        # Traverse characters of first string
        for i in range(len(strs[0])):

            # Compare with all strings
            for s in strs:

                # Mismatch OR string ends
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # Character matches in all strings
            res += strs[0][i]

        return res