# ============================
# PLATFORM:
# LeetCode
# (Problem 3043 - Find the Length of the Longest Common Prefix)
# ============================

# ============================
# PROBLEM:
# You are given two arrays:
#
#     arr1 and arr2
#
# A prefix of a number is formed
# from the starting digits.
#
# Task:
# Find the maximum length
# of any common prefix between:
#
# - a number from arr1
# - a number from arr2
#
# Example:
#
# Input:
# arr1 = [1,10,100]
# arr2 = [1000]
#
# Output:
# 3
#
# Explanation:
#
# Common prefixes:
# "1"
# "10"
# "100"
#
# Longest length = 3
# ============================

# ============================
# APPROACH:
#
# Use HASH SET
#
# Steps:
#
# 1. Convert each number in arr1
#    into string.
#
# 2. Generate all prefixes
#    and store them in a set.
#
# Example:
#
# 123 -> "1", "12", "123"
#
# 3. Traverse arr2:
#
#    - generate prefixes
#    - check if prefix exists in set
#
# 4. Track maximum prefix length.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(total digits in arr1 + arr2)
#
# SPACE COMPLEXITY:
# O(total prefixes)
# ============================

class Solution:

    def longestCommonPrefix(self, arr1, arr2):

        # Store prefixes from arr1
        s = set()

        # Generate prefixes for arr1
        for num in arr1:

            num = str(num)

            prefix = ""

            for ch in num:

                prefix += ch

                s.add(prefix)

        # Maximum prefix length
        ans = 0

        # Check prefixes in arr2
        for num in arr2:

            num = str(num)

            prefix = ""

            for ch in num:

                prefix += ch

                # Common prefix found
                if prefix in s:

                    ans = max(ans, len(prefix))

        return ans