# ============================
# PLATFORM:
# LeetCode
# (Earliest Finish Time)
# ============================

# ============================
# PROBLEM
# ============================
#
# We have two types of rides:
#
# 1. Land rides
# 2. Water rides
#
# For every ride:
#
# startTime[i]
# duration[i]
#
# A person must complete:
#
# - One land ride
# - One water ride
#
# in any order.
#
# Goal:
#
# Return the earliest possible
# finishing time.
#
# ============================

# ============================
# APPROACH
# ============================
#
# Try every pair:
#
# Land ride i
# Water ride j
#
# For each pair:
#
# Case 1:
# Land → Water
#
# Finish land:
#
# landFinish = ls + ld
#
# Water starts at:
#
# max(landFinish, ws)
#
# Finish time:
#
# max(ls + ld, ws) + wd
#
# ----------------------------
#
# Case 2:
# Water → Land
#
# Finish water:
#
# waterFinish = ws + wd
#
# Land starts at:
#
# max(waterFinish, ls)
#
# Finish time:
#
# max(ws + wd, ls) + ld
#
# ----------------------------
#
# Take minimum among all
# possible pairs and orders.
#
# ============================

from typing import List
from math import inf

class Solution:

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        n = len(landStartTime)
        m = len(waterStartTime)

        res = inf

        for i in range(n):

            for j in range(m):

                ls = landStartTime[i]
                ld = landDuration[i]

                ws = waterStartTime[j]
                wd = waterDuration[j]

                # ====================
                # Land -> Water
                # ====================
                finish1 = max(
                    ls + ld,
                    ws
                ) + wd

                # ====================
                # Water -> Land
                # ====================
                finish2 = max(
                    ws + wd,
                    ls
                ) + ld

                res = min(
                    res,
                    finish1,
                    finish2
                )

        return res