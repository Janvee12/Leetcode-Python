# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 50. Pow(x, n)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Implement:
#
#     pow(x, n)
#
# Calculate:
#
#     xⁿ
#
# without using the built-in
# power function.
#
# The exponent n can be:
#
# • Positive
# • Negative
# • Zero
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Use Binary Exponentiation.
#
# Observations:
#
# xⁿ
#
# If n is even:
#
# xⁿ = (x^(n/2))²
#
# If n is odd:
#
# xⁿ = x × (x^((n-1)/2))²
#
# This reduces the exponent
# by half each time.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(log n)
# (Recursive stack)
# ============================

class Solution:

    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):

            # Base cases
            if x == 0:
                return 0

            if n == 0:
                return 1

            # Compute x^(n/2)
            res = helper(x, n // 2)

            # Square it
            res = res * res

            # Odd exponent
            if n % 2:
                return x * res

            # Even exponent
            return res

        answer = helper(x, abs(n))

        # Negative power
        if n < 0:
            return 1 / answer

        return answer