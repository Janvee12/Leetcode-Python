# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Sum and Multiply
# ============================

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        # Special case
        if n == 0:
            return 0

        digits = []
        digit_sum = 0

        # Process each digit
        for c in str(n):

            if c != '0':
                digits.append(c)
                digit_sum += int(c)

        # Form the number after removing zeros
        number = int("".join(digits))

        # Return product
        return number * digit_sum