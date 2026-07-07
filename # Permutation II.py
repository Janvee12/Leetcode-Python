# ============================
# PLATFORM:
# LeetCode 47
# PROBLEM:
# Permutations II
# ============================

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        perm = []

        # Frequency map
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():

            # Base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            # Try every available number
            for n in count:

                if count[n] > 0:

                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    # Backtrack
                    count[n] += 1
                    perm.pop()

        dfs()
        return res