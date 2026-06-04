# ============================
# PLATFORM:
# LeetCode
# (Problem 39 - Combination Sum)
# ============================

# ============================
# PROBLEM
# ============================
#
# Given an array of distinct
# integers candidates and a
# target integer target.
#
# Return all unique combinations
# where the chosen numbers sum
# to target.
#
# You may use the same number
# unlimited times.
#
# ============================

# ============================
# APPROACH (BACKTRACKING)
# ============================
#
# At each index i:
#
# Choice 1:
#   include candidates[i]
#   (can reuse same element)
#
# Choice 2:
#   skip candidates[i]
#
# Stop conditions:
#
# - total == target → valid path
# - total > target → invalid path
# - i out of bounds → stop
#
# ============================

from typing import List

class Solution:

    def combinationSum(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:

        res = []

        def dfs(i, cur, total):

            # ====================
            # BASE CASE: success
            # ====================
            if total == target:
                res.append(cur.copy())
                return

            # ====================
            # BASE CASE: invalid
            # ====================
            if i >= len(candidates) or total > target:
                return

            # ====================
            # CHOICE 1:
            # include current number
            # ====================
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()

            # ====================
            # CHOICE 2:
            # skip current number
            # ====================
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res