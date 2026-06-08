# ============================
# PLATFORM:
# LeetCode
# (42. Trapping Rain Water)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an array height[] where each element
# represents bar height,
#
# calculate how much water can be trapped
# after raining.
#
# Water at each index depends on:
#
#   min(max_left, max_right) - height[i]
#
# ============================
# APPROACH USED:
# ============================
#
# We precompute:
#
# 1. max_left[i]  → tallest bar on left of i
# 2. max_right[i] → tallest bar on right of i
#
# Then compute trapped water.
#
# ============================

from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:

        n = len(height)

        # ============================
        # STEP 1: Arrays for max walls
        # ============================
        max_left = [0] * n
        max_right = [0] * n

        l_wall = 0
        r_wall = 0

        # ============================
        # STEP 2: Fill left and right max in one loop
        # ============================
        for i in range(n):

            j = -i - 1  # reverse index

            max_left[i] = l_wall
            max_right[j] = r_wall

            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        # ============================
        # STEP 3: Calculate water trapped
        # ============================
        total_water = 0

        for i in range(n):

            # water level at index i
            water_level = min(max_left[i], max_right[i])

            # water stored = water_level - height[i]
            total_water += max(0, water_level - height[i])

        return total_water