# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# GCD of Odd and Even Sums
# ============================

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        # Calculate the sum of odd and even numbers
        odd_sum = 0
        even_sum = 0

        for num in range(1, 2 * n + 1):
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num

        # Compute GCD using Euclid's subtraction algorithm
        def gcd(a, b):

            if a > b:
                return gcd(a - b, b)

            if b > a:
                return gcd(a, b - a)

            return a

        return gcd(even_sum, odd_sum)