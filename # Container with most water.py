# ============================
# PLATFORM:
# LeetCode (Problem 11 - Container With Most Water)
# ============================

# ============================
# PROBLEM:
# You are given an array height[] where each element represents
# the height of a vertical line.
#
# Find two lines such that together they form a container
# that holds the maximum amount of water.
#
# Water area = min(height[l], height[r]) * (r - l)
#
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# ============================

# ============================
# APPROACH:
#
# Use Two Pointer Technique:
#
# 1. Start with:
#    l = 0 (left pointer)
#    r = n-1 (right pointer)
#
# 2. Calculate area:
#    area = min(height[l], height[r]) * (r - l)
#
# 3. Move pointer:
#    - Move the smaller height pointer
#      (because area depends on smaller height)
#
# 4. Repeat until l < r
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Single pass
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        max_area = 0  # better initialization than -inf

        while l < r:

            # Calculate area
            area = min(height[l], height[r]) * (r - l)

            # Update maximum
            max_area = max(max_area, area)

            # Move pointer with smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area