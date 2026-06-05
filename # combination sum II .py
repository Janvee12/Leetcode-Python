# ============================
# PLATFORM:
# LeetCode
# (Problem 40 - Combination Sum II)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an array of integers
# candidates (may contain duplicates)
# and a target.
#
# Return all UNIQUE combinations
# where numbers sum to target.
#
# Rules:
# - Each number can be used ONCE
# - No duplicate combinations
#
# ============================
# APPROACH:
# ============================
#
# 1. Sort the array
#    → helps to handle duplicates
#
# 2. Use backtracking
#
# 3. At each step:
#    - pick a number
#    - move forward (i+1)
#
# 4. Skip duplicates using:
#    prev tracking
#
# ============================

from typing import List

class Solution:

    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(cur, pos, target):

            # ====================
            # BASE CASE: valid
            # ====================
            if target == 0:
                res.append(cur.copy())
                return

            # ====================
            # BASE CASE: invalid
            # ====================
            if target < 0:
                return

            prev = -1

            # ====================
            # TRY ALL OPTIONS
            # ====================
            for i in range(pos, len(candidates)):

                # ====================
                # SKIP DUPLICATES
                # ====================
                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])

                backtrack(
                    cur,
                    i + 1,
                    target - candidates[i]
                )

                cur.pop()

                prev = candidates[i]

        backtrack([], 0, target)
        return res