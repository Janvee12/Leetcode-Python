# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 53. Maximum Subarray
# ============================

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize with first element
        curr_sum = nums[0]
        max_sum = nums[0]

        # Traverse remaining elements
        for i in range(1, len(nums)):

            # Either extend previous subarray
            # or start a new subarray
            curr_sum = max(
                curr_sum + nums[i],
                nums[i]
            )

            # Update maximum sum
            max_sum = max(max_sum, curr_sum)

        return max_sum