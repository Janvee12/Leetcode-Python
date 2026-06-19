# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 1732. Find the Highest Altitude
# ============================

# ============================
# PROBLEM:
# ============================
#
# A biker starts at altitude 0.
#
# gain[i] represents the net gain
# in altitude between points.
#
# Find the highest altitude reached.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Keep track of:
#
# 1. Current altitude
# 2. Maximum altitude seen so far
#
# Start altitude = 0
#
# For every gain:
#
# altitude += gain
#
# Update maximum altitude.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = 0
        altitude = 0

        for g in gain:

            altitude += g

            highest = max(
                highest,
                altitude
            )

        return highest