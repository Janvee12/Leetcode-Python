# ============================
# PLATFORM:
# LeetCode
# (Problem 31 - Next Permutation)
# ============================

# ============================
# PROBLEM:
# Rearrange numbers into the
# lexicographically next
# greater permutation.
#
# If such arrangement
# is not possible,
# rearrange into the
# lowest possible order
# (ascending order).
#
# Must modify array in-place.
#
# Example:
#
# Input:
# nums = [1,2,3]
#
# Output:
# [1,3,2]
#
# Example:
#
# Input:
# nums = [3,2,1]
#
# Output:
# [1,2,3]
# ============================

# ============================
# APPROACH:
#
# Key Idea:
#
# Find first decreasing element
# from the right.
#
# Steps:
#
# 1. Traverse from right
#    to find pivot:
#
#       nums[i-1] < nums[i]
#
# 2. If no pivot exists:
#
#       reverse entire array
#
# 3. Otherwise:
#
#    Find next larger element
#    from the right.
#
# 4. Swap them.
#
# 5. Reverse suffix
#    after pivot index
#    to get smallest order.
#
# ============================

# ============================
# EXAMPLE:
#
# nums = [1,2,7,4,3,1]
#
# Pivot:
#        2
#
# Swap with:
#        3
#
# Result:
# [1,3,1,2,4,7]
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution(object):

    def nextPermutation(self, nums):

        """
        :type nums: List[int]
        :rtype: None
        Do not return anything,
        modify nums in-place instead.
        """

        # ====================
        # Find pivot
        # ====================
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:

            i -= 1

        # ====================
        # Entire array descending
        # ====================
        if i < 1:

            nums[:] = nums[::-1]

        else:

            # ====================
            # Find next larger element
            # ====================
            j = len(nums) - 1

            while nums[j] <= nums[i - 1]:

                j -= 1

            # Swap
            nums[j], nums[i - 1] = (
                nums[i - 1],
                nums[j]
            )

            # Reverse suffix
            nums[i:] = nums[i:][::-1]