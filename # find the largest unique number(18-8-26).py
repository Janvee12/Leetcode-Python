# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Find the Largest Unique Number
# ============================

from typing import List
from collections import defaultdict


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # If k equals the array length, all elements are included
        if k == n:
            return max(nums)

        # Count the frequency of each number
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        # Find numbers that appear exactly once
        unique_numbers = []

        for num, count in frequency.items():
            if count == 1:
                unique_numbers.append(num)

        # If k is 1, return the largest unique number
        if k == 1:
            return max(unique_numbers) if unique_numbers else -1

        # Check the first and last elements
        first = nums[0] if frequency[nums[0]] == 1 else -1
        last = nums[-1] if frequency[nums[-1]] == 1 else -1

        return max(first, last)