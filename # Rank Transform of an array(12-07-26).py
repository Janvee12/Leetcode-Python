# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Rank Transform of an Array
# ============================

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # Store rank for each unique element
        value_to_rank = {}

        # Sort unique values
        unique_values = sorted(set(arr))

        # Assign ranks starting from 1
        rank = 1
        for value in unique_values:
            value_to_rank[value] = rank
            rank += 1

        # Replace each element with its rank
        for i in range(len(arr)):
            arr[i] = value_to_rank[arr[i]]

        return arr