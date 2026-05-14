# ============================
# PLATFORM:
# LeetCode (Problem 18 - 4Sum)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums and an integer target,
# return all unique quadruplets:
#
#     [nums[i], nums[j], nums[left], nums[right]]
#
# such that:
#     nums[i] + nums[j] + nums[left] + nums[right] == target
#
# Constraints:
# - No duplicate quadruplets allowed
#
# Example:
# Input:
# nums = [1,0,-1,0,-2,2]
# target = 0
#
# Output:
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# ============================

# ============================
# APPROACH:
#
# 1. Sort the array.
#
# 2. Fix first two numbers:
#    - i from 0 to n-4
#    - j from i+1 to n-3
#
# 3. Use Two Pointers:
#    - left = j+1
#    - right = n-1
#
# 4. Compute total sum:
#       nums[i] + nums[j] + nums[left] + nums[right]
#
# 5. Adjust pointers:
#    - if sum < target → move left
#    - if sum > target → move right
#    - if equal → store result and skip duplicates
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^3)
#
# - Two nested loops + two pointers
#
# SPACE COMPLEXITY:
# O(1)
# → excluding output list
# ============================

class Solution:

    def fourSum(self, nums, target):

        # Sort array
        nums.sort()

        res = []
        n = len(nums)

        # First number
        for i in range(n - 3):

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second number
            for j in range(i + 1, n - 2):

                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                # Two pointer search
                while left < right:

                    total = (
                        nums[i] +
                        nums[j] +
                        nums[left] +
                        nums[right]
                    )

                    if total == target:

                        res.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left values
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return res