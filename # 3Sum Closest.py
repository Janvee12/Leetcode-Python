# ============================
# PLATFORM:
# LeetCode (Problem 16 - 3Sum Closest)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums
# and an integer target,
#
# find three integers in nums such that:
#
#     nums[i] + nums[j] + nums[k]
#
# is closest to target.
#
# Return the sum of the three integers.
#
# Example:
# Input:
# nums = [-1,2,1,-4]
# target = 1
#
# Output:
# 2
#
# Explanation:
# (-1 + 2 + 1 = 2)
# which is closest to target 1.
# ============================

# ============================
# APPROACH:
#
# 1. Sort the array.
#
# 2. Fix one element nums[i].
#
# 3. Use Two Pointers:
#    - left = i + 1
#    - right = n - 1
#
# 4. Compute:
#       current_sum
#
# 5. Compare with target:
#    - If current_sum is closer,
#      update closest.
#
# 6. Move pointers:
#    - current_sum < target
#         → increase left
#
#    - current_sum > target
#         → decrease right
#
#    - exact match
#         → return immediately
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
#
# - Sorting: O(n log n)
# - Two-pointer traversal: O(n^2)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:

    def threeSumClosest(self, nums, target):

        # Sort array
        nums.sort()

        # Initial closest sum
        closest = nums[0] + nums[1] + nums[2]

        # Traverse array
        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            # Two-pointer search
            while left < right:

                current_sum = (
                    nums[i] +
                    nums[left] +
                    nums[right]
                )

                # Update closest sum
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Move pointers
                if current_sum < target:

                    left += 1

                elif current_sum > target:

                    right -= 1

                else:
                    # Exact match found
                    return current_sum

        return closest