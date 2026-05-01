# ============================
# PLATFORM:
# LeetCode (Problem 6 - Zigzag Conversion)
# ============================

# ============================
# PROBLEM:
# Given a string s and an integer numRows,
# write the string in a zigzag pattern on the given number of rows.
#
# Then read the pattern row by row and return the result.
#
# Example:
# Input: s = "PAYPALISHIRING", numRows = 3
#
# Zigzag Pattern:
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# Output: "PAHNAPLSIIGYIR"
# ============================

# ============================
# APPROACH:
#
# Instead of building the full zigzag matrix,
# we directly calculate indices for each row.
#
# Key Idea:
# - Pattern repeats every cycle:
#     cycle length = 2 * (numRows - 1)
#
# - For each row r:
#     - Pick elements at index i = r, r + cycle, r + 2*cycle...
#
# - For middle rows:
#     - Also pick diagonal elements:
#       index = i + cycle - 2*r
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Each character is visited once
#
# SPACE COMPLEXITY:
# O(1) (excluding output string)
# ============================

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Edge case: no zigzag needed
        if numRows == 1:
            return s

        res = ""

        for r in range(numRows):

            increment = 2 * (numRows - 1)

            for i in range(r, len(s), increment):

                # Vertical element
                res += s[i]

                # Diagonal element (only for middle rows)
                if (r > 0 and r < numRows - 1 and
                        i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]

        return res