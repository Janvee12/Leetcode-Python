# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Jump Game
# ============================

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Last index that needs to be reached
        goal = len(nums) - 1

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):

            # Update the goal if the current index can reach it
            if i + nums[i] >= goal:
                goal = i

        # Check if the first index can reach the last index
        return goal == 0