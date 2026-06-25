# ============================
# PLATFORM:
# LeetCode Contest
# PROBLEM:
# Count Majority Subarrays
# ============================

from typing import List

class Solution:
    def countMajoritySubarrays(
        self,
        nums: List[int],
        target: int
    ) -> int:

        n = len(nums)
        res = 0

        # Choose starting index
        for i in range(n):

            targetc = 0

            # Extend subarray
            for j in range(i, n):

                # Count occurrences of target
                if nums[j] == target:
                    targetc += 1

                # Length of current subarray
                length = j - i + 1

                # Target is majority
                if targetc > length // 2:
                    res += 1

        return res