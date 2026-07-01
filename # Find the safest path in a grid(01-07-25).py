# ============================
# PLATFORM:
# LeetCode 2812
# PROBLEM:
# Find the Safest Path in a Grid
# ============================

from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        N = len(grid)

        # Check if a cell is inside the grid
        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N

        # ---------------------------------
        # Step 1: Multi-Source BFS
        # Compute distance of every cell
        # from the nearest thief.
        # ---------------------------------
        def precompute():

            q = deque()
            min_dist = {}

            # Put all thief cells into queue
            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0

            # BFS
            while q:

                r, c, dist = q.popleft()

                neighbors = [
                    [r + 1, c],
                    [r - 1, c],
                    [r, c + 1],
                    [r, c - 1]
                ]

                for r2, c2 in neighbors:

                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:

                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])

            return min_dist

        # Distance of every cell from nearest thief
        min_dist = precompute()

        # ---------------------------------
        # Step 2: Max Heap
        # Find safest path
        # ---------------------------------

        maxHeap = [(-min_dist[(0, 0)], 0, 0)]

        visit = {(0, 0)}

        while maxHeap:

            dist, r, c = heapq.heappop(maxHeap)

            dist = -dist

            # Destination reached
            if (r, c) == (N - 1, N - 1):
                return dist

            neighbors = [
                [r + 1, c],
                [r - 1, c],
                [r, c + 1],
                [r, c - 1]
            ]

            for r2, c2 in neighbors:

                if in_bounds(r2, c2) and (r2, c2) not in visit:

                    visit.add((r2, c2))

                    # Minimum safeness on this path
                    dist2 = min(dist, min_dist[(r2, c2)])

                    heapq.heappush(maxHeap, (-dist2, r2, c2))