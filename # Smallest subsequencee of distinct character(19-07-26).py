# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Smallest Subsequence of Distinct Characters
# ============================

class Solution:
    def smallestSubsequence(self, s: str) -> str:

        # Store the last occurrence of each character
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []

        # Build the smallest lexicographical subsequence
        for i, char in enumerate(s):

            # Skip if the character is already included
            if char in stack:
                continue

            # Remove larger characters that appear again later
            while (
                stack
                and char < stack[-1]
                and i < last_occurrence[stack[-1]]
            ):
                stack.pop()

            # Add the current character
            stack.append(char)

        return "".join(stack)