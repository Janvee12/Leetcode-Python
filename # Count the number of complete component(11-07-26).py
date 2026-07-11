# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Count the Number of Complete Components
# ============================

from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # DFS to collect all nodes in a connected component
        def dfs(node):
            visited.add(node)
            component.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        complete_components = 0

        # Traverse every connected component
        for node in range(n):

            if node in visited:
                continue

            component = []
            dfs(node)

            size = len(component)
            is_complete = True

            # Check if every pair of nodes is directly connected
            for i in range(size):
                for j in range(i + 1, size):
                    if component[i] not in graph[component[j]]:
                        is_complete = False
                        break

                if not is_complete:
                    break

            if is_complete:
                complete_components += 1

        return complete_components