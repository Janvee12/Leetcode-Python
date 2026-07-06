# ============================
# PLATFORM:
# LeetCode 60
# PROBLEM:
# Permutation Sequence
# ============================

from typing import List
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Numbers available to build the permutation
        nums = [str(i) for i in range(1, n + 1)]

        output = []

        # Total permutations of n numbers
        factorial = math.factorial(n)

        # Convert k to 0-based index
        index = k - 1

        while nums:

            # Number of permutations in one block
            factorial //= len(nums)

            # Select the correct digit
            pos = index // factorial

            # Add it to the answer
            output.append(nums.pop(pos))

            # Remaining index within the block
            index %= factorial

        return "".join(output)