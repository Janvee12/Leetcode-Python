# ============================
# PLATFORM:
# LeetCode 1358
# PROBLEM:
# Number of Substrings Containing All Three Characters
# ============================

from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        fm = defaultdict(int)   # Frequency map of characters
        res = 0                 # Final answer

        l = 0                   # Left pointer

        # Expand the window
        for r in range(n):

            # Add current character
            fm[s[r]] += 1

            # While window contains a, b and c
            while l < r and all(fm[c] > 0 for c in ['a', 'b', 'c']):

                # Every substring ending from r to n-1 is valid
                res += n - r

                # Shrink the window
                fm[s[l]] -= 1
                l += 1

        return res