# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Path Existence Queries II
# ============================

from typing import List
from math import inf
import bisect


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # (value, original index)
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()

        # Original index -> Sorted index
        node_to_index = {}
        for i, (_, node) in enumerate(nums):
            node_to_index[node] = i

        # Farthest reachable index in one jump
        maxReach = [0] * n
        for i, (value, _) in enumerate(nums):
            j = bisect.bisect_left(nums, (value + maxDiff, inf)) - 1
            maxReach[i] = j

        # Binary Lifting Table
        LOG = n.bit_length()
        up = [maxReach]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        answer = []

        for u, v in queries:

            u = node_to_index[u]
            v = node_to_index[v]

            if u == v:
                answer.append(0)
                continue

            if u > v:
                u, v = v, u

            current = u
            jumps = 0

            # Binary Lifting
            for k in range(LOG - 1, -1, -1):
                if up[k][current] < v:
                    current = up[k][current]
                    jumps += 1 << k

            if maxReach[current] >= v:
                answer.append(jumps + 1)
            else:
                answer.append(-1)

        return answer