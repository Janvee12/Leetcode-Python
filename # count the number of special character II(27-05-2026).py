# ============================
# PLATFORM:
# LeetCode
# (Problem 3121 - Count the Number of Special Characters II)
# ============================

# ============================
# PROBLEM:
# A character is SPECIAL if:
#
# 1. Both lowercase and uppercase
#    versions exist in the string.
#
# 2. Every lowercase occurrence
#    appears BEFORE
#    the first uppercase occurrence.
#
# Task:
# Return the number of
# special characters.
#
# Example:
#
# Input:
# word = "aaAbcBC"
#
# Output:
# 3
#
# Explanation:
#
# a/A → valid
# b/B → valid
# c/C → valid
# ============================

# ============================
# APPROACH:
#
# Store:
#
# 1. lastlower[c]
#    → last index of lowercase char
#
# 2. firstupper[c]
#    → first index of uppercase char
#
# A character is special if:
#
# lastlower[c] < firstupper[c.upper()]
#
# meaning:
# all lowercase letters occur
# before uppercase letters.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + 26)
# ≈ O(n)
#
# SPACE COMPLEXITY:
# O(26)
# ============================

class Solution:

    def numberOfSpecialChars(
        self,
        word: str
    ) -> int:

        n = len(word)

        # Last position of lowercase
        lastlower = {}

        # First position of uppercase
        firstupper = {}

        # Traverse string
        for i, c in enumerate(word):

            # Store last lowercase index
            if c.islower():

                lastlower[c] = i

            # Store first uppercase index
            elif c not in firstupper:

                firstupper[c] = i

        # Count special characters
        res = 0

        # Check all alphabets
        for i in range(26):

            c = chr(i + ord('a'))

            # Valid special character
            if (
                c in lastlower
                and c.upper() in firstupper
                and lastlower[c] < firstupper[c.upper()]
            ):

                res += 1

        return res