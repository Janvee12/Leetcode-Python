# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Maximum Product of Two Digits
# ============================

class Solution:
    def maxProduct(self, n: int) -> int:

        # Store all digits of the number
        digits = []

        while n:
            digits.append(n % 10)
            n //= 10

        # Sort the digits
        digits.sort()

        # Return the product of the two largest digits
        return digits[-1] * digits[-2]