# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 1840. Maximum Building Height
# ============================

# ============================
# PROBLEM:
# ============================
#
# There are n buildings numbered
# from 1 to n.
#
# Rules:
#
# 1. Building 1 has height 0.
#
# 2. Adjacent buildings can differ
#    in height by at most 1.
#
# 3. Some buildings have maximum
#    height restrictions.
#
# Find the maximum possible height
# of any building.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# 1. Add building 1 with height 0.
#
# 2. Add building n if it does not
#    exist.
#
# 3. Sort restrictions.
#
# 4. Left → Right pass:
#    propagate restrictions.
#
# 5. Right → Left pass:
#    propagate restrictions.
#
# 6. For every adjacent pair of
#    restrictions, calculate the
#    maximum peak between them.
#
# ============================

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        # Building 1 always has height 0
        restrictions.append([1, 0])

        # Sort by building number
        restrictions.sort()

        # Add building n if absent
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        m = len(restrictions)

        # ============================
        # LEFT TO RIGHT
        # ============================
        for i in range(1, m):

            dist = (
                restrictions[i][0]
                - restrictions[i - 1][0]
            )

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # ============================
        # RIGHT TO LEFT
        # ============================
        for i in range(m - 2, -1, -1):

            dist = (
                restrictions[i + 1][0]
                - restrictions[i][0]
            )

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        # ============================
        # FIND MAXIMUM PEAK
        # ============================
        answer = 0

        for i in range(1, m):

            dist = (
                restrictions[i][0]
                - restrictions[i - 1][0]
            )

            h1 = restrictions[i - 1][1]
            h2 = restrictions[i][1]

            peak = (dist + h1 + h2) // 2

            answer = max(answer, peak)

        return answer