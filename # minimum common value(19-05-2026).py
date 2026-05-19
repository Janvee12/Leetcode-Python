# ============================
# PLATFORM:
# LeetCode (Problem 2540 - Minimum Common Value)
# ============================

# ============================
# PROBLEM:
# Given two sorted integer arrays:
#
#     nums1 and nums2
#
# Return the minimum integer
# common to both arrays.
#
# If there is no common integer,
# return -1.
#
# Example:
#
# Input:
# nums1 = [1,2,3]
# nums2 = [2,4]
#
# Output:
# 2
#
# Example:
#
# Input:
# nums1 = [1,2,3,6]
# nums2 = [2,3,4,5]
#
# Output:
# 2
# ============================

# ============================
# APPROACH:
#
# Use TWO POINTERS
#
# Since arrays are already sorted:
#
# 1. Compare nums1[i] and nums2[j]
#
# 2. If equal:
#       common value found
#
# 3. If nums1[i] < nums2[j]:
#       move i forward
#
# 4. Otherwise:
#       move j forward
#
# 5. If no common value exists:
#       return -1
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + m)
#
# n = len(nums1)
# m = len(nums2)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import List

class Solution:

    def getCommon(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> int:

        # Two pointers
        i, j = 0, 0

        # Traverse both arrays
        while i < len(nums1) and j < len(nums2):

            # Common value found
            if nums1[i] == nums2[j]:

                return nums1[i]

            # Move pointer of smaller value
            elif nums1[i] < nums2[j]:

                i += 1

            else:

                j += 1

        # No common value
        return -1