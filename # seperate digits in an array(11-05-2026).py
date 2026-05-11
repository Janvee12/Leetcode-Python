# ============================
# PLATFORM:
# LeetCode (Problem 2553 - Separate the Digits in an Array)
# ============================

# ============================
# PROBLEM:
# Given an array nums containing positive integers,
# separate every digit of each number
# and return all digits in the same order.
#
# Example:
# Input:
# nums = [13,25,83,77]
#
# Output:
# [1,3,2,5,8,3,7,7]
# ============================

# ============================
# APPROACH:
#
# 1. Create helper function separate(num):
#    - Extract digits using:
#          num % 10
#    - Remove last digit using:
#          num // 10
#
# 2. Digits are extracted in reverse order,
#    so reverse the list.
#
# 3. For every number in nums:
#    - get separated digits
#    - append them to answer list
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(d)
#
# d = total number of digits
#
# SPACE COMPLEXITY:
# O(d)
# → output array
# ============================

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        ans = []

        # ============================
        # Helper Function
        # ============================
        def separate(num):

            res = []

            # Extract digits
            while num != 0:

                res.append(num % 10)

                num = num // 10

            # Reverse to maintain original order
            res.reverse()

            return res

        # Process every number
        for num in nums:

            digits = separate(num)

            ans.extend(digits)

        return ans