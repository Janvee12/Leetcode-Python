# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Path Existence Queries
# ============================

from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # group[i] = connected component id of nums[i]
        groups = [0] * n
        group_id = 0

        # Build connected components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group_id += 1
            groups[i] = group_id

        # Answer queries
        answer = []
        for u, v in queries:
            answer.append(groups[u] == groups[v])

        return answer