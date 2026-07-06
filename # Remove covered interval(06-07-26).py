# ============================
# PLATFORM:
# LeetCode 1288
# PROBLEM:
# Remove Covered Intervals
# ============================

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        n = len(intervals)

        # Sort by decreasing start,
        # and increasing end.
        intervals.sort(key=lambda x: (-x[0], x[1]))

        res = [intervals[0]]

        for i in range(1, n):

            # Remove intervals that are
            # completely covered.
            while (
                res and
                res[-1][0] >= intervals[i][0] and
                res[-1][1] <= intervals[i][1]
            ):
                res.pop()

            res.append(intervals[i])

        return len(res)