# ============================
# PLATFORM:
# LeetCode
# (Problem 26 - Remove Duplicates from Sorted Array)
# ============================

# ============================
# PROBLEM:
# Given a sorted array nums,
# remove duplicates in-place
# such that each unique element
# appears only once.
#
# Return the number of
# unique elements.
#
# The first k elements of nums
# should contain the final result.
#
# Example:
#
# Input:
# nums = [1,1,2]
#
# Output:
# 2
#
# nums becomes:
# [1,2,_]
#
# Example:
#
# Input:
# nums = [0,0,1,1,1,2,2,3,3,4]
#
# Output:
# 5
#
# nums becomes:
# [0,1,2,3,4,_,_,_,_,_]
# ============================

# ============================
# APPROACH:
#
# Use TWO POINTERS
#
# l -> position to place
#      next unique element
#
# r -> scans array
#
# Steps:
#
# 1. Start l from index 1
#    because first element
#    is always unique.
#
# 2. Traverse array using r.
#
# 3. If current element differs
#    from previous:
#
#       nums[l] = nums[r]
#       l += 1
#
# 4. Return l
#    (count of unique elements)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def removeDuplicates(
        self,
        nums: List[int]
    ) -> int:

        # Position for next unique element
        l = 1

        # Traverse array
        for r in range(1, len(nums)):

            # Found new unique element
            if nums[r] != nums[r - 1]:

                nums[l] = nums[r]

                l += 1

        # Number of unique elements
        return l