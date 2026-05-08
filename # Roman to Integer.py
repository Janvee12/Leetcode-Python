# ============================
# PLATFORM:
# LeetCode (Problem 13 - Roman to Integer)
# ============================

# ============================
# PROBLEM:
# Convert a Roman numeral string into an integer.
#
# Roman symbols:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Special subtraction cases:
# IV = 4
# IX = 9
# XL = 40
# XC = 90
# CD = 400
# CM = 900
#
# Example:
# Input: "MCMXCIV"
# Output: 1994
# ============================

# ============================
# APPROACH:
#
# 1. Store Roman symbols in a dictionary.
#
# 2. Traverse the string from left → right.
#
# 3. Compare current symbol with next symbol:
#
#    - If current value < next value:
#         subtract current value
#
#    - Otherwise:
#         add current value
#
# Why subtraction?
#
# Example:
# "IV"
# I = 1, V = 5
# Since 1 < 5:
# result = -1 + 5 = 4
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverse string once
#
# SPACE COMPLEXITY:
# O(1)
# → Fixed-size dictionary
# ============================

class Solution:
    def romanToInt(self, s: str) -> int:

        # Roman symbol mapping
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0

        for i in range(len(s)):

            # If smaller value appears before larger value
            # subtract it
            if (i + 1 < len(s) and
                    roman[s[i]] < roman[s[i + 1]]):

                res -= roman[s[i]]

            else:
                res += roman[s[i]]

        return res