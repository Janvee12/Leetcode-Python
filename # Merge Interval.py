# ============================
# PLATFORM:
# LeetCode 56
# PROBLEM:
# Merge Intervals
# ============================

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals according to starting point
        intervals.sort(key=lambda i: i[0])

        # Add first interval
        output = [intervals[0]]

        # Traverse remaining intervals
        for start, end in intervals[1:]:

            # End of last merged interval
            lastEnd = output[-1][1]

            # Overlapping intervals
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            # Non-overlapping interval
            else:
                output.append([start, end])

        return output