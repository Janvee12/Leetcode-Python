# ============================
# PLATFORM:
# LeetCode
# (Partition Array According to Pivot)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given an array nums and a pivot value.
#
# Rearrange the array such that:
#
# 1. All elements < pivot come first
# 2. Then all elements == pivot
# 3. Then all elements > pivot
#
# Order within groups should be preserved.
#
# ============================
# APPROACH:
# ============================
#
# We use 3 separate lists:
#
#   less   → elements < pivot
#   equal  → elements == pivot
#   greater→ elements > pivot
#
# Then concatenate them.
#
# ============================


from typing import List

class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        # ============================
        # STEP 1: Create buckets
        # ============================
        less = []
        equal = []
        greater = []

        # ============================
        # STEP 2: Distribute elements
        # ============================
        for num in nums:

            if num < pivot:
                less.append(num)

            elif num == pivot:
                equal.append(num)

            else:
                greater.append(num)

        # ============================
        # STEP 3: Combine results
        # ============================
        return less + equal + greater