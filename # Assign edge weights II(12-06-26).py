# ============================
# PLATFORM:
# LeetCode
# (Assign Edge Weights II)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given:
#
# - A tree with n nodes
# - Multiple queries (u, v)
#
# For each query:
#
# Find the number of ways to assign
# edge weights on the path from u to v.
#
# The answer depends only on:
#
#     path length = number of edges
#
# If path contains d edges:
#
#     ways = 2^(d-1)
#
# Return answers modulo:
#
#     10^9 + 7
#
# ============================
# APPROACH:
# ============================
#
# To find path length quickly:
#
# 1. Build tree
# 2. Compute depth of every node
# 3. Build Binary Lifting table
# 4. Find LCA(u,v)
# 5. Distance:
#
#    depth[u] + depth[v]
#    - 2 * depth[LCA]
#
# 6. Answer:
#
#    0                 if dist = 0
#    2^(dist-1) mod M otherwise
#
# ============================

from typing import List
from collections import deque

class Solution:

    def assignEdgeWeights(
        self,
        edges: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:

        MOD = 10**9 + 7

        # ============================
        # STEP 1: Build Graph
        # ============================
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # ============================
        # STEP 2: Binary Lifting Setup
        # ============================
        LOG = (n + 1).bit_length()

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # ============================
        # STEP 3: BFS for depth & parent
        # ============================
        q = deque([1])

        visited = [False] * (n + 1)
        visited[1] = True

        while q:

            u = q.popleft()

            for v in g[u]:

                if not visited[v]:

                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u

                    q.append(v)

        # ============================
        # STEP 4: Build lifting table
        # ============================
        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k - 1][parent[k - 1][v]]

        # ============================
        # STEP 5: LCA Function
        # ============================
        def lca(a: int, b: int) -> int:

            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            # bring same depth
            for k in range(LOG):
                if diff & (1 << k):
                    a = parent[k][a]

            if a == b:
                return a

            # lift both nodes
            for k in range(LOG - 1, -1, -1):

                if parent[k][a] != parent[k][b]:

                    a = parent[k][a]
                    b = parent[k][b]

            return parent[0][a]

        # ============================
        # STEP 6: Process Queries
        # ============================
        ans = []

        for u, v in queries:

            ancestor = lca(u, v)

            dist = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if dist == 0:
                ans.append(0)
            else:
                ans.append(
                    pow(2, dist - 1, MOD)
                )

        return ans