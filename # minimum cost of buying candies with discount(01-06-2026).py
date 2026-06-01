# ============================
# PLATFORM:
# LeetCode
# (Problem 2144 -
# Minimum Cost of Buying Candies With Discount)
# ============================

# ============================
# PROBLEM
# ============================
#
# You are given an array
# cost where:
#
# cost[i] = price of a candy.
#
# Offer:
#
# If you buy 2 candies,
# you can get 1 additional
# candy for free.
#
# Condition:
#
# The free candy's cost
# must be less than or equal
# to the minimum cost among
# the two purchased candies.
#
# Return the minimum amount
# of money needed to buy
# all candies.
#
# ============================

# ============================
# GREEDY OBSERVATION
# ============================
#
# To maximize the discount,
# make the most expensive
# possible candy free.
#
# Sort the candies in
# descending order:
#
# Example:
#
# [6,5,4,3,2,1]
#
# Group them as:
#
# (6,5,4)
# (3,2,1)
#
# In every group:
#
# Pay:
# 6 + 5
#
# Free:
# 4
#
# Pay:
# 3 + 2
#
# Free:
# 1
#
# Total:
#
# 6 + 5 + 3 + 2 = 16
#
# ============================

# ============================
# APPROACH
# ============================
#
# 1. Sort costs.
#
# 2. Traverse from largest
#    to smallest.
#
# 3. For every group of 3:
#
#    - Pay first candy
#    - Pay second candy
#    - Skip third candy
#
# The skipped candy is free.
#
# ============================

# ============================
# TIME COMPLEXITY
# ============================
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
# ============================
# SPACE COMPLEXITY
# ============================
#
# O(1)
# (excluding sort space)
#
# ============================

from typing import List

class Solution:

    def minimumCost(
        self,
        cost: List[int]
    ) -> int:

        n = len(cost)

        # Sort ascending
        cost.sort()

        total_cost = 0

        count = 1

        # Traverse from largest
        # to smallest
        for i in range(n - 1, -1, -1):

            # Pay for first
            # two candies
            if count != 3:

                total_cost += cost[i]

                count += 1

            # Every third candy
            # becomes free
            else:

                count = 1

        return total_cost