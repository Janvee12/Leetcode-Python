# ============================
# PLATFORM:
# LeetCode (Problem 1665 - Minimum Initial Energy to Finish Tasks)
# ============================

# ============================
# PROBLEM:
# You are given tasks where:
#
# tasks[i] = [actual, minimum]
#
# - actual  = energy spent to complete task
# - minimum = minimum energy required before starting task
#
# You can complete tasks in any order.
#
# Task:
# Return the minimum initial energy required
# to finish all tasks.
#
# Example:
# Input:
# tasks = [[1,2],[2,4],[4,8]]
#
# Output:
# 8
# ============================

# ============================
# APPROACH:
#
# GREEDY STRATEGY
#
# Important Observation:
#
# Tasks with larger:
#     (minimum - actual)
#
# should be done first.
#
# Why?
#
# They require more "extra energy"
# before starting.
#
# ------------------------------------------------
# STEP 1:
# Sort tasks by:
#
#     minimum - actual
#
# in descending order.
#
# ------------------------------------------------
# STEP 2:
#
# Maintain:
#
# avail = current available energy
# res   = minimum initial energy needed
#
# ------------------------------------------------
# STEP 3:
#
# For each task:
#
# If available energy is insufficient:
#
#     need = minimum - avail
#
# Add extra energy.
#
# Then complete task:
#
#     avail -= actual
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
# → sorting tasks
#
# SPACE COMPLEXITY:
# O(1)
# → excluding sorting space
# ============================

from typing import List

class Solution:

    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # Sort by (minimum - actual) descending
        tasks.sort(
            key=lambda x: x[1] - x[0],
            reverse=True
        )

        # Total initial energy required
        res = 0

        # Current available energy
        avail = 0

        # Process tasks
        for actual, minimum in tasks:

            # Extra energy needed
            need = minimum - avail

            if need > 0:

                res += need
                avail += need

            # Complete task
            avail -= actual

        return res