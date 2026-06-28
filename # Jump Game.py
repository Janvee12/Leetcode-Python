# ============================
# PLATFORM:
# LeetCode 55
# PROBLEM:
# Jump Game
# ============================

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Initially, the goal is the last index
        goal = len(nums) - 1

        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):

            # If current index can reach the goal
            if i + nums[i] >= goal:
                goal = i

        # If we can move the goal to index 0
        return goal == 0