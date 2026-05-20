# ============================
# PLATFORM:
# LeetCode
# (Problem 2657 - Find the Prefix Common Array of Two Arrays)
# ============================

# ============================
# PROBLEM:
# You are given two arrays:
#
#     A and B
#
# Both arrays are permutations
# of integers from 1 to n.
#
# Prefix Common Array:
#
# C[i] = number of common elements
#        between:
#
#        A[0...i]
#        B[0...i]
#
# Task:
# Return the prefix common array C.
#
# Example:
#
# Input:
# A = [1,3,2,4]
# B = [3,1,2,4]
#
# Output:
# [0,2,3,4]
#
# Explanation:
#
# i = 0
# A prefix = [1]
# B prefix = [3]
# common = 0
#
# i = 1
# A prefix = [1,3]
# B prefix = [3,1]
# common = 2
# ============================

# ============================
# APPROACH:
#
# Use TWO SETS
#
# Steps:
#
# 1. Maintain:
#
#       setA -> elements seen in A
#       setB -> elements seen in B
#
# 2. Traverse arrays together.
#
# 3. Add current elements
#    into both sets.
#
# 4. Check:
#
#    - If A[i] already exists in setB
#         increase common count
#
#    - If B[i] already exists in setA
#      and A[i] != B[i]
#         increase common count
#
# 5. Store common count in answer.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from typing import List

class Solution:

    def findThePrefixCommonArray(
        self,
        A: List[int],
        B: List[int]
    ) -> List[int]:

        n = len(A)

        # Result array
        ans = []

        # Seen elements
        setA = set()
        setB = set()

        # Current common count
        common = 0

        # Traverse arrays
        for i in range(n):

            # Add current elements
            setA.add(A[i])

            setB.add(B[i])

            # A[i] exists in B prefix
            if A[i] in setB:

                common += 1

            # B[i] exists in A prefix
            # Avoid double counting
            if B[i] in setA and A[i] != B[i]:

                common += 1

            # Store result
            ans.append(common)

        return ans