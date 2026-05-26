# ============================
# PLATFORM:
# LeetCode
# (Problem 30 - Substring with Concatenation of All Words)
# ============================

# ============================
# PROBLEM:
# Given:
#
#     s      -> string
#     words  -> list of words
#
# All words have same length.
#
# Task:
# Find all starting indices
# where a substring is formed
# by concatenating every word
# exactly once
# and without extra characters.
#
# Example:
#
# Input:
# s = "barfoothefoobarman"
# words = ["foo","bar"]
#
# Output:
# [0,9]
#
# Explanation:
#
# "barfoo" starts at 0
# "foobar" starts at 9
# ============================

# ============================
# APPROACH:
#
# BRUTE FORCE
#
# Steps:
#
# 1. Compute total substring length:
#
#       word_length * number_of_words
#
# 2. Traverse every possible start.
#
# 3. Extract substring of total length.
#
# 4. Split substring into chunks
#    of word size.
#
# 5. Compare sorted chunk list
#    with sorted words list.
#
# 6. If equal:
#       store index.
#
# ============================

# ============================
# NOTE:
#
# This solution works,
# but sorting every time
# is expensive.
#
# Optimized solutions use:
#
# - Sliding Window
# - HashMap frequency counting
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(n * k log k)
#
# n = length of string
# k = number of words
#
# SPACE COMPLEXITY:
# O(k)
# ============================

class Solution(object):

    def findSubstring(self, s, words):

        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # Total substring length
        total = len(words[0]) * len(words)

        # Result indices
        res = []

        # Traverse all possible starts
        for i in range(len(s) - total + 1):

            sub = []

            # Extract candidate substring
            ele = s[i : i + total]

            # Break into equal-sized words
            for j in range(
                0,
                len(ele),
                len(words[0])
            ):

                sub.append(
                    ele[j : j + len(words[0])]
                )

            # Compare sorted lists
            if sorted(sub) == sorted(words):

                res.append(i)

        return res