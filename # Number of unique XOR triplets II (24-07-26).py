# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Number of Unique XOR Triplets II
# ============================

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        n = len(nums)

        # Store all possible XOR values of pairs
        pair_xor = set()

        for i in range(n):
            for j in range(i, n):
                pair_xor.add(nums[i] ^ nums[j])

        # Compute unique XOR values of triplets
        triplet_xor = set()

        for num in nums:
            for value in pair_xor:
                triplet_xor.add(num ^ value)

        return len(triplet_xor)