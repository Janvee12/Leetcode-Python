# ============================
# PLATFORM:
# (Custom / LeetCode-style)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given two integers num1 and num2,
# consider every number in range [num1, num2].
#
# For each number:
#   Convert it to string.
#
# A digit at position i is called a
# "waviness point" if:
#
#   s[i-1] < s[i] > s[i+1]   OR
#   s[i-1] > s[i] < s[i+1]
#
# Count total number of such
# waviness points across all numbers.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# 1. Iterate over all numbers
#    from num1 to num2.
#
# 2. Convert each number to string.
#
# 3. For each middle digit i:
#
#    Check:
#    - peak  (up-down pattern)
#    - valley (down-up pattern)
#
# 4. If condition satisfies,
#    increment result.
#
# ============================

class Solution:

    def totalWaviness(
        self,
        num1: int,
        num2: int
    ) -> int:

        res = 0

        # Iterate over range
        for n in range(num1, num2 + 1):

            s = str(n)

            # Check middle digits only
            for i in range(1, len(s) - 1):

                # ====================
                # Peak or Valley check
                # ====================
                if (
                    s[i - 1] < s[i] > s[i + 1]
                    or
                    s[i - 1] > s[i] < s[i + 1]
                ):
                    res += 1

        return res