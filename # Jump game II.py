# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 45. Jump Game II
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given an array nums.
#
# nums[i] represents the maximum
# jump length from index i.
#
# Return the minimum number of
# jumps required to reach the
# last index.
#
# It is guaranteed that the
# last index is reachable.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Greedy + BFS Level Traversal
#
# Think of each jump as a level.
#
# [l, r] represents all positions
# reachable using the current
# number of jumps.
#
# For every index in the current
# range, calculate the farthest
# position we can reach.
#
# Then move to the next level.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0

        # Current reachable range
        left = 0
        right = 0

        while right < len(nums) - 1:

            farthest = 0

            # Explore current level
            for i in range(left, right + 1):
                farthest = max(
                    farthest,
                    i + nums[i]
                )

            # Next level
            left = right + 1
            right = farthest

            jumps += 1

        return jumps