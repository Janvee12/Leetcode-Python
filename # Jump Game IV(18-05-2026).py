# ============================
# PLATFORM:
# LeetCode (Problem 1345 - Jump Game IV)
# ============================

# ============================
# PROBLEM:
# Given an array arr,
# you start at index 0.
#
# In one move, you can jump to:
#
# 1. i + 1
# 2. i - 1
# 3. Any index j where:
#
#       arr[i] == arr[j]
#       and i != j
#
# Task:
# Return the minimum number
# of jumps needed to reach
# the last index.
#
# Example:
#
# Input:
# arr = [100,-23,-23,404,100,23,23,23,3,404]
#
# Output:
# 3
#
# Explanation:
# 0 -> 4 -> 3 -> 9
# ============================

# ============================
# APPROACH:
#
# Use BFS (Breadth First Search)
#
# Why BFS?
#
# Because every jump has equal cost,
# and BFS guarantees minimum steps.
#
# Steps:
#
# 1. Store indices of same values
#    using hashmap:
#
#       value -> list of indices
#
# 2. Start BFS from index 0.
#
# 3. From each index,
#    explore:
#
#       i - 1
#       i + 1
#       all same-value indices
#
# 4. Use visited array
#    to avoid revisiting nodes.
#
# 5. Clear processed value group
#    after visiting to optimize.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# Each index/value processed once.
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from collections import defaultdict, deque
from typing import List

class Solution:

    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)

        # Edge case
        if n == 1:

            return 0

        # Map:
        # value -> all indices
        dict1 = defaultdict(list)

        for i, val in enumerate(arr):

            dict1[val].append(i)

        # BFS queue
        q = deque([0])

        # Visited indices
        visited = [False] * n

        visited[0] = True

        steps = 0

        # BFS traversal
        while q:

            for _ in range(len(q)):

                i = q.popleft()

                # Reached last index
                if i == n - 1:

                    return steps

                neighbour = []

                # Left jump
                if i - 1 >= 0:

                    neighbour.append(i - 1)

                # Right jump
                if i + 1 < n:

                    neighbour.append(i + 1)

                # Same value jumps
                neighbour.extend(dict1[arr[i]])

                # Process neighbors
                for neigh in neighbour:

                    if not visited[neigh]:

                        visited[neigh] = True

                        q.append(neigh)

                # Optimization:
                # clear processed indices
                dict1[arr[i]].clear()

            steps += 1

        return -1