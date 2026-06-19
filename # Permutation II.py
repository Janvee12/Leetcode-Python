# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 47. Permutations II
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given a collection of numbers
# that may contain duplicates,
# return all unique permutations.
#
# Example:
#
# nums = [1,1,2]
#
# Output:
#
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Backtracking + Frequency Map
#
# Count how many times each
# number appears.
#
# During recursion:
#
# 1. Choose a number whose
#    frequency > 0.
#
# 2. Add it to permutation.
#
# 3. Decrease frequency.
#
# 4. Recurse.
#
# 5. Backtrack.
#
# Since duplicate numbers are
# tracked by frequency,
# duplicate permutations are
# never generated.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n × n!)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from typing import List

class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        permutation = []

        # Frequency map
        count = {num: 0 for num in nums}

        for num in nums:
            count[num] += 1

        def dfs():

            # Complete permutation found
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            for num in count:

                if count[num] > 0:

                    permutation.append(num)
                    count[num] -= 1

                    dfs()

                    # Backtrack
                    count[num] += 1
                    permutation.pop()

        dfs()

        return result