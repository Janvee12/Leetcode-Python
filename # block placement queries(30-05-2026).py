# ============================
# PLATFORM:
# LeetCode
# (Problem 3161 - Block Placement Queries)
# ============================

# ============================
# PROBLEM:
# We process two types of queries:
#
# Type 1:
#   [1, x]
#
#   Place an obstacle at x.
#
# Type 2:
#   [2, x, sz]
#
#   Check whether a block of
#   length sz can fit entirely
#   within range [0, x]
#   without crossing obstacles.
#
# Return results of all
# Type-2 queries.
# ============================

# ============================
# APPROACH:
#
# DATA STRUCTURES:
#
# 1. SortedList
#    Stores obstacle positions.
#
# 2. Segment Tree
#    Stores maximum gap length
#    starting at each obstacle.
#
# ----------------------------
# IDEA:
#
# Obstacles divide the line
# into intervals.
#
# Example:
#
# 0 -------- 20 -------- 50
#
# Gaps:
#
# 20
# 30
#
# Segment tree stores
# the maximum gap.
#
# ----------------------------
#
# Type 1:
#
# Insert obstacle x.
#
# Existing interval:
#
# l -------- r
#
# becomes:
#
# l ---- x ---- r
#
# Update segment tree:
#
# gap(l) = x - l
# gap(x) = r - x
#
# ----------------------------
#
# Type 2:
#
# Need largest free segment
# ending before x.
#
# Query:
#
# max gap before obstacle
# immediately left of x
#
# plus tail segment:
#
# x - previous_obstacle
#
# If maximum >= sz
# answer True.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Insert:
# O(log MX)
#
# Query:
# O(log MX)
#
# Overall:
# O(Q log MX)
#
# SPACE COMPLEXITY:
# O(MX)
# ============================

from sortedcontainers import SortedList
from typing import List

MX = 10 ** 5


# ============================
# Segment Tree
# ============================

class ST:

    def __init__(self):

        self.st = [0] * (4 * (MX + 1))

    # Point update
    def insert(
        self,
        idx,
        val,
        node=1,
        l=0,
        r=MX
    ):

        if l == r:

            self.st[node] = val

            return

        mid = l + (r - l) // 2

        if idx <= mid:

            self.insert(
                idx,
                val,
                node * 2,
                l,
                mid
            )

        else:

            self.insert(
                idx,
                val,
                node * 2 + 1,
                mid + 1,
                r
            )

        self.st[node] = max(
            self.st[node * 2],
            self.st[node * 2 + 1]
        )

    # Range maximum query
    def check(
        self,
        ql,
        qr,
        node=1,
        l=0,
        r=MX
    ):

        if r < ql or l > qr:

            return 0

        if ql <= l and r <= qr:

            return self.st[node]

        mid = l + (r - l) // 2

        return max(
            self.check(
                ql,
                qr,
                node * 2,
                l,
                mid
            ),
            self.check(
                ql,
                qr,
                node * 2 + 1,
                mid + 1,
                r
            )
        )


# ============================
# Solution
# ============================

class Solution:

    def getResults(
        self,
        queries: List[List[int]]
    ) -> List[bool]:

        res = []

        # Obstacles
        obs = SortedList([0, MX])

        st = ST()

        # Initial interval
        st.insert(0, MX)

        for q in queries:

            # ====================
            # Type 1:
            # Add obstacle
            # ====================
            if q[0] == 1:

                _, x = q

                i = obs.bisect_left(x)

                l = obs[i - 1]

                r = obs[i]

                # Split interval
                st.insert(l, x - l)

                st.insert(x, r - x)

                obs.add(x)

            # ====================
            # Type 2:
            # Check block fit
            # ====================
            else:

                _, x, sz = q

                i = obs.bisect_left(x)

                prev_obstacle = obs[i - 1]

                # Largest gap before prev obstacle
                best_gap = st.check(
                    0,
                    prev_obstacle - 1
                )

                # Tail segment ending at x
                tail_gap = x - prev_obstacle

                mx = max(
                    best_gap,
                    tail_gap
                )

                res.append(mx >= sz)

        return res