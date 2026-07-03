# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Find Maximum Path Score
# ============================

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(
        self,
        edges: List[List[int]],
        online: List[bool],
        k: int
    ) -> int:

        n = len(online)

        # If source or destination is offline,
        # no valid path exists.
        if not online[0] or not online[n - 1]:
            return -1

        # -------------------------------
        # Build graph using only
        # online nodes.
        # -------------------------------
        adj = defaultdict(list)

        left = float("inf")
        right = 0

        for u, v, w in edges:

            if online[u] and online[v]:
                adj[u].append((v, w))

                left = min(left, w)
                right = max(right, w)

        if left == float("inf"):
            return -1

        # ---------------------------------
        # Can we reach destination
        # using only edges >= limit
        # while total cost <= k ?
        # ---------------------------------
        def check(limit):

            pq = [(0, 0)]          # (cost, node)

            dist = [float("inf")] * n
            dist[0] = 0

            while pq:

                cost, node = heapq.heappop(pq)

                if cost > dist[node]:
                    continue

                if node == n - 1:
                    return True

                for nei, weight in adj[node]:

                    # Ignore weak edges
                    if weight < limit:
                        continue

                    new_cost = cost + weight

                    if (
                        new_cost <= k and
                        new_cost < dist[nei]
                    ):

                        dist[nei] = new_cost
                        heapq.heappush(
                            pq,
                            (new_cost, nei)
                        )

            return False

        # -------------------------------
        # Binary Search
        # -------------------------------
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans