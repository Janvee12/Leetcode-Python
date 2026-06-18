# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 46. Permutations
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an array of distinct integers,
# return all possible permutations.
#
# A permutation is an arrangement
# of all elements in different orders.
#
# Example:
#
# nums = [1,2,3]
#
# Output:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Recursion
#
# For every number:
#
# 1. Choose it as the first element.
# 2. Generate permutations of
#    the remaining elements.
# 3. Add the chosen element
#    in front of every permutation.
#
# Repeat for all numbers.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n × n!)
#
# SPACE COMPLEXITY:
# O(n!)
# ============================

from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        # ============================
        # BASE CASE
        # ============================
        if len(nums) == 1:
            return [nums[:]]

        res = []

        # ============================
        # TRY EVERY ELEMENT
        # AS FIRST ELEMENT
        # ============================
        for i in range(len(nums)):

            current = nums[i]

            # Remaining elements
            remaining = nums[:i] + nums[i + 1:]

            # Generate permutations
            perms = self.permute(remaining)

            # Add current element
            for p in perms:
                res.append([current] + p)

        return res