# ============================
# PLATFORM:
# LeetCode (Problem 12 - Integer to Roman)
# ============================

# ============================
# PROBLEM:
# Convert an integer into its Roman numeral representation.
#
# Roman symbols:
# I   = 1
# V   = 5
# X   = 10
# L   = 50
# C   = 100
# D   = 500
# M   = 1000
#
# Special cases:
# IV  = 4
# IX  = 9
# XL  = 40
# XC  = 90
# CD  = 400
# CM  = 900
#
# Example:
# Input: 1994
# Output: "MCMXCIV"
# ============================

# ============================
# APPROACH:
#
# Greedy Algorithm:
#
# 1. Store Roman symbols with values.
#
# 2. Traverse values from largest → smallest.
#
# 3. For each value:
#    - Find how many times it fits into num
#    - Append corresponding symbol
#    - Reduce num using modulo
#
# 4. Continue until num becomes 0.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
# → Fixed number of Roman symbols (13)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:
    def intToRoman(self, num: int) -> str:

        # Roman symbols and values
        symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]

        res = ""

        # Traverse from largest value to smallest
        for sym, val in reversed(symList):

            if num // val:

                # Number of times symbol repeats
                count = num // val

                # Append symbol
                res += (sym * count)

                # Reduce number
                num = num % val

        return res