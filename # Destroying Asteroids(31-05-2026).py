# ============================
# PLATFORM:
# LeetCode
# (Problem 2126 - Destroying Asteroids)
# ============================

# ============================
# PROBLEM:
# You are given:
#
# - An initial planet mass
# - An array of asteroid masses
#
# Rules:
#
# 1. If:
#
#       mass >= asteroid
#
#    the planet destroys
#    the asteroid.
#
# 2. After destruction:
#
#       mass += asteroid
#
# 3. If an asteroid is larger
#    than the current mass,
#    it cannot be destroyed.
#
# Task:
# Determine whether the planet
# can destroy ALL asteroids.
# ============================

# ============================
# APPROACH:
#
# GREEDY
#
# Always destroy the
# smallest asteroid first.
#
# Why?
#
# Smaller asteroids are easier
# to absorb and increase the
# planet's mass.
#
# After sorting:
#
# - If current asteroid
#   is larger than mass,
#   answer is False.
#
# - Otherwise absorb it
#   and increase mass.
#
# ============================

# ============================
# EXAMPLE
#
# mass = 10
# asteroids = [3, 9, 19]
#
# Sort:
# [3, 9, 19]
#
# Destroy 3:
# mass = 13
#
# Destroy 9:
# mass = 22
#
# Destroy 19:
# mass = 41
#
# All destroyed.
#
# Output:
# True
# ============================

# ============================
# TIME COMPLEXITY:
#
# Sorting:
# O(n log n)
#
# Traversal:
# O(n)
#
# Total:
# O(n log n)
#
# SPACE COMPLEXITY:
# O(1)
# (excluding sorting space)
# ============================

from typing import List

class Solution:

    def asteroidsDestroyed(
        self,
        mass: int,
        asteroids: List[int]
    ) -> bool:

        # Process asteroids
        # from smallest to largest
        asteroids.sort()

        for asteroid in asteroids:

            # Cannot destroy it
            if asteroid > mass:

                return False

            # Absorb asteroid mass
            mass += asteroid

        return True