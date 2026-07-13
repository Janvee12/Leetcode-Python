# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Maximum Subarray
# ============================

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize current and maximum sum
        current_sum = maximum_sum = nums[0]

        # Traverse the array
        for i in range(1, len(nums)):

            # Either extend the current subarray or start a new one
            current_sum = max(current_sum + nums[i], nums[i])

            # Update the maximum subarray sum
            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum