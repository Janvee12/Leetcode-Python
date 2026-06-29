# ============================
# PLATFORM:
# LeetCode 1967
# PROBLEM:
# Number of Strings That Appear as Substrings in Word
# ============================

from typing import List

class Solution:
    def numOfStrings(
        self,
        patterns: List[str],
        word: str
    ) -> int:

        res = 0

        # Check every pattern
        for p in patterns:

            m = len(p)

            # Try every starting position
            for i in range(len(word) - m + 1):

                j = 0

                # Compare characters one by one
                while j < m and word[i + j] == p[j]:
                    j += 1

                # Entire pattern matched
                if j == m:
                    res += 1
                    break

        return res