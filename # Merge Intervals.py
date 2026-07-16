# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Merge Intervals
# ============================

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals based on their starting time
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = [intervals[0]]

        # Merge overlapping intervals
        for start, end in intervals[1:]:

            last_end = merged_intervals[-1][1]

            # If intervals overlap, update the end time
            if start <= last_end:
                merged_intervals[-1][1] = max(last_end, end)

            # Otherwise, add the current interval
            else:
                merged_intervals.append([start, end])

        return merged_intervals