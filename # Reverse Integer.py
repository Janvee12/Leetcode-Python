# ============================
# PLATFORM:
# LeetCode (Problem 7 - Reverse Integer)
# ============================

# ============================
# PROBLEM:
# Given a signed 32-bit integer x, return x with its digits reversed.
#
# If reversing x causes the value to go outside the signed
# 32-bit integer range [-2^31, 2^31 - 1], return 0.
#
# Example:
# Input: x = 123
# Output: 321
#
# Input: x = -123
# Output: -321
#
# Input: x = 1534236469
# Output: 0  (overflow case)
# ============================

# ============================
# APPROACH:
#
# 1. Extract last digit using modulo (% or fmod for negatives).
# 2. Remove last digit using division.
# 3. Build reversed number by:
#       res = res * 10 + digit
#
# 4. Before updating res, check for overflow:
#    - If res exceeds 32-bit integer limits → return 0
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(log10(n))
# → Number of digits in x
#
# SPACE COMPLEXITY:
# O(1)
# ============================

import math

class Solution:
    def reverse(self, x: int) -> int:

        # 32-bit integer limits
        MIN_INT = -2147483648
        MAX_INT = 2147483647

        res = 0

        while x != 0:

            # Extract last digit (handles negative correctly)
            digit = int(math.fmod(x, 10))

            # Remove last digit
            x = int(x / 10)

            # Check overflow before multiplying
            if (res > MAX_INT // 10 or
                (res == MAX_INT // 10 and digit > 7)):
                return 0

            if (res < MIN_INT // 10 or
                (res == MIN_INT // 10 and digit < -8)):
                return 0

            # Build reversed number
            res = res * 10 + digit

        return res