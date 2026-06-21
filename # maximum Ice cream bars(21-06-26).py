# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 1833. Maximum Ice Cream Bars
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given:
#
# costs[i] = cost of the ith
# ice cream bar.
#
# coins = total money available.
#
# Return the maximum number of
# ice cream bars that can be
# purchased.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Greedy Algorithm
#
# To buy the maximum number of
# ice creams, always buy the
# cheapest ice cream first.
#
# Steps:
#
# 1. Sort the costs array.
# 2. Buy ice creams from the
#    smallest cost.
# 3. Stop when coins are not
#    sufficient.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
#
# SPACE COMPLEXITY:
# O(1)
# (Ignoring sorting space)
# ============================

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        # Sort costs in increasing order
        costs.sort()

        count = 0

        for cost in costs:

            # Not enough money
            if coins < cost:
                break

            # Buy the ice cream
            coins -= cost
            count += 1

        return count