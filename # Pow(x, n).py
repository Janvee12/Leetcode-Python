# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Pow(x, n)
# ============================

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):

            # Base Cases
            if x == 0:
                return 0

            if n == 0:
                return 1

            # Compute x^(n//2)
            half = helper(x, n // 2)

            # Square the result
            result = half * half

            # If exponent is odd, multiply once more by x
            return x * result if n % 2 else result

        # Calculate power using positive exponent
        answer = helper(x, abs(n))

        # Handle negative exponent
        return answer if n >= 0 else 1 / answer