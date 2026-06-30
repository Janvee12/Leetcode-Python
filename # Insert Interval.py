# ============================
# PLATFORM:
# LeetCode 57
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

        res = []

        # Traverse all intervals
        for i in range(len(intervals)):

            # Case 1: New interval comes before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: New interval comes after current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: Overlapping intervals
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the merged interval
        res.append(newInterval)

        return res