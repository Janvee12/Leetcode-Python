# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Permutation Sequence
# ============================

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Store numbers from 1 to n
        numbers = [str(i) for i in range(1, n + 1)]

        result = []

        # Total permutations
        factorial = math.factorial(n)

        # Convert to 0-based index
        index = k - 1

        # Build the kth permutation
        while numbers:

            factorial //= len(numbers)

            position = index // factorial
            result.append(numbers.pop(position))

            index %= factorial

        return "".join(result)