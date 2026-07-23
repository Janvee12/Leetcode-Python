# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Number of Unique XOR Triplets I
# ============================

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        n = len(nums)

        # If there are fewer than 3 elements,
        # every value is already a unique XOR result
        if n <= 2:
            return n

        # Return the smallest power of 2
        # greater than or equal to n
        return 2 ** n.bit_length()