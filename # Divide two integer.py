# ============================
# PLATFORM:
# LeetCode
# (Problem 29 - Divide Two Integers)
# ============================

# ============================
# PROBLEM:
# Given two integers:
#
#     dividend
#     divisor
#
# Divide them WITHOUT using:
#
# - multiplication (*)
# - division (/)
# - modulo (%)
#
# Return the quotient
# truncated toward zero.
#
# Example:
#
# Input:
# dividend = 10
# divisor = 3
#
# Output:
# 3
#
# Example:
#
# Input:
# dividend = 7
# divisor = -3
#
# Output:
# -2
# ============================

# ============================
# APPROACH:
#
# Use BIT MANIPULATION
# and repeated subtraction.
#
# Key Idea:
#
# Instead of subtracting divisor
# one-by-one,
#
# subtract the largest
# power-of-two multiple.
#
# Example:
#
# 40 / 3
#
# Largest doubles:
#
# 3
# 6
# 12
# 24
#
# subtract 24 first,
# then continue.
#
# ============================

# ============================
# IMPORTANT CASE:
#
# 32-bit overflow:
#
# -2^31 / -1
#
# exceeds integer range.
#
# Return:
#
# 2^31 - 1
# ============================

# ============================
# TIME COMPLEXITY:
# O(log n * log n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:

    def divide(
        self,
        dividend: int,
        divisor: int
    ) -> int:

        # ====================
        # Handle overflow
        # ====================
        if dividend == -2**31 and divisor == -1:

            return 2**31 - 1

        # ====================
        # Determine sign
        # ====================
        sign = -1 if (
            (dividend < 0) ^
            (divisor < 0)
        ) else 1

        # ====================
        # Convert to positive
        # ====================
        dividend = abs(dividend)

        divisor = abs(divisor)

        quotient = 0

        # ====================
        # Main division logic
        # ====================
        while dividend >= divisor:

            temp = divisor

            multiple = 1

            # Double divisor
            while dividend >= (temp << 1):

                temp <<= 1

                multiple <<= 1

            # Subtract largest multiple
            dividend -= temp

            quotient += multiple

        # Apply sign
        return sign * quotient