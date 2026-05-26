# ============================
# PLATFORM:
# LeetCode
# (Problem 3120 - Count the Number of Special Characters I)
# ============================

# ============================
# PROBLEM:
# A character is called SPECIAL if:
#
# - both lowercase and uppercase
#   versions exist in the string.
#
# Example:
#
# 'a' and 'A'
#
# Task:
# Return the number of
# special characters in the string.
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
# Special characters:
# a/A
# b/B
# c/C
# ============================

# ============================
# APPROACH:
#
# Use SET
#
# Steps:
#
# 1. Store all characters
#    in a set.
#
# 2. Traverse all lowercase letters:
#
#       'a' to 'z'
#
# 3. Check:
#
#       lowercase exists
#       AND
#       uppercase exists
#
# 4. Count valid characters.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + 26)
# ≈ O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

class Solution:

    def numberOfSpecialChars(
        self,
        word: str
    ) -> int:

        # Count of special characters
        res = 0

        # Store all characters
        seen = set()

        for c in word:

            seen.add(c)

        # Check all alphabets
        for i in range(26):

            # Lowercase character
            c = chr(i + ord('a'))

            # Both lowercase and uppercase exist
            if c in seen and c.upper() in seen:

                res += 1

        return res