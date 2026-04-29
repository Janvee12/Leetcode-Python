class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # ============================
        # PLATFORM:
        # LeetCode (Hard - Binary Search)
        # ============================

        # ============================
        # PROBLEM:
        # Given two sorted arrays nums1 and nums2 of size m and n,
        # return the median of the two sorted arrays.
        #
        # The overall run time complexity should be O(log (m+n)).
        # ============================

        # ============================
        # APPROACH:
        # We use Binary Search on the smaller array.
        #
        # Idea:
        # - We partition both arrays such that:
        #     left part contains half of total elements
        #     right part contains remaining elements
        #
        # Conditions for correct partition:
        #     maxLeftX <= minRightY
        #     maxLeftY <= minRightX
        #
        # If partition is correct:
        #   - If total length is even:
        #       median = (max(left) + min(right)) / 2
        #   - If odd:
        #       median = max(left)
        #
        # If partition is not correct:
        #   - Move left or right using binary search
        # ============================

        # ============================
        # TIME COMPLEXITY:
        # O(log(min(m, n)))
        #
        # SPACE COMPLEXITY:
        # O(1)
        # ============================

        x = len(nums1)
        y = len(nums2)

        # Ensure nums1 is the smaller array
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x

        while low <= high:

            # Partition indices
            px = (low + high) // 2
            py = ((x + y + 1) // 2) - px

            # Edge handling using infinity
            maxLeftX = float('-inf') if px == 0 else nums1[px - 1]
            minRightX = float('inf') if px == x else nums1[px]

            maxLeftY = float('-inf') if py == 0 else nums2[py - 1]
            minRightY = float('inf') if py == y else nums2[py]

            # Correct partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Even total length
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

                # Odd total length
                else:
                    return max(maxLeftX, maxLeftY)

            # Move left
            elif maxLeftX > minRightY:
                high = px - 1

            # Move right
            else:
                low = px + 1