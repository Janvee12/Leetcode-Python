# ============================
# PLATFORM:
# LeetCode (Problem 396 - Rotate Function)
# ============================

# ============================
# PROBLEM:
# Given an integer array nums of length n, define the rotation function:
#
# F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n-1) * arr_k[n-1]
#
# where arr_k is nums rotated k positions clockwise.
#
# Return the maximum value of F(k) for 0 ≤ k < n.
#
# Example:
# Input: nums = [4, 3, 2, 6]
# Output: 26
#
# ============================

# ============================
# APPROACH:
#
# 1. Compute:
#    - total sum of array → sum_array
#    - F(0) directly → result = sum(i * nums[i])
#
# 2. Use relation to compute next rotations efficiently:
#
#    F(k) = F(k-1) + sum_array - n * nums[n-k]
#
#    (Instead of recomputing from scratch)
#
# 3. Iterate through all rotations and track maximum value.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → One pass to compute F(0) + one pass for rotations
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        pos = n - 1

        # Total sum of array
        sum_array = sum(nums)

        # Compute F(0)
        result = 0
        for i in range(n):
            result += i * nums[i]

        r = result  # store max result

        # Compute F(1) to F(n-1)
        for _ in range(n - 1):
            # Apply formula:
            # F(k) = F(k-1) + sum_array - n * nums[pos]
            result = result + sum_array - n * nums[pos]
            pos -= 1

            r = max(r, result)

        return r