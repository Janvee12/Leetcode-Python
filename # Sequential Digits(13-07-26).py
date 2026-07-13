# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Sequential Digits
# ============================

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # String containing sequential digits
        digits = "123456789"

        result = []

        # Generate all possible sequential numbers
        for start in range(9):
            for end in range(start, 9):

                number = int(digits[start:end + 1])

                if low <= number <= high:
                    result.append(number)

        # Return numbers in sorted order
        result.sort()
        return result