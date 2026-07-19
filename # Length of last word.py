# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Length of Last Word
# ============================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Start from the end of the string
        index = len(s) - 1
        length = 0

        # Skip trailing spaces
        while s[index] == " ":
            index -= 1

        # Count the characters of the last word
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1

        return length