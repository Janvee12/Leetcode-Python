# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Insert Interval
# ============================

from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        result = []

        # Traverse all intervals
        for i in range(len(intervals)):

            # New interval comes before the current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # Current interval comes before the new interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Overlapping intervals
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Append the merged interval
        result.append(newInterval)

        return result